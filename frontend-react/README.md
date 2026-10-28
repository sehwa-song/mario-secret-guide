# Mario Secret Guide — React 프론트엔드

## 1. 프로젝트 소개

Mario Secret Guide는 닌텐도 DS 게임인 뉴 슈퍼 마리오브라더스의 숨겨진 월드와 비밀 출구 공략을 공유하기 위한 JWT 인증 기반 웹 게시판입니다.

이 폴더는 React와 Vite를 이용한 프론트엔드 프로젝트입니다.

사용자는 로그인하지 않아도 게시글을 조회할 수 있으며, 로그인한 사용자는 게시글을 작성할 수 있습니다. 게시글 수정과 삭제는 작성자 본인에게만 허용됩니다.

프론트엔드는 사용자 화면과 상태 관리를 담당하며, 인증·권한 검사와 데이터 저장은 FastAPI 백엔드에서 처리합니다.

## 2. 실행 환경

- Node.js 20.19 이상
- npm
- React
- Vite
- FastAPI 백엔드 (127.0.0.1:8000)

프론트엔드를 실행하기 전에 `backend-fastapi` 서버를 먼저 실행해야 합니다.

백엔드 실행 방법은 `../backend-fastapi/README.md`를 참고합니다.

## 3. 프론트엔드 설치 및 개발 서버 실행

프로젝트의 `frontend-react` 폴더에서 실행합니다.

### 3.1 의존성 설치

```bash
npm ci
```

`package-lock.json`에 기록된 의존성 버전을 기준으로 필요한 패키지를 설치합니다.

### 3.2 개발 서버 실행

```bash
npm run dev
```

브라우저 접속 주소:

http://127.0.0.1:5173

Vite 개발 서버는 React 파일을 브라우저에 제공하며, `/api` 요청을 FastAPI 백엔드의 8000번 포트로 전달합니다.

따라서 개발 환경에서는 별도의 CORS 설정 없이 Vite 프록시를 통해 API를 호출합니다.

## 4. 로컬 빌드 및 최종 실행

이번 과제의 최종 검증은 개발 서버가 아니라 빌드 결과를 이용하여 진행합니다.

개발 서버가 실행 중이라면 `Control + C`로 종료합니다.

### 4.1 프론트엔드 빌드

```bash
npm run build
```

React 애플리케이션의 빌드 결과는 `dist/` 폴더에 생성됩니다.

### 4.2 빌드 결과 실행

```bash
npm run preview
```

브라우저 접속 주소:

http://127.0.0.1:4173

Vite Preview 서버에서도 `/api` 요청이 FastAPI 백엔드로 전달됩니다.

프론트엔드 코드를 수정한 경우에는 `npm run build`를 다시 실행한 후 Preview 서버에서 변경 사항을 확인해야 합니다.

**포트 구분**

| 포트 | 역할 |
|---|---|
| 5173 | React 개발 서버 |
| 4173 | React 빌드 미리보기 서버 |
| 8000 | FastAPI 백엔드 서버 |

백엔드 포트를 변경하면 `vite.config.js`의 개발 및 미리보기 프록시 설정도 함께 수정해야 합니다.

## 5. 구현 기능

### FE-01. 로그인 기능 및 JWT 저장

관련 파일: `src/api.js`

관련 함수: `login()`

사용자가 입력한 이메일과 비밀번호를 JSON 형식으로 FastAPI의 `/api/auth/login`에 전송하도록 구현하였습니다.

로그인에 성공하면 서버가 반환한 JWT와 사용자 정보를 React 애플리케이션의 메모리에 저장합니다.

로그인 사용자 이름을 화면에 표시하며, 잘못된 계정 정보에 대해서는 오류를 안내합니다.

JWT는 `localStorage`나 `sessionStorage`에 저장하지 않습니다.

### FE-02. Authorization Bearer 헤더 전송

관련 파일: `src/api.js`

관련 함수: `authorizationHeaders()`

로그인 상태에서 API 요청을 보낼 때 메모리에 저장된 JWT를 Authorization 헤더에 첨부합니다.

```http
Authorization: Bearer <TOKEN>
```

JWT가 없으면 Authorization 헤더를 생성하지 않습니다.

이를 통해 비로그인 상태에서도 공개 게시글 목록과 상세 내용을 조회할 수 있습니다.

### FE-03. 인증 오류 및 로그인 상태 처리

관련 파일: `src/api.js`

관련 함수: `request()`, `clearSession()`

FastAPI에서 HTTP 401을 반환하면 React 메모리에 저장된 JWT와 사용자 정보를 제거하도록 구현하였습니다.

만료된 JWT로 보호 API를 요청하면 서버에서 `TOKEN_EXPIRED`가 반환되며, React 화면이 로그아웃 상태로 변경됩니다.

HTTP 403은 인증된 사용자의 권한 부족을 의미하므로, 401과 구분하여 처리합니다.

게시글 삭제 성공 시 반환되는 HTTP 204는 응답 본문이 없으므로 JSON 파싱 없이 처리합니다.

### FE-04. 작성자별 수정·삭제 버튼 표시

관련 파일: `src/api.js`

관련 함수: `canEdit()`

현재 로그인한 사용자 ID와 게시글 작성자 ID를 비교하여 작성자 본인에게만 수정·삭제 버튼을 표시하도록 구현하였습니다.

다른 사용자의 게시글에서는 수정·삭제 버튼을 숨깁니다.

다만 프론트엔드의 버튼 표시 여부는 사용자 인터페이스 제어이며, 실제 작성자 권한 검사는 FastAPI 백엔드에서 별도로 수행합니다.

### 비로그인 게시글 작성 제한

관련 파일: `src/main.jsx`

관련 함수: `save()`

로그인하지 않은 상태에서 게시글을 등록하려는 경우 다음 안내 메시지를 표시합니다.

"게시글을 작성하려면 먼저 로그인하세요."

비로그인 사용자는 게시글을 읽을 수 있지만, 글을 작성하려면 로그인이 필요합니다.

## 6. 주요 파일 구조

```text
frontend-react/
├── src/
│   ├── api.js
│   └── main.jsx
├── index.html
├── package.json
├── package-lock.json
├── vite.config.js
└── README.md
```

| 파일 | 역할 |
|---|---|
| src/api.js | FastAPI 요청, JWT 저장 및 전송, 인증 오류 처리 |
| src/main.jsx | React 화면 구성, 게시글 및 로그인 상태 표시 |
| index.html | HTML 진입점 및 브라우저 탭 제목 |
| vite.config.js | Vite 개발·미리보기 서버와 API 프록시 설정 |
| package.json | 프로젝트 의존성 및 실행 명령 |
| package-lock.json | 설치할 의존성의 버전 고정 |

## 7. 테스트 계정

과제에서 제공한 테스트 계정을 사용합니다.

| 사용자 | 이메일 | 비밀번호 |
|---|---|---|
| Alice | alice@class.test | Classroom!2026 |
| Bob | bob@class.test | Classroom!2026 |

별도의 회원가입 기능은 이번 과제 범위에 포함하지 않았습니다.

## 8. 주요 API 연동

React는 다음 FastAPI API를 호출합니다.

| Method | API | 기능 |
|---|---|---|
| POST | /api/auth/login | 로그인 및 JWT 발급 |
| GET | /api/me | 로그인 사용자 조회 |
| GET | /api/posts | 게시글 목록 조회 |
| GET | /api/posts/{id} | 게시글 상세 조회 |
| POST | /api/posts | 게시글 작성 |
| PUT | /api/posts/{id} | 게시글 수정 |
| DELETE | /api/posts/{id} | 게시글 삭제 |

공개 조회 API는 JWT 없이 호출할 수 있습니다.

게시글 작성에는 정상 JWT가 필요하며, 수정·삭제에는 JWT 인증과 작성자 권한 검사가 필요합니다.

## 9. JWT 및 화면 동작 검증

Chrome 개발자 도구의 Network와 Console을 이용하여 API 응답을 확인하였습니다.

### 주요 검증 결과

| 테스트 항목 | 실제 결과 |
|---|---|
| Alice 정상 로그인 | HTTP 200, JWT 발급 |
| 정상 JWT로 내 정보 조회 | HTTP 200, Alice 정보 반환 |
| 잘못된 계정 로그인 | 401 INVALID_CREDENTIALS |
| JWT 없는 보호 API 요청 | 401 TOKEN_REQUIRED |
| 변조된 JWT 요청 | 401 INVALID_TOKEN |
| 만료된 JWT 요청 | 401 TOKEN_EXPIRED |
| 다른 사용자의 게시글 수정·삭제 | 403 FORBIDDEN |
| 작성자 ID 위조 | 400 BAD_INPUT |
| 본인 게시글 작성 | 201 Created |
| 본인 게시글 수정 | 200 OK |
| 본인 게시글 삭제 | 204 No Content |
| 새로고침 후 공개 게시글 조회 | 200 OK, 게시글 유지 |
| 새로고침 후 로그인 상태 | 로그아웃 상태 |

전체 T01~T17 시나리오를 최종 빌드 환경인 4173번 포트에서 검증하였습니다.

테스트별 세부 요청과 증거는 프로젝트 루트의 `docs/` 폴더를 참고합니다.

## 10. 로그아웃 및 새로고침 동작

로그아웃 시 React 메모리에 저장된 JWT와 사용자 정보를 제거합니다.

페이지를 새로고침하면 JavaScript 메모리에 보관된 JWT가 초기화되어 로그인 상태가 해제됩니다.

반면 게시글은 백엔드의 SQLite 데이터베이스에 저장되므로 페이지를 새로고침하거나 서버를 재시작해도 유지됩니다.

현재 로그아웃 기능은 브라우저 메모리의 JWT를 제거하는 방식이며, 이미 외부에 복사된 JWT를 서버에서 즉시 무효화하는 기능은 포함하지 않았습니다.

## 11. 서비스 구현 범위 및 제한사항

현재 Mario Secret Guide는 게임 공략을 게시글 형태로 작성하고 공유할 수 있는 웹서비스입니다.

JWT 인증과 작성자 권한 검사를 적용하여 인증된 사용자만 게시글을 변경할 수 있도록 구현하였습니다.

다음 기능은 현재 구현 범위에 포함하지 않았습니다.

- 사용자 회원가입 및 비밀번호 재설정
- Refresh Token 및 서버 측 토큰 철회
- 월드별 공략 검색·분류
- 이미지 첨부
- 클라우드 배포

## 12. 관련 문서

- 전체 프로젝트 실행 안내: `../README.md`
- 구현 보고서: `../docs/report.pdf`
- 테스트 시나리오: `../docs/05_테스트시나리오.md`
- 개발 기록: `../docs/개발기록.md`
- 테스트 증거 목록: `../docs/evidence.md`

본 프로젝트는 웹서비스설계 개인 과제 제출용입니다.

AI 활용 및 수업 자료 참고 내역은 최종 구현 보고서에 기록하였습니다.