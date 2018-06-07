Title: Netlifyに静的コンテンツをホスティングする
Date: 2018-06-07
Category: Pelican
Tags: Netlify,Python,Pelican
Slug:　pelicannetlify

## Netlifyとは？
Netlifyとは静的コンテンツベースのウェブサイトに特化したWEBホスティングサービスです。  PelicanやHexoなどの静的サイトジェネレーターでウェブサイトを公開するのに便利なサービスです。他にはGitHub Pagesなどがありますね。  
GitHubやGitLabと連携してリポジトリからデプロイしたり、連携しなくてもhtmlファイルなどが入ったフォルダをzipで固めて直接ドラッグアンドドロップでアップロードするだけでサイトを公開できます。  

## Netlifyの特長
- ビルドコマンドが実行可能  
静的サイトジェネレーターでhtmlをジェネレイトするのをNetlifyが勝手にやってくれるので、記事を書いてpushするだけでい
い。
- http/2
- 独自ドメインが使用可能
- 無料のssl/https
- CDN  
cloudflareなどのサービスを使わずにサイトを高速化することができる。
- フォームの設置

他にもいろいろな機能があります。詳しくは→[Docs](https://www.netlify.com/docs/)参照。  
GitHub Pagesとの比較は[コチラ](https://www.netlify.com/github-pages-vs-netlify/)を参照してください。  
デメリットは日本語未対応なことでしょうか。

## Freeプラン

Freeプランでどれくらい利用できるのかというと、

- ネットワーク転送量 100GB/月
- ストレージ100GB
- APIリクエスト500リクエスト/分, 3デプロイ/分  

ストレージ100GBなんてほぼ制限がないと言っているようなもの。

## サインイン

ログインはGitHub、GitLab、Bitbucket、Emailから可能

## Gitと連携

使用するリポジトリを選ぶ。

## Deployセッティング

デプロイセッティングとビルドセッティングを登録したら`Deploy site`をクリックして完了。  
ビルドセッティングは後で設定可。

## コンソール画面

`Deploy site`をクリックしたらこんな風にコンソール画面が表示されます。"happy-hugle-5cae8e.netlify.com"というURLが割り当てられました。  
<a href="../../../images/netlify_overview2.jpg" data-toggle="lightbox" data-max-width="100%"><img src="../../../images/netlify_overview2.jpg"  class="img-thumbnail" alt="overview" width="300" ></a>  
