# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"

# to use theme in another local folder, set:
template = {
    "name": "Prism",
    "type": "local",
    "path": "../Templates/Prism"
}
# template = "Prism"

index_page_size = 5
archives_page_size = 10
locale = "Asia/Shanghai"
category_by_folder = False
enable_jsdelivr = {
    "enabled": True,
    "repo": "Reedo0910/Prism-Blog@gh-pages"
}

# 站点设置
site_name = "灯森"
site_logo = "${static_prefix}logo.png"
site_build_date = "2019-12-23T16:51+08:00"
author = "Zeee"
email = "ericrlee@outlook.com"
author_homepage = "https://www.velas.xyz"
description = "另一边的风景"
key_words = ['Prism', 'Zeee', 'blog']
language = 'zh-CN'
background_img = ''
external_links = [
    {
        "name": "Velas电波站",
        "url": "https://www.velasx.com",
        "brief": "非正常信号发射与搜寻装置"
    }
]
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
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
<link rel="shortcut icon" href="/favicon.ico">
'''

footer_addon = '<a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="知识共享许可协议" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" /></a><br />本作品由<a xmlns:cc="http://creativecommons.org/ns#" href="https://www.akari-mori.com/" property="cc:attributionName" rel="cc:attributionURL">Zeee</a>采用<a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">知识共享署名-非商业性使用-禁止演绎 4.0 国际许可协议</a>进行许可。<br />基于<a xmlns:dct="http://purl.org/dc/terms/" href="https://www.akari-mori.com/" rel="dct:source">https://www.akari-mori.com/</a>上的作品创作。'

body_addon = ''
