T01. 그림1. 비로그인 상태의 게시글 목록 조회 및 인증 헤더 미포함 확인
![alt text](evidence/image.png)

T01. 그림 2. 비로그인 상태의 게시글 상세 조회 성공
 ![alt text](evidence/image-1.png)

그림 3
T02. Alice 계정 로그인 성공 및 HTTP 200 확인
![alt text](evidence/image-2.png)

그림 4
T02. JWT 발급 및 사용자 정보 반환 확인
![alt text](evidence/image-3.png)

그림 5. T03 — 잘못된 비밀번호 입력 시 로그인 거부 (HTTP 401)
![alt text](evidence/image-4.png)

 ![alt text](evidence/image-5.png)

그림 6. T03 — 존재하지 않는 이메일에 대한 로그인 거부 (HTTP 401)
 ![alt text](evidence/image-6.png)
 ![alt text](evidence/image-7.png)

 그림 7. T04 — JWT 없이 내 정보 조회 시 인증 거부 (401 TOKEN_REQUIRED)
 ![alt text](evidence/image-8.png)
 ![alt text](evidence/image-9.png)

그림 8. T04 — JWT 없는 게시글 등록 요청 거부 (401 TOKEN_REQUIRED)
![alt text](evidence/image-11.png)

그림 9. T05 — Alice 토큰을 이용한 게시글 등록 및 작성자 ID 확인
![alt text](evidence/image-12.png)
![alt text](evidence/image-13.png)

그림 10. T05 — JWT를 이용한 Alice 내 정보 조회 및 사용자 정보 확인
![alt text](evidence/image-14.png)
![alt text](evidence/image-15.png)

그림 11. T06 — Alice 본인 게시글 수정 성공 및 작성자 정보 유지 확인 (HTTP 200)
![alt text](evidence/image-16.png)
![alt text](evidence/image-17.png)

그림 12. T06 — Alice 본인 게시글 삭제 성공 (HTTP 204 No Content)
![alt text](evidence/image-18.png)

그림 13. T07 — Bob의 Alice 게시글 수정 요청 거부 및 원본 유지 확인 (HTTP 403)
![alt text](evidence/image-19.png)

그림 14. T08 — Bob의 Alice 게시글 삭제 요청 거부 및 원본 유지 확인 (HTTP 403)
![alt text](evidence/image-20.png)

그림 15. T09 — 변조된 JWT를 이용한 내 정보 조회 거부 (401 INVALID_TOKEN)
![alt text](evidence/image-21.png)

그림 16. T09 — 변조된 JWT를 이용한 게시글 등록 거부 및 데이터 유지 확인
![alt text](evidence/image-22.png)

그림 17. T09 — 변조된 JWT를 이용한 게시글 수정 거부 및 원본 유지 확인 (HTTP 401)
![alt text](evidence/image-23.png)

그림 18. T09 — 변조된 JWT를 이용한 게시글 삭제 거부 및 원본 유지 확인 (HTTP 401)
![alt text](evidence/image-24.png)

그림 19. T10 — JWT 유효 시간 3초 설정 확인
![alt text](evidence/image-25.png)

그림 20. T10 — JWT 만료 시 내 정보 조회 거부 및 자동 로그아웃 확인 (HTTP 401)
![alt text](evidence/image-26.png)

그림 21. T10 — 만료된 JWT를 이용한 게시글 등록 거부 및 데이터 유지 확인 (401 TOKEN_EXPIRED)
![alt text](evidence/image-27.png)

그림 22. T10 — 만료된 JWT를 이용한 게시글 수정 거부 및 원본 유지 확인 (HTTP 401)
![alt text](evidence/image-28.png)

그림 23. T10 — 만료된 JWT를 이용한 게시글 삭제 거부 및 원본 유지 확인 (HTTP 401)
![alt text](evidence/image-29.png)

그림 24. T11 — 로그아웃 후 내 정보 조회 거부 (HTTP 401)
![alt text](evidence/image-30.png)
![alt text](evidence/image-31.png)

그림 25. T12 — Bob의 작성자 ID 위조 요청 거부 및 게시글 미생성 확인 (400 BAD_INPUT)
![alt text](evidence/image-32.png)

그림 25. T12 — Bob의 작성자 ID 위조 요청 거부 및 게시글 미생성 확인 (HTTP 400)
![alt text](evidence/image-33.png)

그림 26. T13 — 빈 제목·공백 본문·길이 초과 입력에 대한 서버 검증 (400 BAD_INPUT)
![alt text](evidence/image-34.png)
![alt text](evidence/image-35.png)
![alt text](evidence/image-36.png)

그림 27. T14 — 존재하지 않는 게시글 및 잘못된 ID 요청에 대한 오류 처리 확인
![alt text](evidence/image-37.png)
![alt text](evidence/image-38.png)
![alt text](evidence/image-39.png)
![alt text](evidence/image-40.png)

그림 28. T15 — 서버 재시작 전 게시글 등록 및 저장 데이터 확인
![alt text](evidence/image-41.png)
![alt text](evidence/image-42.png)

그림 29. T15 — FastAPI 서버 재시작 후 게시글 및 작성자 정보 유지 확인
![alt text](evidence/image-44.png)
![alt text](evidence/image-45.png)
![alt text](evidence/image-46.png)

그림 30. T16 — 페이지 새로고침 후 로그인 상태 해제 및 게시글 유지 확인
![alt text](evidence/image-47.png)

그림 31. T17 — 토큰 없는 게시글 수정·삭제 요청 거부 (401 TOKEN_REQUIRED)
![alt text](evidence/image-48.png)
![alt text](evidence/image-49.png)

그림 32. T17 — Bob 계정의 게시글 등록 성공 및 작성자 정보 확인 (HTTP 201)
![alt text](evidence/image-50.png)
![alt text](evidence/image-51.png)

그림 33. T17 — Bob 본인 게시글 수정 성공 및 작성자 정보 유지 확인 (HTTP 200)
![alt text](evidence/image-52.png)
![alt text](evidence/image-53.png)

그림 34. T17 — Bob 본인 게시글 삭제 성공 및 목록 반영 확인 (HTTP 204)
![alt text](evidence/image-54.png)

그림 35. 추가 검증 — JWT 없이 존재하지 않는 게시글 수정 요청 거부 (401 TOKEN_REQUIRED)
![alt text](evidence/image-55.png)
