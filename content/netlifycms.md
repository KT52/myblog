---
Title: netlifycms
Date: '2019-05-16'
Category: Pelican
Tags: 'netlify,pelican'
Slug: netlifycms
---
## はじめに

- - -

Netlify CMSは静的サイトジェネレーターにWordpressのような管理画面を追加するオープンソースのコンテンツ管理システムです。\
多分Wordpressのデータベースの代わりにGitHubやGitLabを利用して管理しているのでしょう。  

このブログは静的サイトジェネレーターのPelicanを利用していますがここにNetlify CMSを追加してみようと思います。

管理画面を表示するまでにする事は少なく、  

1. GitHub認証
2. Netlifyの設定
3. content内にadminディレクトリを作って2つのファイルを置く
4. pelicanconf.pyの編集
5. GitHubにpush

これだけです。

## GitHub認証

- - -

最初にGitHubの右上にある自分のアイコンから`setting→Developer settings
OAth Apps`を選択して`Register a new application`をクリック。  

すると下記の画面になるのでこんな感じに入力していきます。    

![gitoauth](/../../../images/gitoauth.jpg)

Application nameは適当にHomepage URLはブログのURL、`Authorization call back URL`は`https://api.netlify.com/auth/done`と入力してRegister applicationをクリック。  

するとClient IDと Client Secretが発行されるのでページはそのままでNetlifyのsite settingsに移動します。  

## Netlifyの設定

- - -

Netlifyのsite settingsの一番下にある`Access control`→`OAuth`→`Install provider`をクリック。すると下記の画面になるので先程のClient IDと Client Secretを入力して`install`を押します。\
これでNetlifyの設定は終了です。  

![installprovider](/../../../images/installprovider.jpg)
