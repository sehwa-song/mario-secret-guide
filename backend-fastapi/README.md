# Mario Secret Guide — FastAPI 백엔드

React와 연동하여 JWT 인증, 사용자 확인, 게시글 작성자 권한 검사 및 SQLite 데이터 저장을 처리하는 FastAPI 백엔드입니다.

## 실행 환경

Python 3.10 이상이 필요합니다.

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

### JWT 환경변수 설정

`.env.example`을 `.env`로 복사합니다.

```bash
cp .env.example .env
```

Python의 `secrets` 모듈을 이용하여 JWT 서명에 사용할 32바이트 난수를 생성합니다.

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

출력된 64자리 16진수 값을 `.env`의 `JWT_SECRET`에 설정합니다.

나머지 환경변수는 `.env.example`의 설정을 참고합니다. `load_dotenv()`가 `.env` 설정을 읽습니다.

실제 `.env` 파일과 JWT 비밀 키는 GitHub에 업로드하지 않습니다.

### FastAPI 서버 실행

```bash
python -m uvicorn app:app --host 127.0.0.1 --port 8000
```

서버 상태 확인:

http://127.0.0.1:8000/api/health

FastAPI API 문서:

http://127.0.0.1:8000/docs

### Windows PowerShell

```powershell
py -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe -m uvicorn app:app --host 127.0.0.1 --port 8000
```

Windows에서도 `.env.example`을 복사하여 `.env`를 준비하고 JWT_SECRET을 설정해야 합니다.

## 구현 기능

| 관련 파일 | 기능 |
|---|---|
| `app.py` | HTTP API 경로 및 입력 검증 |
| `auth.py` | JWT 발급·검증 및 작성자 권한 검사 |
| `users.py` | 사용자 계정 확인 및 scrypt 비밀번호 검증 |
| `store.py` | SQLite 게시글 데이터 저장·조회 |
| `errors.py` | HTTP 오류 및 JSON 오류 응답 처리 |

JWT 발급, JWT 검증, 사용자 ID 확인 및 게시글 작성자 권한 검사 기능을 구현하였습니다.

## 데이터베이스

SQLite 파일 경로:

`data/board.sqlite`

초기 DB 파일이 없으면 서버 실행 과정에서 자동으로 생성됩니다.

데이터베이스를 초기화하려면 FastAPI 서버를 종료한 후 `data/board.sqlite` 파일을 삭제하고 다시 실행합니다.

이 작업은 기존 게시글을 모두 삭제하므로 주의해야 합니다.

## JWT 인증과 만료 처리

JWT는 HS256 알고리즘으로 발급 및 검증합니다.

기본 유효 시간은 90초입니다.

만료 검증 시에는 `.env`의 `TOKEN_TTL`을 3초로 변경한 뒤 서버를 재시작하여 테스트하였습니다.

테스트 완료 후에는 일반 설정인 90초로 복구합니다.

인증 실패 및 권한 오류에는 다음 응답을 사용합니다.

| HTTP 상태 | JSON code |
|---|---|
| 401 | TOKEN_REQUIRED |
| 401 | INVALID_TOKEN |
| 401 | TOKEN_EXPIRED |
| 403 | FORBIDDEN |

T01~T17 테스트를 통해 JWT 인증, 작성자 권한 및 게시글 CRUD를 검증하였습니다.

자세한 테스트 결과는 프로젝트 루트의 `docs/05_테스트시나리오.md`와 최종 구현 보고서를 참고하세요.