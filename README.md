# Mario Secret Guide

## 1. 프로젝트 소개

Mario Secret Guide는 닌텐도 DS 게임인 뉴 슈퍼 마리오브라더스의 숨겨진 월드와 비밀 출구 공략을 공유하기 위한 JWT 인증 기반 웹 게시판 서비스입니다.

사용자는 로그인하지 않아도 공략 게시글을 조회할 수 있으며, 로그인한 사용자는 게시글을 작성할 수 있습니다. 게시글 수정과 삭제는 작성자 본인에게만 허용됩니다.

본 프로젝트는 웹서비스설계 개인 과제로 진행하였으며, 제공된 게시판 CRUD 시작 코드를 기반으로 JWT 인증, 작성자 권한 검사, React 로그인 연동 및 오류 처리 기능을 완성하였습니다.

**개발자:** 송세화

**개발일:** 2026.10.28

**구현 환경:** macOS, VS Code, Chrome

## 2. 기술 스택

| 구분 | 기술 |
|---|---|
| Frontend | React, Vite, JavaScript |
| Backend | Python, FastAPI, Uvicorn |
| Database | SQLite |
| Authentication | JWT (HS256) |
| Package Manager | npm, pip |
| Development | VS Code, Git, Chrome DevTools |

프로젝트는 React 프론트엔드와 FastAPI 백엔드로 구성됩니다. 프론트엔드는 API 요청과 화면 표시를 담당하고, 백엔드는 JWT 인증·권한 검사·게시글 데이터 처리를 담당합니다.

## 3. 구현 기능

| 기능 | 구현 상태 |
|---|---|
| 비로그인 게시글 목록 및 상세 조회 | 완료 |
| Alice·Bob 계정 로그인 | 완료 |
| JWT 발급 및 서명 검증 | 완료 |
| JWT를 이용한 현재 사용자 조회 | 완료 |
| Bearer 토큰 자동 전송 | 완료 |
| 로그인 사용자 게시글 작성 | 완료 |
| 작성자 본인 게시글 수정·삭제 | 완료 |
| 다른 작성자의 수정·삭제 거부 | 완료 |
| JWT 누락·변조·만료 오류 처리 | 완료 |
| 작성자 ID 위조 방지 | 완료 |
| 제목·본문 입력값 검증 | 완료 |
| 로그아웃 및 로그인 상태 초기화 | 완료 |
| 서버 재시작 후 게시글 데이터 유지 | 완료 |

현재 서비스는 게임 공략을 게시글 형태로 공유하는 기본 게시판입니다. 월드별 검색·분류와 이미지 업로드 기능은 포함하지 않았습니다.

## 4. 프로젝트 구조

```text
JWT-Assignment/
├── backend-fastapi/
│   ├── app.py
│   ├── auth.py
│   ├── users.py
│   ├── store.py
│   ├── errors.py
│   ├── requirements.txt
│   └── README.md
├── frontend-react/
│   ├── src/
│   │   ├── api.js
│   │   └── main.jsx
│   ├── index.html
│   ├── package.json
│   ├── package-lock.json
│   └── vite.config.js
├── docs/
│   ├── report.pdf
│   ├── 개발기록.md
│   ├── 05_테스트시나리오.md
│   ├── evidence.md
│   └── evidence/
├── tools/
│   └── check_api.py
├── README.md
└── .gitignore
```

`report.pdf`는 최종 보고서 변환 후 추가합니다. `evidence/`에는 테스트 캡처 파일을 보관합니다.

## 5. 실행 환경 및 사전 준비

다음 프로그램이 필요합니다.

- Python 3.10 이상
- Node.js 20.19 이상
- npm
- Git

실제 설치된 버전은 다음 명령어로 확인할 수 있습니다.

```bash
python3 --version
node --version
npm --version
git --version
```

본 프로젝트는 별도의 클라우드 서버나 외부 데이터베이스 없이 로컬 환경에서 실행합니다.

## 6. 프로젝트 다운로드

GitHub 저장소를 clone합니다.

```bash
git clone <GitHub 저장소 URL>
cd JWT-Assignment
```

GitHub 저장소 URL은 저장소 생성 후 실제 주소로 변경합니다.

## 7. FastAPI 백엔드 실행

### 7.1 Python 가상환경 생성

프로젝트의 백엔드 폴더로 이동합니다.

```bash
cd backend-fastapi
python3 -m venv .venv
```

가상환경은 프로젝트에서 필요한 Python 패키지를 독립적으로 관리하기 위해 사용합니다.

### 7.2 의존성 설치

```bash
.venv/bin/python -m pip install -r requirements.txt
```

### 7.3 JWT 환경변수 설정

JWT는 서버의 비밀 키를 사용하여 HS256 알고리즘으로 서명합니다.

FastAPI 백엔드는 `.env` 파일에서 JWT 관련 환경변수를 읽습니다. GitHub에서 프로젝트를 다운로드한 후 다음 절차에 따라 설정해야 합니다.

**① 환경변수 예시 파일 복사**

`backend-fastapi` 폴더에서 다음 명령어를 실행합니다.

```bash
cp .env.example .env
```

**② JWT 비밀 키 생성**

Python의 `secrets` 모듈을 이용하여 무작위 32바이트 키를 생성합니다.

```bash
python3 -c "import secrets; print(secrets.token_hex(32))"
```

출력된 64자리 16진수 문자열을 `.env` 파일의 `JWT_SECRET` 값으로 설정합니다.

**③ 나머지 환경변수 확인**

`.env.example`에 정의된 JWT 관련 설정을 확인합니다.

| 환경변수 | 역할 |
|---|---|
| JWT_SECRET | JWT 서명 및 검증에 사용하는 비밀 키 |
| JWT_ISSUER | JWT 발급자 |
| JWT_AUDIENCE | JWT 사용 대상 |
| TOKEN_TTL | JWT 유효 시간(초) |

일반 실행 시 `TOKEN_TTL`은 90초로 설정합니다. 발급자와 사용 대상은 실제 백엔드 설정값을 유지합니다.

Fast

### 7.4 백엔드 서버 실행

```bash
.venv/bin/python -m uvicorn app:app --host 127.0.0.1 --port 8000
```

정상 실행 시 다음 메시지를 확인할 수 있습니다.

```text
Application startup complete.
Uvicorn running on http://127.0.0.1:8000
```

서버 상태 확인:

http://127.0.0.1:8000/api/health

정상 응답은 HTTP 200 OK입니다.

## 8. React 프론트엔드 실행

백엔드 서버는 실행한 상태로 유지하고 새 터미널을 엽니다.

프로젝트 루트에서 프론트엔드 폴더로 이동합니다.

```bash
cd frontend-react
```

### 8.1 의존성 설치

```bash
npm ci
```

### 8.2 개발 서버 실행

```bash
npm run dev
```

개발 서버 접속 주소:

http://127.0.0.1:5173

### 8.3 최종 빌드 및 실행

개발 서버를 종료한 뒤 다음 명령어를 실행합니다.

```bash
npm run build
npm run preview
```

빌드 미리보기 접속 주소:

http://127.0.0.1:4173

Vite 프록시는 `/api` 요청을 FastAPI 백엔드의 8000번 포트로 전달합니다.

최종 기능 검증은 4173번 포트에서 진행하였습니다.

### 8.4 서버 종료

각 서버가 실행 중인 터미널에서 `Control + C`를 눌러 종료할 수 있습니다.

## 9. 테스트 계정

과제에서 제공된 테스트 계정을 사용합니다.

| 사용자 | 이메일 | 비밀번호 |
|---|---|---|
| Alice | alice@class.test | Classroom!2026 |
| Bob | bob@class.test | Classroom!2026 |

두 계정은 인증과 작성자 권한 검사 기능을 확인하는 데 사용합니다.

별도의 회원가입 기능은 이번 과제에 포함하지 않았습니다.

## 10. SQLite 데이터 저장

게시글 데이터는 SQLite 파일 데이터베이스에 저장됩니다.

기본 데이터베이스 경로:

`backend-fastapi/data/board.sqlite`

초기 DB 파일이 없는 경우 백엔드 실행 시 생성되는 구조입니다.

데이터베이스에는 게시글 ID, 제목, 본문, 작성자 ID, 생성 시각 및 수정 시각 등의 정보가 저장됩니다.

서버 재시작 이후에도 저장된 게시글 데이터가 유지되는지 T15에서 검증하였습니다.

**주의:** 실제 SQLite DB 파일은 GitHub에 업로드하지 않습니다. 실행 과정에서 자동으로 생성되도록 구성합니다.

## 11. 주요 API

| HTTP Method | API | 기능 | 인증 |
|---|---|---|---|
| GET | /api/health | 서버 상태 확인 | 불필요 |
| POST | /api/auth/login | 로그인 및 JWT 발급 | 불필요 |
| GET | /api/me | 현재 사용자 조회 | 필요 |
| GET | /api/posts | 게시글 목록 조회 | 불필요 |
| GET | /api/posts/{id} | 게시글 상세 조회 | 불필요 |
| POST | /api/posts | 게시글 등록 | 필요 |
| PUT | /api/posts/{id} | 게시글 수정 | 작성자 본인 |
| DELETE | /api/posts/{id} | 게시글 삭제 | 작성자 본인 |

### JWT 인증

정상 로그인 시 서버는 `accessToken`, `expiresIn`, `user` 정보를 반환합니다.

React는 JWT를 JavaScript 메모리에 보관하며, 인증이 필요한 요청에 다음 헤더를 추가합니다.

```text
Authorization: Bearer <JWT>
```

서버는 서명·만료 시각·필수 클레임을 검증한 후 인증된 사용자 ID를 확인합니다.

게시글 수정·삭제 요청에서는 검증된 사용자 ID와 게시글 작성자 ID를 비교합니다.

## 12. HTTP 오류 처리

| HTTP | JSON code | 처리 내용 |
|---|---|---|
| 400 | BAD_INPUT | 입력값 및 ID 형식 오류 |
| 401 | INVALID_CREDENTIALS | 로그인 실패 |
| 401 | TOKEN_REQUIRED | JWT 누락 |
| 401 | INVALID_TOKEN | JWT 변조 또는 검증 실패 |
| 401 | TOKEN_EXPIRED | JWT 만료 |
| 403 | FORBIDDEN | 작성자 권한 부족 |
| 404 | NOT_FOUND | 게시글 없음 |

JWT 인증 실패와 작성자 권한 부족은 서로 다른 오류로 처리합니다.

HTTP 401이 발생하면 React에서 로그인 상태를 초기화합니다. 반면 HTTP 403은 해당 요청의 권한 부족을 나타내며 JWT 자체가 무효하다는 뜻은 아닙니다.

## 13. 테스트 결과

T01~T17 수동 테스트를 수행하였습니다.

주요 검증 결과는 다음과 같습니다.

| 검증 항목 | 실제 결과 |
|---|---|
| 비로그인 목록·상세 조회 | 200 OK |
| 정상 로그인 | 200 OK, JWT 발급 |
| 잘못된 로그인 | 401 INVALID_CREDENTIALS |
| 토큰 누락 | 401 TOKEN_REQUIRED |
| 토큰 변조 | 401 INVALID_TOKEN |
| 토큰 만료 | 401 TOKEN_EXPIRED |
| 다른 작성자 수정·삭제 | 403 FORBIDDEN |
| 작성자 ID 위조 | 400 BAD_INPUT |
| 정상 게시글 작성 | 201 Created |
| 본인 게시글 수정 | 200 OK |
| 본인 게시글 삭제 | 204 No Content |
| 서버 재시작 후 데이터 조회 | 200 OK, 데이터 유지 |

모든 주요 검증은 Chrome 개발자 도구에서 HTTP 상태와 JSON 응답을 직접 확인하는 방식으로 진행하였습니다.

별도 제공된 자동 검사 도구는 다음 명령어로 실행할 수 있습니다.

```bash
python3 tools/check_api.py --mode final
```

자동 검사 실행 결과는 수동 검증 결과와 구분하여 기록합니다. 자동 검사 실행 완료 여부는 최종 제출 전 확인합니다.

## 14. 보고서 및 테스트 증거

- [최종 구현 보고서](docs/report.pdf)
- [T01~T17 테스트 시나리오](docs/05_테스트시나리오.md)
- [테스트 증거 목록](docs/evidence.md)
- [테스트 캡처 폴더](docs/evidence/)
- [개발 기록](docs/개발기록.md)

보고서에는 JWT 발급·검증, 작성자 권한 검사, React 인증 연동 및 실제 HTTP 테스트 결과를 기록하였습니다.

테스트 증거에는 HTTP 상태, JSON 오류 코드, 데이터 유지 여부를 확인한 캡처본을 포함합니다.

## 15. AI 활용 및 참고 자료

본 과제에서는 OpenAI ChatGPT를 개발 학습 및 코드 작성 보조 도구로 활용하였습니다.

주요 활용 영역은 다음과 같습니다.

- JWT 비밀 키 생성 및 인증 구조 학습
- JWT 저장·전송을 위한 React 코드 작성 보조
- HTTP 401 발생 시 로그인 상태 처리
- 작성자 권한에 따른 수정·삭제 기능 연결
- API 테스트 코드 작성 및 결과 분석
- 개발 기록과 구현 보고서 작성 보조

AI 제안 코드를 참고하여 직접 개발 환경에 적용하고, 실제 HTTP 응답과 데이터 상태를 확인하는 방식으로 검증하였습니다.

관련 수업 자료는 웹서비스설계 02·03·06·07주차 강의자료를 참고하였습니다.

AI 사용 범위 및 대표 사례의 자세한 내용은 최종 구현 보고서에 기록하였습니다.

## 16. 구현 범위 및 제한사항

현재 구현한 기능은 공개 게시글 조회, JWT 인증, 본인 글 작성·수정·삭제, 작성자 권한 검사 및 SQLite 데이터 유지입니다.

다음 기능은 이번 과제의 구현 범위에 포함하지 않았습니다.

- 회원가입 및 비밀번호 재설정
- Refresh Token 발급
- 서버 측 JWT 즉시 철회
- 월드별 게시글 검색 및 분류
- 이미지 첨부
- 외부 서버 및 클라우드 배포

현재 로그아웃은 브라우저 메모리에 저장된 JWT를 제거하는 방식이며, 이미 복사된 JWT를 서버에서 즉시 폐기하지는 않습니다.

## 17. 제출 안내

본 프로젝트는 웹서비스설계 개인 과제 제출용입니다.

GitHub 저장소에는 React·FastAPI 소스 코드, 실행 안내 README, 최종 보고서 및 테스트 증거를 포함합니다.

실제 JWT 비밀 키, `.env`, `node_modules`, `.venv`, SQLite 데이터베이스 파일은 제출 대상에서 제외합니다.

최종 GitHub 저장소 URL과 제출 기준 커밋 SHA는 LMS에 제출합니다.