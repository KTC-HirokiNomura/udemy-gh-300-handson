const { findUserByEmail } = require("./users");

// メールアドレスとパスワードで、ログインできるかを確かめる
function login(email, password) {
  const user = findUserByEmail(email);
  if (!user) {
    return false;
  }
  return user.passwordHash === hashPassword(password);
}

// パスワードをハッシュにする（サンプル）
function hashPassword(password) {
  return `sample-hash-${password}`;
}

module.exports = { login };
