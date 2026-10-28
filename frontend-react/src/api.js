// TODO FE-01~04: 공통 API 명세와 구현 체크리스트를 보고 완성하세요.
let session = { accessToken: "", user: null };
export const getSession = () => session;
export function clearSession() {
  session = { accessToken: "", user: null };
}

function authorizationHeaders() {
  if (!session.accessToken) {
    return {};
  }

  return {
    Authorization: `Bearer ${session.accessToken}`,
  };
}

export async function request(path, options = {}) {
  const response = await fetch(`/api${path}`, {
    ...options,
    headers: {
      "Content-Type": "application/json",
      ...authorizationHeaders(),
      ...options.headers,
    },
  });
  const data = response.status === 204 ? null : await response.json();
  if (!response.ok) {
    // 인증 실패 시 로그인 상태 제거
    if (response.status === 401) {
      clearSession();
    }

    // 오류 내용을 화면에 전달
    const error = new Error(
      data?.message || data?.code || `HTTP ${response.status}`,
    );

    error.status = response.status;
    error.code = data?.code;
    throw error;
  }
  return data;
}

export async function login(email, password) {
  // 1. FastAPI 서버에 로그인 요청
  const data = await request("/auth/login", {
    method: "POST",
    body: JSON.stringify({ email, password }),
  });

  // 2. 서버가 반환한 JWT와 사용자 정보 저장
  session = {
    accessToken: data.accessToken,
    user: data.user,
  };

  // 3. 로그인한 사용자 정보 반환
  return data.user;
}

export function canEdit(post) {
  return Boolean(
    session.user &&
    post &&
    session.user.id === post.authorId
  );
}
export const api = {
  list: () => request("/posts"),
  detail: (id) => request(`/posts/${id}`),
  create: (input) =>
    request("/posts", { method: "POST", body: JSON.stringify(input) }),
  update: (id, input) =>
    request(`/posts/${id}`, { method: "PUT", body: JSON.stringify(input) }),
  remove: (id) => request(`/posts/${id}`, { method: "DELETE" }),
  me: () => request("/me"),
};
