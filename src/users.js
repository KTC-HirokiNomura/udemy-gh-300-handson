// サンプルのユーザー一覧（実際のサービスでは、データベースから読み込みます）
const users = [
  { id: 1, email: "alice@example.com", passwordHash: "sample-hash-1" },
  { id: 2, email: "bob@example.com", passwordHash: "sample-hash-2" },
];

/**
 * メールアドレスでユーザーを探す
 * @param {string} email
 * @returns {object | undefined}
 */
function findUserByEmail(email) {
  return users.find((user) => user.email === email);
}

module.exports = { findUserByEmail };
