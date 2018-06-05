Title: Google App EngineでFlaskを使う
Date: 2018-05-17 21:00
Category: GAE
Tags: Python,GAE
Slug: gaeflasks

Google App EngineでFlaskを使う時のチュートリアル

### Google App Engineでサードパーティ製ライブラリを使う

GAEでサードパーティ製ライブラリを使うにはルートディレクトリにlibディレクトリを作ってそこにライブラリをインストールします。Flaskをインストールする場合は
```

mkdir lib
pip install -t lib/ Flask
```

これでlibディレクトリにFlaskがインストールされました。

### appengine_config.py

appengine_config.pyというファイルをapp.yamlがある場所に作成して、以下の記述をする
```python

# appengine_config.py
# coding: utf-8
from google.appengine.ext import vendor
# Add any libraries install in the "lib" folder.
vendor.add('lib')
```

プロジェクトのディレクトリ構成はこんな感じになる

```
myproject/
  lib/
  app.yaml
  appengine_config.py
  main.py
```

なお、このページにある[組み込みサードパーティ ライブラリ](https://cloud.google.com/appengine/docs/standard/python/tools/built-in-libraries-27?hl=ja)はインストールする必要はなく、app.yamlに記述するだけで良い

```yaml

libraries:
- name: jinja2
  version: latest
```

### app.yaml

app.yamlにstaticファイルやテンプレートファイルの場所を記述します

```yaml

runtime: python27
api_version: 1
threadsafe: yes

handlers:
- url: /static
  static_dir: static

- url: /templates
  static_dir: .*\.html

- url: /.*
  script: main.app
```

### main.pyにFlaskをインポート

```python

#!  /usr/bin/env python
#-*- coding: utf-8-*-
from flask import Flask, request, redirect, url_for, render_template, g

app = Flask(__name__)

@app.route('/')
def test():
    return "Hello World!"

```

### ローカルにサーバーを立ち上げる

`dev_appserver.py .`でローカルにサーバーを立ち上げて、`localhost:8080`にブラウザからアクセスすると"Hello World!"が表示されると思います。

### デプロイ

`gcloud app deploy app.yaml --project idkidc-980`でデプロイ。<br>
`https://プロジェクト名.appspot.com/`にアクセスして"Hello World!"が表示されていることを確認。

参考サイト<br>
[Getting Started with Flask on App Engine Standard Environment](https://cloud.google.com/appengine/docs/standard/python/getting-started/python-standard-env)<br>
サードパーティライブラリの使い方:[Using third-party libraries](https://cloud.google.com/appengine/docs/standard/python/tools/using-libraries-python-27?hl=ja)
