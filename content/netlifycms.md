---
Title: netlifycms
Date: '2019-05-16'
Category: Pelican
Tags: 'netlify,pelican'
slug: netlifycms
---
## はじめに

- - -

[Netlify CMS](https://www.netlifycms.org/){:target="_blank"}は静的サイトジェネレーターにWordpressのような管理画面を追加するオープンソースのコンテンツ管理システムです。\
Wordpressのデータベースの代わりにGitHubやGitLabのリポジトリを利用して管理しているようです。  

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

Netlifyのsite settingsの一番下にある`Access control`→`OAuth`→`Install provider`をクリック。すると下記の画面になるので先程のClient IDと Client Secretを入力して`install`を押します。  
これでNetlifyの設定は終了です。  

![installprovider](/../../../images/installprovider.jpg)

## Netlify CMS用のファイルを作成
---

一旦ブラウザから離れてローカルのcontentディレクトリにadminディレクトリを作成して`index.html`、`config.yml`を作成します。

### index.htmlの中身

```html

<!doctype html>
<html>
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Content Manager</title>
</head>
<body>
  <!-- Include the script that builds the page and powers Netlify CMS -->
  <script src="https://unpkg.com/netlify-cms@^2.0.0/dist/netlify-cms.js"></script>
</body>
</html>

```

公式サイトからのコピペでOKです。

### config.ymlの中身

```python

backend:
  name: github
  repo: Squigly77/myblog
  branch: master

publish_mode: editorial_workflow

media_folder: "content/images"
public_folder: "/{static}/images"

collections:
  - label: "Blog"
    name: "blog"
    folder: "content"
    create: true
    slug: "{{fields.slug}}"
    identifier_field: Title
    fields:
      - {label: "Title", name: "Title", widget: "string"}
      - {label: "Publish Date", name: "Date", widget: "date",format: "YYYY-MM-DD"}
      - {label: "Modified", name: "Modified", widget: "string", required: false}
      - {label: "Category", name: "Category", widget: "string"}
      - {label: "Tags", name: "Tags", widget: "string"}
      - {label: "Slug", name: "slug", widget: "string"}
      - {label: "Related", name: "related_post", widget: "string", required: false}
      - {label: "Body", name: "body", widget: "markdown"}

```

#### backend
GitHubを使用している場合はrepoに使用するリポジトリとbranchを指定。

#### publish_mode: editorial_workflow
editorial_workflowというモードを設定することで下書き保存が可能になります。  
これがないと記事を作成してセーブすると即座に公開されてしまう。

#### media/public_folder

- media_folder  
画像ファイル置き場の場所。  

- public_folder  
記事をアップロードした後に実際にアクセスされる画像ファイルのパス。  
記事を書いてるとき画像のパスは、({static}/images/xxx.jpg)とか(../../../images/xxx.jpg)こんな感じに書きますよね。その部分をpublic_folderに指定します。

#### collections


