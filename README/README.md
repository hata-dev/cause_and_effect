# case_and_effect

## Visual studio code インストール

[インストーラ置き場](https://code.visualstudio.com/)

- [https://www.javadrive.jp/vscode/install/index4.html](vscode 日本語)
- pyhonインストール
- LiveShareインストール
- Japanese Language Pack for Visual Studio Codeインストール
## github for windows インストール

[gitインストーラ置き場](https://git-scm.com/download/win)  
[インストール手順](https://qiita.com/HyunwookPark/items/d399f6959fc922a15ee1)

- choosing the defauklt editor used by Gitは
   - use visual studio code as git's default editor
- adjusting the name of the initial branch in new repositories
  - Let git decide
- adjusting your PATH enviroment
  - Git from the command line and also from 3rd-party software
- Choosing HTTPS transport backend
  - Use the OpenSSL library

あとはデフォルト

## リポジトリ作成から
https://web-engineer-wiki.com/git/init-push/

- ローカルPCから
   - リポジトリ利用のフォルダを作成
   - フォルダに移動(cd フォルダ名) 
   - git init 
   - git config -e
```
[user]
	name=ユーザー名
	email=メールアドレス
```
   - git config -lで追加されているか確認
   - 右のソースからBranchの発行
   - git remote add origin https://github.com/hata-dev/case_and_effect.git
   - git remote -v で紐づき確認
   - git pull origin develop
   - git pull <リモート名> <ブランチ名>
   
## テスト用追加テキスト

- test

## ブランチ

 - git status
 - git add .
 - git commit -m "prefix 変更内容"
 - git push origin(リモートブランチ) develop(今いるブランチ)

## ブランチ削除

- git branch -d <branchname>

## コミット規約

| prefix | 意味 |
| -- | -- |
| fix | バグ修正 |
| add | 機能(またはファイル)追加 |
| update | バグではない細かなコード変更 |
| change | 仕様変更によるコード変更 |
| delete  | 機能(またはファイル)削除 |
| rename | ファイル名変更 |
| move | ファイル移動 |
| docs | ドキュメント修正 |
| test | テストで機能の追加・修正 |



