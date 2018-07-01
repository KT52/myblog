Title: Netlifyで独自ドメインを設定する
Date: 2018-07-01
Category: Pelican
Tags: Netlify,Python,Pelican
Slug: netlifydomain

Netlifyで独自ドメインを設定してみた

## ドメインを取得する
---

![Xdomain](../../../images/xdomaintop.jpg)  <br>

他サイトのドメインはムームードメインを利用しているが、今回はドメインを[Xdomain（エックスドメイン）](https|//www.xdomain.ne.jp/)で取得することにしました。<br><br>

- エックスドメインの良いところ
	- 更新料が安い  
	お名前ドットコムやムームードメインの方が、キャンペーンで.comや.netなどを安く購入できるが、2年目以降の更新料がエックスドメインに比べると高い。  
	- 無料のレンタルサーバーを使用できる  
	ドメインを取得しなくても利用できる無料のレンタルサーバーの機能を少し拡張して使える。  

`ドメインの検索`→`会員登録`→`お支払い情報の入力`→`内容の確認・規約への同意`→`申込み完了`と進んで10～20分で簡単にドメインを取得できます。（クレカ払いの場合）

## Netlifyでドメイン設定
---

### Netlifyにカスタムドメインを登録

Domain Setting→Add custom domainと進んで取得したドメインを入力`(www).xxx.com` wwwは任意で

### エックスドメインでDNSレコードを編集

<br>
#### サブドメインのwwwなしのルートドメインで運用する場合は、下記のように設定する。<br><br>

<table class="table table-striped table-bordered">
<thead>
<tr>
<th>ホスト名</th>
<th>タイプ</th>
<th>コンテンツ</th>
</tr>
</thead>
<tbody>
<tr>
<td>ravness.com</td>
<td>A</td>
<td>104.198.14.52</td>
</tr>
<tr>
<td>www.ravness.com</td>
<td>CNAME</td>
<td>※デフォルトのサブドメイン</td>
</tr>
</tbody>
</table>


※デフォルトのサブドメインはNetlifyが割り当てたドメインxxx-xxx-xxx.netlify.comみたいなURL。<br><br>

#### wwwありのサブドメインの場合


なにもしなくていい

Netlifyはwwwありのサブドメインでの利用を推奨しています。→[Naked domains?](https://www.netlify.com/docs/custom-domains/#naked-domains)<br>
理由はNetlifyの強力なCDNを使えてパフォーマンスがアップするからだそうです。


### ネームサーバーの変更

Netlifyで次のステップに進むと4つのネームサーバーが表示されるので、コピーしてエックスドメインのネームサーバーの確認・変更から４つのネームサーバーをペーストする。


![nameserver](../../../images/nameservers.jpg)   

DNSが浸透すると独自ドメインでアクセスできるようになる。


![domainset](../../../images/domainset.jpg)


### Let’s Encryptの証明書を取得

カスタムドメインを設定したらHTTPSの`Verify DNS configuration`→`Let's Encypt certificate`をクリック。しばらくすると証明書を取得できます。  
下の画面のような表示になれば成功。    


![https](../../../images/https.jpg)


### httpsを強制

Force HTTPSをクリックしてhttpでのアクセスをhttpsにリダイレクトさせる。