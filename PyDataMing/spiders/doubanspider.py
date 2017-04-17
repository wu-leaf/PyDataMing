# -*- coding: utf-8 -*-
import scrapy

from scrapy.spiders import CrawlSpider
from scrapy.http import Request
from scrapy.selector import Selector
from PyDataMing.items import PydatamingItem
import json
from PyDataMing.ShowJson import showJson

class Douban(CrawlSpider):

    name = "douban"
    redis_key = 'douban:start_urls'
    start_urls = ['http://x.heshuicun.com/forum.php?mod=viewthread&tid=80']

    url = 'http://x.heshuicun.com/forum.php?mod=viewthread&tid=80'

    def parse(self, response):
        # 源字典
        dict = {'post': '', 'replys': ''}
        # 定义 post 内部数据
        post = {}
        # 定义 replys 内部数据,列表  形式    ，循环把字典放入这里
        #replys = []


        selector = Selector(response)
        tit = selector.xpath('//span[@id="thread_subject"]/text()').extract()
        titl = "".join(tit)

        #一次拿到所有时间数据
        tim = selector.xpath('//em[starts-with(@id,"authorposton")]/text()').extract()
        print len(tim)
        time = "".join(tim[0])

        #一次性拿到所有 content
        data = selector.xpath('//div[@class="t_fsz"]/table/tr/td[@class="t_f"]')
        con = data.xpath('string(.)').extract()
        cont = "".join(con[0])

        # 作者模块搞定
        post['publish_date'] = time
        post['content'] = cont
        post['title'] = titl


        #循环把回复的 字典 添加进入 replys 列表中
        del tim[0]
        del con[0]

        print len(tim)
        i = 0

        replys = range(len(tim))



        while i < len(tim):
          replys[i] = {}
          replys[i]['publish_date'] = "".join(tim[i])
          replys[i]['content'] = "".join(con[i])
          replys[i]['title'] = titl
          i +=1

        dict['replys'] = replys
        dict['post'] = post

        #print dict
        showJson(dict)
