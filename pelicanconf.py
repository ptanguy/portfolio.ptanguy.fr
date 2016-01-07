#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'ptanguy'
SITENAME = u"ptanguy's portfolio"
SITEURL = ''

USE_FOLDER_AS_CATEGORY = False

PATH = 'content'
STATIC_PATHS = ['files','images']
ARTICLE_PATHS = ['projects']

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Formatting for urls
ARTICLE_URL = "projects/{date:%Y}/{date:%m}/{date:%d}/{slug}/"
ARTICLE_SAVE_AS = "projects/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html"


# Generate yearly archive

YEAR_ARCHIVE_SAVE_AS = 'projects/{date:%Y}/index.html'

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/phtanguy'),
        ('Github', 'https://github.com/ptanguy'),)


DEFAULT_PAGINATION = 10


THEME = "pelican-bootstrap3"
BOOTSTRAP_THEME = 'united'

#Template settings
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
TAG_CLOUD_MAX_ITEMS = 10

#Sidebar options
DISPLAY_TAGS_ON_SIDEBAR = False
DISPLAY_CATEGORIES_ON_SIDEBAR = True

#
BOOTSTRAP_NAVBAR_INVERSE=True

#
DISPLAY_BREADCRUMBS=True
DISPLAY_CATEGORY_IN_BREADCRUMBS=True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
