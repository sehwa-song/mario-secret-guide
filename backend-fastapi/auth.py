import os
import re
import time
import jwt
from users import find_public
from errors import ApiError


# PyJWT는 requirements.txt에 포함되어 있습니다. 아래 함수를 완성하세요.
def issue_token(user): # 로그인 성공 시 JWT 발급
    # 1. 서버 환경변수에서 비밀 키 가져오기
    secret_hex = os.getenv("JWT_SECRET", "")

    # 2. 비밀 키 형식 확인
    if not re.fullmatch(r"[0-9a-fA-F]{64}", secret_hex):
        raise RuntimeError("JWT_SECRET 설정이 올바르지 않습니다.")

    # 3. JWT 유효 시간 확인
    ttl = int(os.getenv("TOKEN_TTL", "90"))
    if ttl <= 0:
        raise RuntimeError("TOKEN_TTL은 양수여야 합니다.")

    # 4. 발급자와 사용 대상 확인
    issuer = os.getenv("JWT_ISSUER", "")
    audience = os.getenv("JWT_AUDIENCE", "")

    if not issuer or not audience:
        raise RuntimeError("JWT 발급자 또는 사용 대상 설정이 없습니다.")

    # 5. JWT에 담을 사용자 정보 구성
    now = int(time.time())

    payload = {
        "sub": str(user["id"]), # sub: 토큰의 주체인 사용자 id
        "exp": now + ttl, # 토큰이 만료되는 시각
        "iss": issuer, # JWT를 발급한 주체
        "aud": audience, # JWT를 사용할 대상
    }

    # 6. 비밀 키로 서명한 JWT 발급
    return jwt.encode(
        payload,
        bytes.fromhex(secret_hex),
        algorithm="HS256",
    )

def current_user_id(request): # 전달받은 JWT 검증
    # 1. Authorization 헤더 확인
    authorization = request.headers.get("Authorization", "")
    parts = authorization.split()

    if len(parts) != 2 or parts[0].lower() != "bearer":
        raise ApiError(401, "TOKEN_REQUIRED", "Bearer 토큰이 필요합니다.")

    token = parts[1]

    # 2. 서버의 JWT 설정 확인
    secret_hex = os.getenv("JWT_SECRET", "")
    issuer = os.getenv("JWT_ISSUER", "")
    audience = os.getenv("JWT_AUDIENCE", "")

    if not re.fullmatch(r"[0-9a-fA-F]{64}", secret_hex):
        raise RuntimeError("JWT_SECRET 설정이 올바르지 않습니다.")

    if not issuer or not audience:
        raise RuntimeError("JWT 발급자 또는 사용 대상 설정이 없습니다.")

    # 3. JWT 서명과 만료 시간, 필수 정보 검증
    try:
        payload = jwt.decode(
            token,
            bytes.fromhex(secret_hex),
            algorithms=["HS256"],
            issuer=issuer,
            audience=audience,
            options={"require": ["sub", "exp", "iss", "aud"]},
        )

    except jwt.ExpiredSignatureError:
        raise ApiError(401, "TOKEN_EXPIRED", "토큰이 만료되었습니다.")

    except jwt.InvalidTokenError:
        raise ApiError(401, "INVALID_TOKEN", "유효하지 않은 토큰입니다.")

    # 4. 실제 사용자가 존재하는지 확인
    subject = payload.get("sub")

    if not isinstance(subject, str) or not re.fullmatch(r"[1-9][0-9]*", subject):
        raise ApiError(401, "INVALID_TOKEN", "사용자 ID가 올바르지 않습니다.")

    user_id = int(subject)

    if not find_public(user_id):
        raise ApiError(401, "INVALID_TOKEN", "존재하지 않는 사용자입니다.")

    # 5. 검증된 사용자 ID 반환
    return user_id


def assert_owner(user_id, author_id): # 게시글 작성자 권한 검사
    # 로그인한 사용자와 게시글 작성자가 다르면 거부
    if user_id != author_id:
        raise ApiError(
            403,
            "FORBIDDEN",
            "자신의 게시글만 수정하거나 삭제할 수 있습니다."
        )
