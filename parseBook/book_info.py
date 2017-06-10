#!/usr/bin/env python
# coding:utf-8
class BookDetail:
    def __init__(self, dic_metas):
        self.title = dic_metas['og:novel:book_name']
        self.author = dic_metas['og:novel:author']
        self.image = dic_metas['og:image']
        self.category = dic_metas['og:novel:category']
        self.read_url = dic_metas['og:novel:read_url']
        self.latest_chapter_name = dic_metas['og:novel:latest_chapter_name']
        self.latest_chapter_url = dic_metas['og:novel:latest_chapter_url']
        self.description = dic_metas['og:description']
        self.status = dic_metas['og:novel:status']
        self.update_time = dic_metas['og:novel:update_time']

    def printf(self):
        print 'title                = ' + self.title
        print 'author               = ' + self.author
        print 'image                = ' + self.image
        print 'category             = ' + self.category
        print 'read_url             = ' + self.read_url
        print 'latest_chapter_name  = ' + self.latest_chapter_name
        print 'latest_chapter_url   = ' + self.latest_chapter_url
        print 'description          = ' + self.description
        print 'status               = ' + self.status
        print 'update_time          = ' + self.update_time


class BookChapter:
    # list index
    # chapterList
    # def __init__(self, title, text, url):
    #     self.title = title
    #     self.text = text
    #     self.url = url
    def __init__(self):
        self.title = ''
        self.text = ''
        self.url = ''

    def printf(self):
        print self.url + ' | ' + self.title

