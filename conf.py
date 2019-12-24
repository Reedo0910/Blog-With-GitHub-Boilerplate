# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/Prism-Blog/"
source_dir = "../src/"
build_dir = "../dist/"
template = "Prism"
index_page_size = 10
archives_page_size = 20
enable_jsdelivr = {
    "enabled": True,
    "repo": "Reedo0910/Prism-Blog@gh-pages"
}

# 站点设置
site_name = "Prism示例博客"
site_logo = "${static_prefix}logo.png"
site_build_date = "2019-12-23T16:51+08:00"
author = "Zeee"
email = "ericrlee@outlook.com"
author_homepage = "https://www.velas.xyz"
description = "Hello World"
key_words = ['Prism', 'Zeee', 'blog']
language = 'zh-CN'
background_img = '${static_prefix}bg/bg.jpg'
external_links = [
    {
        "name": "Velas电波站",
        "url": "https://www.velas.xyz",
        "brief": "非正常信号发射与搜寻装置"
    }
    # {
    #     "name": "三無計劃",
    #     "url": "https://www.imalan.cn",
    #     "brief": "熊猫小A的主页。"
    # }
]
nav = [
    {
        "name": "首页",
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
    # {
    #     "name": "Twitter",
    #     "url": "",
    #     "icon": "gi gi-twitter"
    # },
    {
        "name": "GitHub",
        "url": "https://github.com/Reedo0910",
        "icon": "gi gi-github"
    }
    # {
    #     "name": "Weibo",
    #     "url": "",
    #     "icon": "gi gi-weibo"
    # }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
