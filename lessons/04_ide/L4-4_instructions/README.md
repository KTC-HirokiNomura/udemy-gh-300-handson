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

Chatで新しいチャットを開き、入力欄の下の切り替えを「ローカル」、モードを「Ask」にします。開いているエディターのタブは閉じておきます（エディターで開いているファイルは、入力欄の上に添付されるため）。

1. 入力欄に `#loans` と打ち、候補の一覧から `loans.py`（`app/booklib/loans.py`）を選びます。入力欄に `#file:loans.py` の札が入ります
2. 札のあとに次の文を入れて、送ります

```text
の LoanService に、利用者 ID を受け取って、その利用者が借りている貸出の一覧を返すメソッド loans_of を書いてください。コードだけを示してください。
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

`code .github/copilot-instructions.md` で開き、中身を確かめます。

### 4. 同じ依頼で、答えが変わることを確かめる

作った指示ファイルを添付せずに比べるため、そのタブを閉じてから、新しいチャットを開き（切り替えは「ローカル」、モードは「Ask」）、手順2と同じように `#loans` で `loans.py` を選んで、同じ文を送ります。

たとえば、日本語のdocstring（「引数:」「戻り値:」の節）が付いた答えになります。指示ファイルは、頼むたびに自動で読み込まれます。2つ目の決まり（`ValueError("利用者 ID は正の整数で指定してください")` のような確かめ）は、付く答えと付かない答えがあります。指示は答えの手がかりで、毎回すべての決まりが守られるとは限りません。

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

`code .github/instructions/tests.instructions.md` で開き、中身を確かめます。`applyTo` に書いたパターンに合うファイルを扱うときだけ、この指示が使われます。

### 6. テストを頼んで、効いたことを確かめる

`tests/test_loans.py` を開き、新しいチャットを開いて（切り替えは「ローカル」、モードは「Ask」）、次を送ります。開いたファイルは、入力欄の上に添付として出ます。

```text
LoanService.overdue のテストを tests/test_loans.py に足すコードを示してください。
```

答えの途中の手順に、`tests.instructions.md` を読んだことが出ることがあります。テストの関数に、`"""期限を過ぎた未返却の貸出だけが延滞として返ることを確認する。"""` のような日本語のdocstringが1行付いていれば効いています（いまの `tests/` のテストにはdocstringがありません）。リポジトリ全体の指示も、途中の手順には出ませんが、一緒に使われます。2つの指示が食い違うときに、どちらに沿うかは決まっていないので、決まりは食い違わないように書きます。途中の手順に読んだと出ても、決まりが守られたかは答えそのものを見て確かめます。

## 後片付け

```bash
rm -rf .github && git switch main && git branch -D lesson/l4-4
```

## まとめ

- カスタム指示は、頼むたびに自動で読み込まれ、答えをそろえます
- `.github/copilot-instructions.md` はリポジトリ全体に、`*.instructions.md` は `applyTo` に合うファイルにだけ効きます
- 指示が効いたかは、指示の無いときの答えと比べて確かめます
