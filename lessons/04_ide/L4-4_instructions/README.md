# L4-4 実践: カスタム指示で答えをそろえる

同じ依頼を、カスタム指示の無いときと、あるときで比べます。リポジトリ全体の指示（`.github/copilot-instructions.md`）と、テストのファイルにだけ効く指示（`*.instructions.md`）を作ります。

## 前提

- L0-2 を終えて、Codespacesを開いていること

## 進め方

| 手順 | やること |
|---|---|
| 1 | レッスン用のブランチを作る |
| 2 | 指示なしで頼み、答えを残す |
| 3 | `copilot-instructions.md` を作る |
| 4 | 同じ依頼で、答えが変わることを確かめる |
| 5 | テスト用の `*.instructions.md` を作る |
| 6 | テストを頼んで、効いたことを確かめる |

### 1. レッスン用のブランチを作る

```bash
git switch main && git switch -c lesson/l4-4
```

### 2. 指示なしで頼み、答えを残す

Chatで新しいチャットを開き、切り替えを「ローカル」、モードを「Ask」にして、次を送ります。

```text
#file:app/booklib/loans.py の LoanService に、利用者 ID を受け取って、その利用者が借りている貸出の一覧を返すメソッド loans_of を書いてください。コードだけを示してください。
```

たとえば、docstringの無い2行のメソッドが返ります。答えを覚えておきます。

### 3. `copilot-instructions.md` を作る

```bash
mkdir -p .github
cat > .github/copilot-instructions.md <<'EOF'
# booklib のコードの決まり

- 関数とメソッドには、日本語の docstring を書く。1行目に要約、続けて「引数:」と「戻り値:」の節を書く
- 引数の値が正しくないときは、日本語のメッセージで ValueError を出す
EOF
```

### 4. 同じ依頼で、答えが変わることを確かめる

新しいチャットを開き（切り替えは「ローカル」、モードは「Ask」）、手順2と同じ文を送ります。

日本語のdocstring（「引数:」「戻り値:」の節）と、`ValueError("利用者 ID は正の整数で指定してください")` のような確かめが付いた答えになります。指示ファイルは、頼むたびに自動で読み込まれます。

### 5. テスト用の `*.instructions.md` を作る

```bash
mkdir -p .github/instructions
cat > .github/instructions/tests.instructions.md <<'EOF'
---
applyTo: "tests/**"
---

- テストの関数には、何を確かめるかを日本語の docstring で1行で書く
EOF
```

`applyTo` に書いたパターンに合うファイルを扱うときだけ、この指示が使われます。

### 6. テストを頼んで、効いたことを確かめる

`tests/test_loans.py` を開き、新しいチャットで次を送ります。

```text
LoanService.overdue のテストを tests/test_loans.py に足すコードを示してください。
```

テストの関数に、`"""期限を過ぎた未返却の貸出だけが延滞として返ることを確認する。"""` のような日本語のdocstringが1行付いていれば効いています（いまの `tests/` のテストにはdocstringがありません）。

## 後片付け

```bash
rm -rf .github && git switch main && git branch -D lesson/l4-4
```

## まとめ

- カスタム指示は、頼むたびに自動で読み込まれ、答えをそろえます
- `.github/copilot-instructions.md` はリポジトリ全体に、`*.instructions.md` は `applyTo` に合うファイルにだけ効きます
- 指示が効いたかは、指示の無いときの答えと比べて確かめます
