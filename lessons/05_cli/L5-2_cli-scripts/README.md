# L5-2 実践: CLIでスクリプトを作り、ファイルを扱う

Copilot CLIに、蔵書のCSVを集計するスクリプトを作ってもらいます。非対話のモードで、承認の要る操作は、許可したものだけが動くことを確かめます。最後に、対話のモードでファイル名の一括変更を頼み、承認の前に何をするかを読みます。

## 前提

- L5-1 を終えて、Copilot CLIが入っていること

## 進め方

| 手順 | やること |
|---|---|
| 1 | レッスン用のブランチを作る |
| 2 | 許可なしで、スクリプトの作成を頼む |
| 3 | 許可を付けて、もう一度頼む |
| 4 | 作られたスクリプトを読み、実行する |
| 5 | ファイル名の一括変更を、対話のモードで頼む |
| 6 | gitの差分で確かめ、元に戻す |

### 1. レッスン用のブランチを作る

```bash
git switch main && git switch -c lesson/l5-2
```

### 2. 許可なしで、スクリプトの作成を頼む

```bash
copilot -p "data/books.csv を読んで、著者ごとの冊数を多い順に表示する Python スクリプトを count_authors.py に作り、実行して上位3件を見せてください。"
```

CSVを読むところまでは進みます（CLIが読むだけと判断したコマンドは、承認なしで動きます）。ところが、ファイルを作る・`python` を実行するところで、次のように断られます。

```text
Permission denied because no interactive user response was available.
```

非対話のモードでは、承認する人がいないからです。

### 3. 許可を付けて、もう一度頼む

```bash
copilot -p "data/books.csv を読んで、著者ごとの冊数を多い順に表示する Python スクリプトを count_authors.py に作り、実行して上位3件を見せてください。" --allow-tool 'write' --allow-tool 'shell(python3)'
```

- `--allow-tool 'write'`: ファイルを書くことを許します
- `--allow-tool 'shell(python3)'`: `python3` のコマンドの実行を許します（今回は `python3 count_authors.py` が動きました）

`count_authors.py` が作られ、上位3件が出ます。`python` で実行しようとして断られ、`python3` でやり直すことがあります。承認の要る操作は「許したものだけが動く」ことが分かります。

> `--allow-all-tools` を付けると、すべてのツールを確かめずに許します。何をするか分からない依頼には使いません。

### 4. 作られたスクリプトを読み、実行する

```bash
cat count_authors.py
python3 count_authors.py | head -3
```

読んで、CSVの列の扱いや並べ方が頼んだとおりかを確かめます。

### 5. ファイル名の一括変更を、対話のモードで頼む

```bash
copilot
```

起動したら、次を送ります。

```text
data/notes のファイル名を、note-01.txt のように小文字・2桁の番号・拡張子 .txt にそろえてください。
```

名前を変えるコマンド（たとえば `mv "Note 1.txt" note-01.txt && …` や `git mv "Note 1.txt" note-01.txt && …`）を実行する前に、「Do you want to run this command?」と聞かれます。「どのファイルを、どの名前に変えるのか」を読んでから選びます。先にファイルの一覧を読むコマンド（`ls` など）が動くこともあります。

| 選択肢 | 意味 |
|---|---|
| 1. Yes | 今回だけ実行する |
| 2. Yes, and don't ask again for … | 同じコマンド（今回なら `mv`）は、このリポジトリでは次から聞かずに実行する |
| 3. No, and tell Copilot what to do differently | 実行せずに、やり方を言い直す |

ここでは「1. Yes」を選びます。終わったら `/exit` で終了します。

### 6. gitの差分で確かめ、元に戻す

```bash
git status --short
```

`mv` で名前を変えた場合は、元の名前のファイルが消えた印（D）と、新しい名前のファイル（??）が並びます。`git mv` で変えた場合は、`R  "data/notes/Note 1.txt" -> data/notes/note-01.txt` のように、名前の変更（R）が並びます。どちらでも、`count_authors.py` は新しいファイル（??）です。確かめたら、元に戻します。

```bash
git reset -q && git checkout -- data/notes && git clean -fdq data/notes && rm -f count_authors.py
```

変更が無く、元の5つの名前に戻ったことを確かめます。

```bash
git status --short; ls data/notes
```

## 後片付け

```bash
git switch main && git branch -D lesson/l5-2
```

## まとめ

- 非対話のモードでは、承認の要る操作のうち、許可していないものは断られます
- `--allow-tool` で、許す操作を決められます
- 対話のモードでは、承認の前に、何をするかを読みます
