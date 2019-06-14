#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


AUTHOR = u'AIMLESS BLOG'
SITENAME = u'Aimless Blog'
SITEURL = 'https://www.ravness.com'
#SITEURL = 'http://localhost:8000'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
ABOUT_ME = u'備忘録的ブログ'
AVATAR = ''
SIDEBAR_DIGEST = '備忘録的ブログ'

# Localeを記入することでUnicodeDecodeErrorを回避
LOCALE = ('usa', 'jpn',      # On Windows
           'en_US', 'ja_JP'   # On Unix/Linux
           )

PATH = 'content'
OUTPUT_PATH = 'output'
USE_FOLDER_AS_CATEGORY = True

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/' #gaeの場合index.html記入しないとダメっぽい
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = u'ja'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
FEED_ALL_RSS = 'feeds/all.rss.xml'

#DISPLAY_TAGS_ON_SIDEBAR_LIMIT = 5
DISPLAY_LINKS_ON_SIDEBAR_LIMIT = 5
DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True
DISPLAY_CATEGORIES_ON_SIDEBAR = True
#DISPLAY_ARCHIVE_ON_SIDEBAR = True
#BOOTSTRAP_NAVBAR_INVERSE = True
#DISPLAY_TAGS_ON_SIDEBAR = True
#TAG_CLOUD_MAX_ITEMS = 10
DISPLAY_ARTICLE_INFO_ON_INDEX = True
PYGMENTS_STYLE = 'monokai'
SUMMARY_MAX_LENGTH = 20
RELATED_POSTS_MAX = 3

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['i18n_subsites', "tag_cloud", "related_posts"]


# Blogroll
"""LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)"""

# Social widget
SOCIAL = (('tumblr', 'https://tumblr.com/blog/lollapal00za'),
          ('github', 'https://github.com/Squigly77/myblog')
          )

#DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Theme path
#THEME = './themes/pelican-bootstrap3'
#BOOTSTRAP_THEME = 'yeti'
THEME = 'themes/pelican-blue'

#template pages
TEMPLATE_PAGES = {'admin/index.html': 'admin/index.html'}

#static files path
STATIC_PATHS = ['images','static','admin','Laravel','extra/ads.txt','static/css']

EXTRA_PATH_METADATA = {
    'extra/ads.txt': {'path': 'ads.txt'},
}

#custom css
CUSTOM_CSS = 'static/css/ekko-lightbox.css'
CUSTOM_JS = 'static/js/ekko-lightbox.min.js'

GOOGLE_ANALYTICS = 'UA-67464867-3'

ADDTHIS_PROFILE = 'ra-5b3b6c6367750cca'

DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'sitemap')
SITEMAP_SAVE_AS = 'sitemap.xml'

# pelican-blue setting

DISPLAY_PAGES_ON_MENU = False
DEFAULT_PAGINATION = 10
MENUITEMS = (('Home', SITEURL),('Tags', '/tags.html'),)
LOAD_CONTENT_CACHE = False
