

## 手順1: GitHubアカウントの作成と

[GitHubのウェブサイト](https://github.com)にアクセスし、アカウントを作成します。  

### リポジトリの作成(実施不要)
ログイン後、新しいリポジトリを作成します。リポジトリ名や説明を入力し、必要に応じてリポジトリを初期化するオプションを選択します。

## 手順2 Githubのdevelopブランチの作成(実施不要)

リポジトリのページに移動し、「Branches」をクリックします。
「New Branch」をクリックします。   
「Branch name」にブランチ名として「develop」を入力し、「Create branch」ボタンをクリックします。

## 手順3: Visual Studio Codeのインストールと設定
[Microsoft Visual Studio Codeのウェブサイト](https://code.visualstudio.com/Download)から、適切なプラットフォーム向けのインストーラをダウンロードしてインストールします。  
Visual Studio Codeを起動し、左側のサイドバーで「Extensions（拡張機能）」アイコンをクリックします。  
検索バーに「GitHub」と入力し、表示された「GitHub Pull Requests and Issues」拡張機能をインストールします。

## 手順4: リポジトリをクローンする
Visual Studio Codeを起動し、メニューの「View（表示）」から「Command Palette（コマンド パレット）」を選択します。  
コマンドパレットで「Git: Clone（Git: クローン）」と入力し、Enterキーを押します。  
リポジトリのURLを入力し、Enterキーを押します。  
リポジトリのクローン先のディレクトリを選択し、Enterキーを押します。

- リポジトリURL
https://github.com/hata-dev/cause_and_effect.git

## 手順5: Gitの設定

コマンドラインまたはターミナルを開きます。
下記のコマンドを使用して、GitHubでの表示名を設定します。

```
git config --global user.name "Your GitHub Username"
```

下記のコマンドを使用して、GitHubでのメールアドレスを設定します。

```
git config --global user.email "your-email@example.com"
```

# 手順6: Visual Studio Codeの設定

Visual Studio Codeを起動し、メニューの「表示」→「コマンドパレット」→「setting.json」と入力し、→「基本設定ユーザー設定を開く」を選択します。  
settings.jsonファイルが開かれたら、下記のコードを追加します。

```json
{
    "git.path": "git"
}
```
"git.path"の値を、自分の環境に合わせて正しいGitのパスに変更します。通常はデフォルトのパス「git」で問題ありませんが、独自の設定がある場合はそれに応じて変更してください。

## 手順7: VSCodeでdevelopブランチを作成する

```
git checkout -b develop
```

以下コマンドでdevelopブランチが追加されていることを確認する
```
git branch
```


## 手順6: リポジトリの変更を管理する
Visual Studio Codeの左側のサイドバーで「ソースの管理」をクリックします。  
ソース コントロール パネルが表示されたら、変更したいファイルを選択します。  
選択したファイルに右クリックし、コンテキストメニューから「変更をステージング」を選択します。（もしくは + マークをクリック）  
コミット メッセージを入力し、ソース コントロール パネルの上部のチェックマークアイコンをクリックします。

## 手順7: 変更をリモートリポジトリにプッシュする
「ソースの管理」の右上にある三点リーダーアイコンをクリックし、コンテキストメニューから「Push（プッシュ）」を選択します。  
プッシュ先のリモートリポジトリを選択します。

