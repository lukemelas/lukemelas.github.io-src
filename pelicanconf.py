#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Luke Melas-Kyriazi'
SITENAME = "Luke's Notes"
SITEURL = '' # 'lukemelas.github.io'

PATH = 'content'

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Theme
THEME = 'pelican-themes/attila'
#THEME = 'pelican-themes/aboutwilson'
#THEME = 'pelican-themes/alchemy'

AUTHORS_BIO = {
    "zutrinken": {
        "name": "Zutrinken",
        "cover": "https://arulrajnet.github.io/attila-demo/assets/images/avatar.png",
        "image": "https://arulrajnet.github.io/attila-demo/assets/images/avatar.png",
        "website": "http://blog.arulraj.net",
        "location": "Chennai",
        "bio": "This is the place for a small biography with max 200 characters. Well, now 100 are left. Cool, hugh?"
    }
}


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
