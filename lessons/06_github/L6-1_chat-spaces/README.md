# L6-1 実践: github.comのCopilot ChatとSpaces

github.comのCopilot Chatで、教材リポジトリについて質問します。次に、Copilot Spacesで資料を集めた場所（Space）を作り、同じ質問をします。Spaceの中の答えが、集めた資料に基づくことを確かめます。

## 前提

- L0-2 を終えて、教材リポジトリをForkしていること
- このレッスンはgithub.comだけで進めます。Codespacesは使いません
- Spacesは、Copilot Freeを含むすべてのプランで使えます。Spaceの中の質問はChatと同じ扱いで、AIクレジットを使います

## 進め方

| 手順 | やること |
|---|---|
| 1 | github.comのCopilotを開く |
| 2 | リポジトリを添付して質問する |
| 3 | Spaceを作る |
| 4 | Spaceに資料を足す |
| 5 | Spaceの中で、同じ質問をする |

### 1. github.comのCopilotを開く

ブラウザーで、次のページを開きます。

```text
https://github.com/copilot
```

### 2. リポジトリを添付して質問する

入力欄の下の「All repositories」を押します。`udemy-gh-300-handson` を検索して、自分のForkを選びます。モードは「Ask」のままにします。

次を送ります。

```text
booklibの、本の貸出の決まりを教えてください。利用者1人が同時に何冊まで借りられますか？
```

Copilotが「リポジトリの中を調べてお伝えします」のように答えて止まったら、続けて「はい、調べてください。」と送ります。

冊数の上限は、リポジトリのどこにも書いていません。答えが「上限は無い」「見つからない」のようになることを確かめます。たとえば、根拠として `app/booklib/loans.py` や `docs/design.md` が挙がります。

### 3. Spaceを作る

次のページを開き、「Create space」を押します。

```text
https://github.com/copilot/spaces
```

| 項目 | 入れるもの |
|---|---|
| Space name | `booklib design` |
| Owner | 自分のアカウント |

名前には、半角の英数字・空白・記号だけが使えます。ダイアログの「Create space」を押すと、Spaceができます。個人のSpaceは、自分だけが見られます（Private）。

### 4. Spaceに資料を足す

**Instructions**（Spaceの中の答え方の指示）の欄を押し、次を入れて「Save」を押します。

```text
日本語で答えてください。答えの根拠にした資料の名前を書いてください。
```

**Sources**（資料）を2つ足します。

1. 「Add sources」→「Add files from repository」を選び、自分のForkを選びます。`docs` を開いて `design.md` に印を付け、「Add」を押します
2. 「Add sources」→「Add text content」を選び、次のメモを入れて「Add」を押します

| 項目 | 入れるもの |
|---|---|
| Name | `貸出の上限（決まったこと）` |
| Content | `利用者1人が同時に借りられるのは5冊まで。次の版で loans.py に入れる。` |

メモの中身は、リポジトリにはまだ無い、チームで決まったことです。

「Add sources」のメニューには、リポジトリ全体を足す「Add repository」や、ファイルのアップロード（Upload a file）もあります。

### 5. Spaceの中で、同じ質問をする

Spaceの画面の入力欄（How can I help you?）に、手順2と同じ質問を送ります。

```text
booklibの、本の貸出の決まりを教えてください。利用者1人が同時に何冊まで借りられますか？
```

答えに「5冊まで」が出ることを確かめます。たとえば、根拠として `docs/design.md` とメモが挙がります。手順2では答えられなかった上限に、Spaceの資料から答えています。

この会話は、Spaceの「Conversations」のタブに残ります。

## 後片付け

- Spaceは、ほかのレッスンでは使いません。残しておいても構いません
- Spaceに足したファイルは、リポジトリのmainの最新を参照します。`docs/design.md` を直すと、Spaceの答えも変わります

## まとめ

- github.comのCopilot Chatでは、リポジトリを添付して質問できます
- Spaceには、リポジトリのファイル・メモなどの資料と、答え方の指示を集められます
- Spaceの中の質問には、集めた資料に基づいて答えます
