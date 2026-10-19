# GH-300 GitHub Copilot認定試験対策講座 ハンズオン教材

Udemyの講座「GH-300 GitHub Copilot認定試験対策講座」の実践（ハンズオン）で使う教材です。
このリポジトリをForkして、GitHub Codespacesで開いて使います。

## はじめに

最初に [L0-2 環境を準備する](lessons/00_intro/L0-2_setup/README.md)を進めてください。ForkとCodespacesの作り方、後片付けの方法を説明しています。

## 題材のアプリ `booklib`

町の小さな図書室で使う、蔵書と貸出の管理ライブラリ（Python）です。すべての実践で、このアプリを使います。

| 場所 | 中身 |
|---|---|
| `app/booklib/` | アプリの本体（蔵書・検索・貸出・日付・集計・一覧の整形） |
| `tests/` | テスト（pytest）。mainのままで全部通ります |
| `legacy/old_report.py` | 古い書き方のスクリプト（L7-1 で使います） |
| `data/books.csv` | 蔵書の一覧（50冊。書名・著者は架空です） |
| `data/notes/` | 名前の付け方がばらばらなメモ（L5-2 で使います） |
| `docs/design.md` | 設計メモ（L6-1 で使います） |
| `lessons/` | レッスンごとの手順（README）と、確かめるためのファイル |
| `src/users.js`・`src/login.js` | 第2章・第3章の座学の画面で使ったJavaScriptのサンプル（実践では使いません） |

アプリには、レッスンで直すための弱いところを、わざと残してあります。

## レッスンの進め方

- 各レッスンのREADMEの手順を、番号の順に進めます。コマンドはコピーして貼り付けられます
- **レッスンごとにmainから新しいブランチを作ります。** 前のレッスンの結果を使わないので、どのレッスンからでも始められます
- Copilotの答えは毎回変わります。READMEの答えの例と違っても、手順の「確かめる」で結果を判断してください

## AIクレジットと後片付け

- Chat・エージェント・CLI・クラウド エージェント・コード レビューは、AIクレジットを使います（インラインの提案は、有料プランでは数えません）。使用量はgithub.comの「Settings → Copilot」で見られます
- Codespacesは、使っている時間と保存の容量で、無料の枠を使います。終わったら止めてください（手順はL0-2）

## レッスンの一覧

| 章 | レッスン |
|---|---|
| はじめに | [L0-2 環境を準備する](lessons/00_intro/L0-2_setup/README.md) |
| プロンプト | [L3-2 ゼロショットとフューショットを比べる](lessons/03_prompt/L3-2_zero-few-shot/README.md) |
| IDEの機能 | [L4-1 インラインの提案](lessons/04_ide/L4-1_inline/README.md)・[L4-2 Chatの使い方](lessons/04_ide/L4-2_chat/README.md)・[L4-3 エージェント モード](lessons/04_ide/L4-3_agent/README.md)・[L4-4 カスタム指示](lessons/04_ide/L4-4_instructions/README.md) |
| Copilot CLI | [L5-1 CLIの基本](lessons/05_cli/L5-1_cli-basics/README.md)・[L5-2 CLIでスクリプトとファイル](lessons/05_cli/L5-2_cli-scripts/README.md) |
| github.comの機能 | [L6-2 PRの要約とコード レビュー](lessons/06_github/L6-2_pr-review/README.md)・[L6-3 クラウド エージェント](lessons/06_github/L6-3_cloud-agent/README.md) |
| プライバシーと管理 | [L8-1 フィルターとエディターの設定](lessons/08_privacy/L8-1_filters-settings/README.md) |

ほかのレッスン（L4-5 MCP・L6-1 ChatとSpaces・第7章）の手順は、準備ができたものから追加します。
