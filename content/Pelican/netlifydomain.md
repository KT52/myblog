Title: Netlifyで独自ドメインを設定する
Date: 2018-07-01
Category: Pelican
Tags: Netlify,Python,Pelican
Slug: netlifydomain

Netlifyで独自ドメインを設定してみた

### ドメインを取得する
---

![Xdomain](../../../images/xdomaintop.jpg)  <br>

他サイトのドメインはムームードメインを利用しているが、今回はドメインを[Xdomain（エックスドメイン）](https://www.xdomain.ne.jp/){:target="_blank"}で取得することにしました。<br><br>

- エックスドメインの良いところ
	- 更新料が安い  
	お名前ドットコムやムームードメインの方が、キャンペーンで.comや.netなどを安く購入できるが、2年目以降の更新料がエックスドメインに比べると高い。  
	- 無料のレンタルサーバーを使用できる  
	ドメインを取得しなくても利用できる無料のレンタルサーバーの機能を少し拡張して使える。  

`ドメインの検索`→`会員登録`→`お支払い情報の入力`→`内容の確認・規約への同意`→`申込み完了`と進んで10～20分で簡単にドメインを取得できます。（クレカ払いの場合）

### Netlifyにカスタムドメインを登録
---
Domain Setting→Add custom domainと進んで取得したドメインを入力`(www).xxx.com` を入力して`Verify`をクリック  
Netlifyはwww付きのドメインをプライマリードメインとして推奨しているようです。なのでwww付きで登録しました。

### DNS設定
---
`Verify`をクリックした後はこんな画面になるので`Check DNS Configuration`をクリック。

![dns](../../../images/checkdns.jpg)<br>

すると、CNAMEをエックスドメインで編集するかNetlify DNSを使うか表示されるので`Set up Netlify DNS~~`をクリック。  
ベストパフォーマンスを得るにはNetlify DNSを必ず使ってねと書いてありますね。ALIASやCNAMEも気にしないでね、とも。<br>

![dnsconf](../../../images/dnsconf3.jpg)

<br>
wwwなしのドメインでAレコードをドメインプロバイダーのDNSレコードに記述するやり方だとNetlifyの強力なCDNを利用することができないので注意。
<br>

![dns](../../../images/dnsconf1.jpg)

「Netlify 独自ドメイン」でググるとAレコードを記述する方法ばかりがヒットしたので最初はその方法で設定していましたが、Aレコードを使用するとNetlifyの恩恵が得られなさそうなのでwwwの使用に抵抗がなければwwwありでNetlify DNSを利用しましょう。<br>

### ネームサーバーの変更
---
`Set up Netlify DNS~~`をクリックして進めていくとDNSレコードをNetlifyが勝手に設定してくれて、更に進むと4つのネームサーバーが表示されるのでコピーしてエックスドメインの「ネームサーバーの確認・変更」から４つのネームサーバーをペーストする。


![nameserver](../../../images/nameservers.jpg)   

DNSが浸透すると独自ドメインでアクセスできるようになる。


![domainset](../../../images/domainset.jpg)


### Let’s Encryptの証明書を取得
---
カスタムドメインを設定したらHTTPSの`Verify DNS configuration`→`Let's Encypt certificate`をクリック。しばらくすると証明書を取得できます。  
下の画面のような表示になれば成功。    


![https](../../../images/https.jpg)


### httpsを強制
---
Force HTTPSをクリックしてhttpでのアクセスをhttpsにリダイレクトさせる。


### 感想
---
ドメインを設定するのは簡単なのですが、改めてドキュメンテーションを読んでもDNS関連は全然知識がないし、英語なので誤読していないか心配。時間があるときに辞書片手にしっかり読まないといけないかなあ～と思ったりしました。