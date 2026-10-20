# L6-2 実践: PRの要約とコード レビュー

わざと決まりに合わない変更を入れてPRを作ります。CopilotにPRの要約を書いてもらい、コード レビューを頼みます。レビューが、ブランチに置いたカスタム指示の決まりを使って指摘することを確かめます。

## 前提

- L0-2 を終えて、Codespacesを開いていること
- PRの要約とコード レビューは、有料プランの機能です。AIクレジットを使います

## 進め方

| 手順 | やること |
|---|---|
| 1 | ブランチを作り、決まりと変更を入れる |
| 2 | pushしてPRを作る |
| 3 | PRの要約を作る |
| 4 | Copilotにレビューを頼む |
| 5 | 指摘を読み、受け入れるか決める |
| 6 | PRを閉じる |

### 1. ブランチを作り、決まりと変更を入れる

```bash
git switch main && git switch -c lesson/l6-2
mkdir -p .github
cat > .github/copilot-instructions.md <<'EOF'
# booklib のコードの決まり

- 関数の引数と戻り値には、型ヒントを付ける
- 関数には、日本語の docstring を書く
EOF
cat >> app/booklib/report.py <<'EOF'


def format_titles(books):
    return "、".join(book.title for book in books)
EOF
```

`format_titles` には、型ヒントもdocstringもありません。決まりに合わない変更です。

### 2. pushしてPRを作る

```bash
git add -A && git commit -m "Add format_titles to report" && git push -u origin lesson/l6-2
```

1. Forkしたリポジトリをgithub.comで開くと、「Compare & pull request」が出ます。押します
2. 上の「base repository」を押し、`<自分のアカウント>/udemy-gh-300-handson` を選びます。「base」は `main` にします
3. 「Create pull request」を押します

> 「base repository」の最初の値は、元の教材リポジトリのことがあります。そのまま作ると、PRが元の教材リポジトリに届きます。必ず自分のForkを選んでください。

### 3. PRの要約を作る

1. PRの説明（最初のコメント）の右上の「…」 → 「Edit」を押します
2. 編集欄のツールバーにあるCopilotのアイコンを押し、「Summary」を選びます
3. 変更の要約が説明欄に入ります。英語で出ることがあります。読んで、合っていれば「Update comment」で保存します

### 4. Copilotにレビューを頼む

右側の「Reviewers」にある「Copilot」の「Request」を押します。

「Copilot started reviewing」と出て、1〜2分でレビューが届きます。

### 5. 指摘を読み、受け入れるか決める

たとえば、次のような指摘が付きます。

- 「format_titlesに引数・戻り値の型ヒントと日本語のdocstringがなく、このPRで追加する規約を満たしていません」

レビューは、PRのブランチ（変更のある側）に置いた `.github/copilot-instructions.md` の決まりを読んで指摘します。指摘が正しければ、コードを直してpushします。合わない指摘は、理由を書いて解決済みにします。

### 6. PRを閉じる

このPRはマージせずに、PRの下の「Close pull request」で閉じます。

```bash
git switch main && git branch -D lesson/l6-2 && git push origin --delete lesson/l6-2
```

## まとめ

- PRの要約は、変更の中身から説明を書いてくれます。保存する前に読みます
- Copilotのコード レビューは、PRのブランチのカスタム指示を、レビューの決まりとして使います
- 指摘は、受け入れるか、理由を付けて見送るかを、自分で決めます
