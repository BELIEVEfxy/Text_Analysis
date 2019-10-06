# -*- coding: utf-8 -*-
import scrapy
import re
import time
from CNKISpider.items import CnkispiderItem
import urllib.request
from urllib.error import URLError
from lxml import etree
import os


class LeleSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://www.leleketang.com/zuowen/clist0-0-0-1-1.shtml'       
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    #对于一个作文，提取其中的标题 作者 正文 评论
    def parseNews(self, response):
        item = CnkispiderItem()
        title = response.css(".cp_htitle::text").extract_first()
        author = response.css(".cp_author ::text").extract_first()
        content = response.css(".cp_content p::text").extract()
        content_ = ''.join(content)
        comment =  response.css(".cp_comment p::text").extract_first()
        item['title'] = title
        item['author'] = author
        item['content'] = content
        item['comment'] = comment
        print('title:',title)
        print('author:',author)
        print('content:',content)
        print('comment:',comment)
        f = open('C:/大三上/lele/CNKISpider/lele.csv','a',encoding='utf-8')#储存路径
        f.write(title+','+author+','+content[0]+','+comment+'\n')
        yield item
        #yield{"title":title,"author":author,"content":content_,"comment":comment}

    def parse(self, response):
        newslist=response.css("div.item div.item_title.clearfix a")#获取作文的列表
        for news in newslist:
            url=news.css("a ::attr('href')").extract_first()#抽取连接
            yield response.follow(url, callback=self.parseNews)
        nextpage=response.css(".p_pager_web a.p_next ::attr('href')").extract_first()
        time.sleep(1)
        if nextpage is not None:
            yield response.follow(nextpage, callback=self.parse)
        


