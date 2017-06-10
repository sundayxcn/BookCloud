#!/usr/bin/env python
# coding:utf-8

#
import scrapy
import sys
import re

from book_info import BookDetail
from book_info import BookChapter
from downHtml import down_html

reload(sys)
sys.setdefaultencoding('utf-8')


def parse_detail_from_meta(response):
    metas_prop = response.xpath('//meta/@property').extract()
    metas_value = response.xpath('//meta[@property]/@content').extract()
    dic = {}
    for i in range(len(metas_prop)):
        dic[metas_prop[i]] = metas_value[i]
    return dic


def parse_chapter_list_from_dd(response):
    chapter_list = []
    chapter_url_list = response.xpath('//dd//a/@href').extract()
    for url in chapter_url_list:
        # 获取章节序号,存入数据库，真实网址拼接得来
        # 用于排序和去重,
        pattern = re.compile(r'\d[0-9]*\d\.')
        str_url = pattern.findall(url)[0]
        size = len(str_url) - 1
        chapter = BookChapter()
        chapter.url = str_url[0:size]
        chapter_list.append(chapter)
    chapter_title_list = response.xpath('//dd//a/text()').extract()
    # for title in chapter_title_list:
    #    print title
    for i in range(0, len(chapter_title_list)):
        chapter_list[i].title = chapter_title_list[i]

    return chapter_list


body = down_html.getHtml()
scr_response = scrapy.Selector(text=body, type='html')

dic = parse_detail_from_meta(scr_response)
book_detail = BookDetail(dic)
book_detail.printf()
chapter_list = parse_chapter_list_from_dd(scr_response)
for chapter in chapter_list:
    chapter.printf()



def get_book_detail():
    return book_detail

def get_book_chapter_list():
    return chapter_list