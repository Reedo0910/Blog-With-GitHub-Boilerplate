# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"

# to use theme in another local folder, set:
# template = {
#     "name": "Prism",
#     "type": "local",
#     "path": "../Templates/Prism"
# }

# template = "Prism"

template = {
    "name": "Prism",
    "type": "git",
    "url": "https://github.com/Reedo0910/Maverick-Theme-Prism.git",
    "branch": "deploy"
}

index_page_size = 5
archives_page_size = 10
locale = "Asia/Shanghai"
category_by_folder = False
fetch_remote_imgs = True
enable_jsdelivr = {
    "enabled": True,
    "repo": "Reedo0910/Prism-Blog@gh-pages"
}
parse_alt_as_figcaption = False

# 站点设置
site_name = "灯森"
site_logo = "${static_prefix}logo.png"
site_build_date = "2019-12-23T16:51+08:00"
author = "Zeee"
email = "ericrlee@outlook.com"
author_homepage = "https://www.velasx.com"
description = "另一边的风景"
key_words = ['Akari Mori', 'Velas电波站', '博客', 'Prism']
language = 'zh-CN'
background_img = ''
external_links = []
nav = [
    {
        "name": "博客",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "GitHub",
        "url": "https://github.com/Reedo0910",
        "icon": "gi gi-github"
    }
]

valine = {
    "enable": True,
    "appId": "vCqjtUlqwGDLvu7RLHM8HFik-gzGzoHsz",
    "appKey": "XbhG90ewd7thakxgvv1zRhO3",
    "el": '#vcomments',
    "avatar": "identicon",
    "notify": "true",
    "visitor": "true",
    "recordIP": "true",
    "placeholder": " "
}

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
<link rel="dns-prefetch" href="//www.akari-mori.com" />
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<link rel="shortcut" sizes="180x180" href="/apple-touch-icon.png">
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
<link rel="apple-touch-icon-precomposed" sizes="180x180" href="/apple-touch-icon.png">
<link rel="icon" href="/favicon.ico">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
<meta name="application-name" content="灯森">
<meta name="apple-mobile-web-app-title" content="灯森">
<meta name="msapplication-TileColor" content="#ffffff">
<meta name="theme-color" content="#ffffff">
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-124627473-2"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-124627473-2');
</script>
'''

footer_addon = ''

body_addon = ''
