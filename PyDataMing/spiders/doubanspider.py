# -*- coding: utf-8 -*-
import scrapy
import logging
from scrapy.spiders import CrawlSpider
from scrapy.http import Request
from scrapy.selector import Selector
from PyDataMing.items import PydatamingItem
import json
from PyDataMing.ShowJson import showJson
from PyDataMing.getallurl import allUrl
class Douban(CrawlSpider):

    name = "douban"
    redis_key = 'douban:start_urls'
    global url
    url = 'http://www.3sogou.com/read.php?tid=1089011'
    start_urls = allUrl()

    def parse(self, response):
        currenturl = response.url

        # 源字典
        dict = {'post': '', 'replys': ''}
        # 定义 post 内部数据
        post = {}
        # 定义 replys 内部数据,列表  形式    ，循环把字典放入这里
        # replys = []


        selector = Selector(response)

        # 标题筛选
        tit = selector.xpath('//span[@id="thread_subject"]/text()').extract()
        if tit:
            titl = "".join(tit)
        else:
            tit = selector.xpath('//*[@id="thread_subject"]/text()').extract()
        if tit:
            titl = "".join(tit)
        else:
            tit = selector.xpath('//div[@class="bbs-title"]/h2/text()').extract()
        if tit:
            titl = "".join(tit)
        else:
            tit = selector.xpath('//*[ @ id = "consnav"] / span[4]/text()').extract()
        if tit:
            titl = "".join(tit)
        else:
            tit = selector.xpath('//*[@class="tit"]/h2/text()').extract()
        if tit:
            titl = "".join(tit)
        else:
            tit = selector.xpath('//*[@id="subject_tpc"]/text()').extract()
        if tit:
            titl = "".join(tit)
        else:
            tit = selector.xpath('//span[@class="s_title"]/span/text()').extract()
        if tit:
            titl = "".join(tit)
        else:
            tit = selector.xpath('//div[@class="title_box"]/h1/text()').extract()
        if tit:
            titl = "".join(tit)
        else:
            # 太平洋
            tit = selector.xpath('//*[@class="tit"]/a/text()').extract()
        if tit:
            titl = "".join(tit)
        else:
            # 新浪股吧
            tit = selector.xpath('//*[@class="il_txt"]/h4/text()').extract()
        if tit:
            titl = "".join(tit)
        else:
            # 55style论坛
            tit = selector.xpath('//*[@class="card_person_center"]/h3/text()').extract()
        if tit:
            titl = "".join(tit)
        else:
            # 虎扑 论坛
            tit = selector.xpath('//*[@class="bbs-hd-h1"]/h1/text()').extract()
        if tit:
            titl = "".join(tit)
        else:
            # 金融界 论坛
            tit = selector.xpath('//div[@class="ltit"]/h1/b/text()').extract()
        if tit:
            titl = "".join(tit)
        else:
            # 育儿 论坛
            tit = selector.xpath('//div[@class="title clearfix"]/h3/text()').extract()
        if tit:
            titl = "".join(tit)
        else:
            # 太平洋 论坛
            tit = selector.xpath('//i[@id="subjectTitle"]/text()').extract()
        if tit:
            titl = "".join(tit)
        else:
            # 太平洋亲子网 论坛  PCbaby
            tit = selector.xpath('//div[@class="post_r_tit"]/h1/text()').extract()
        if tit:
            titl = "".join(tit)
        else:
            # 大众点评
            tit = selector.xpath('//div[@class="note-info no-img"]/p[@class="note-title"]/text()').extract()
        if tit:
            titl = "".join(tit)
        else:
            # 慧聪 商学院
            tit = selector.xpath('//div[@class="share_left"]/div[@class="Amain"]/h1/text()').extract()
        if tit:
            titl = "".join(tit)
        else:
            #  羊城生活网
            tit = selector.xpath('//div[@class="mainbox viewthread"]/h1/text()').extract()
        if tit:
            titl = "".join(tit)
        else:
            #  新浪 亲子论坛 网
            tit = selector.xpath('//div[@class="mainbox viewthread "]/h1/text()').extract()
        if tit:
            titl = "".join(tit)
        else:
            #  爱卡汽车 论坛
            tit = selector.xpath('//h1[@class="title"]/text()').extract()
        if tit:
            titl = "".join(tit)
        else:
            # DOSPY 论坛       这个最好一直放在最后    很多论坛适用这个
            tit = selector.xpath('//title/text()').extract()
        if tit:
            titl = "".join(tit)


        print '标题',titl



        # 时间数据筛选
        # 威锋网 适用  feng.com
        tim = selector.xpath('//div[@class="authi"]/em[starts-with(@id,"authorposton")]').xpath('string(.)').extract()
        # print 'tim',tim        叶子猪论坛
        # t = selector.xpath('//div[@class="authi"]/em[starts-with(@id,"authorposton")]/span/text()').extract()
        # print 't',t
        # tim = tim + t
        if tim:
            time = "".join(tim[0])
        else:
            tim = selector.xpath('//em[starts-with(@id,"authorposton")]/text()').extract()
        if tim:
            time = "".join(tim[0])
        else:
            tim = selector.xpath('// *[ @ class = "bbs-list"] / div[2] / div[1] / span[1]/text()').extract()
        if tim:
            time = "".join(tim[0])
        else:
            tim = selector.xpath('//*[@xname="date"]/text()').extract()
        if tim:
            time = "".join(tim[0])
        else:
            tim = selector.xpath('//*[@class="article_foot"]/span/text()').extract()
        if tim:
            time = "".join(tim[0])
        else:
            tim = selector.xpath('//*[@class="floot_right"]/div[1]/span[2]/text()').extract()
        if tim:
            time = "".join(tim[0])
        else:
            tim = selector.xpath('//*[@id="my_info_d"]/text()').extract()
            temp = selector.xpath('//*[@class="my_xiangqing_shijian"]/text()').extract()
            tim.extend(temp)
            # 合并列表
        if tim:
            time = "".join(tim[0])
        else:
            tim = selector.xpath('//*[@class="atl-info"]/span[2]/text()').extract()
        if tim:
            time = "".join(tim[0])
        else:
            tim = selector.xpath('//*[@class="time_box"]/span/text()').extract()
            temp = selector.xpath('//*[@class="time_postcont"]/span/text()').extract()
            tim.extend(temp)
        if tim:
            time = "".join(tim[0])
        else:
            # 太平洋
            tim = selector.xpath('//span[@class="date"]/text()').extract()
        if tim:
            time = "".join(tim[0])
        else:
            # 新浪股吧
            tim = selector.xpath('//*[@class="ilt_panel clearfix"]/div[1]/span[1]/text()').extract()
        if tim:
            time = "".join(tim[0])
        else:
            # 55bbs论坛，暂时拿一个时间   ,user_card_lou 全部
            tim = selector.xpath('//*[@class="user_card_time"]/text()').extract()
        if tim:
            time = "".join(tim[0])
        else:
            # DOSPY 论坛
            tim = selector.xpath('//div[@class="pi cb cf lh40 pl15 pr15 txt_333"]/text()[2]').extract()
        if tim:
            time = "".join(tim[0])
        else:
            # 金融界 论坛
            tim = selector.xpath('//div[@class="author"]/p[@class="name"]/span/text()').extract()
        if tim:
            time = "".join(tim[0])
        else:
            # 育儿 论坛
            tim = selector.xpath('//div[@class="post_head"]/div[2]/text()[1]').extract()
        if tim:
            time = "".join(tim[0])
        else:
            # 太平洋 论坛
            tim = selector.xpath('//div[@class="post_time"]/text()').extract()
        if tim:
            time = "".join(tim[0])
        else:
            # 太平洋 亲子论坛 PCbaby
            tim = selector.xpath('//div[@class="post_info"]/div[starts-with(@class,"user")]/text()').extract()
        if tim:
            time = "".join(tim[0])
        else:
            # 羊城生活网
            tim = selector.xpath('//td[@class="postcontent"]/div[@class="postinfo"]/text()[5]').extract()
        if tim:
            time = "".join(tim[0])
        else:
            # 新浪 亲子论坛
            tim = selector.xpath('//td[starts-with(@class,"postcontent")]/div[@class="postinfo"]/text()[5]').extract()
        if tim:
            time = "".join(tim[0])
        else:
            # 大众点评网
            tim = selector.xpath('//*[@class="topic-info"]/span[@class="time"]/text()').extract()
        if tim:
            time = "".join(tim[0])
        else:
            # 慧聪商学院  论坛,评论者的时间没法爬取
            tim = selector.xpath('//div[@class="header_tool clearFloat"]/p[@class="header_tool_l"]/span[@class="time"]/text()').extract()
            #tim = selector.xpath('//div[@class="pl_1_right"]/div[@class="p1_name"]'
                                # '/span[@class="p1_time"]/text()').extract()
            #tim.insert(0, t[0])
        if tim:
            time = "".join(tim[0])
        else:
            # 大粤社区 网  论坛
            t = selector.xpath('//div[@class="post_t gray"]/div[@class="authi z"]/span/em/text()').extract()
            tim = selector.xpath('//div[@class="p_t cl"]/div[@class="z"]'
                                 '/span[@class="gray mlm"]/em/text()').extract()
            tim.insert(0, t[0])
        if tim:
            time = "".join(tim[0])
        else:
            # 虎扑 论坛              只检索 楼主和  highlights 的
            t = selector.xpath('//div[@class="left"]/span[@class="stime"]/text()').extract()
            tim = selector.xpath('//div[@id="readfloor"]/div[@class="floor"]'
                                 '/div[@class="floor_box"]/div/div/span[@class="stime"]/text()').extract()
            tim.insert(0, t[0])
        if tim:
            time = "".join(tim[0])

        print '时间个数',len(tim)



        # content数据筛选
        #.xpath('//div[@class="t_fsz"]/table/tbody/tr/td[@class="t_f"]/span[@id="travle_body"]')
        data = selector.xpath('//span[@id="travle_body"]')
        # 时空网，广西论坛，又卡又慢
        con = data.xpath('string(.)').extract()
        if data:
            print len(data)
            cont = "".join(con[0])
        else:     # 同时适用叶子猪论坛.两个切换：
            data = selector.xpath('//div[@class="t_fsz"]/table/tr/td[@class="t_f"]')
            #data = selector.xpath('//div[@class="t_fsz"]/table/tbody/tr/td[@class="t_f"]')
            con = data.xpath('string(.)').extract()
        if data:
            cont = "".join(con[0])
        else:
            data = selector.xpath('//*[@class="bbs-list"]/div[2]/div[2]')
            con = data.xpath('string(.)').extract()
        if data:
            cont = "".join(con[0])
        else:
            #针对第四个 URL ，没抓到 post 内容
            data = selector.xpath('//*[@class="rconten"]/div[2]')
            con = data.xpath('string(.)').extract()
        if data:
            cont = "".join(con[0])
        else:
            #这里居然劫持了新浪股吧  的一个文字。   青青岛社区
            data = selector.xpath('//*[@class="layer_c"]/div[2]')
            con = data.xpath('string(.)').extract()
        if data:
            cont = "".join(con[0])
        else:
            data = selector.xpath('//*[@class="tpc_content"]')
            con = data.xpath('string(.)').extract()
        if data:
            cont = "".join(con[0])
        else:
            # 天涯社区 的  ok
            data = selector.xpath('//*[normalize-space(@class)="atl-content"]/div[2]/div')
            con = data.xpath('string(.)').extract()
        if data:
            cont = "".join(con[0])
        else:
            # 易车论坛 的内容,有问题   http://baa.bitauto.com/changancs75/thread-9819102.html
            con = selector.xpath('//*[@class="post_width"]/p[2]/span').xpath('string(.)').extract()
            tempdata = selector.xpath('//*[@class="post_width"]/p').xpath('string(.)').extract()
            con.extend(tempdata)
        if con:
            cont = "".join(con[0])
        else:
            # 太平洋 汽车
            con = selector.xpath('//td[@class="post_msg_wrap"]/div[@class="post_msg replyBody"]')\
                .xpath('string(.)').extract()
        if con:
            cont = "".join(con[0])
        else:
            # 太平洋 手机
            con = selector.xpath('//*[@class="topiccontent"]').xpath('string(.)').extract()
            tempdata = selector.xpath('//*[@class="replycontent"]').xpath('string(.)').extract()
            con.extend(tempdata)
        if con:
            cont = "".join(con[0])
        else:
            # 育儿论坛  内容
            con = selector.xpath('//*[@class="post_content"]/div/div').xpath('string(.)').extract()
        if con:
            cont = "".join(con[0])
        else:
            # 新浪股吧  内容
            con = selector.xpath('//*[@class="ilt_p"]/text()').extract()
        if con:
            cont = "".join(con[0])
        else:
            # 55BBS 论坛    http://bbs.55bbs.com/thread-10139816-1-1.html        暂时没处理
            data = selector.xpath('//*[@class="card_note_matter"]/div[1]')
            con = data.xpath('string(.)').extract()
        if con:
            cont = "".join(con[0])
        else:
            # DOSPY 论坛   适用，新浪亲子网
            data = selector.xpath('//*[@class="t_msgfont"]')
            con = data.xpath('string(.)').extract()

        if con:
            cont = "".join(con[0])
        else:
            # 太平洋 亲子网 论坛
            data = selector.xpath('//div[@class="post_msg"]/div[1]')
            con = data.xpath('string(.)').extract()
        if con:
            cont = "".join(con[0])
        else:
            # 虎扑 论坛      有点问题，跳过先     https://bbs.hupu.com/17680096.html
            con = selector.xpath('//div[@class="quote-content"]').xpath('string(.)').extract()
            #con = selector.xpath('//div[@id="readfloor"]/div[@class="floor"]'
                               #  '/div[@class="floor_box"]/table[@class="case"]/tbody/tr/td/text()').extract()

            #con.insert(0, n[0])
            #print len(con)
        if con:
            cont = "".join(con[0])
        else:
            #  金融界 论坛
            data = selector.xpath('//*[@id="msgMainContent"]')
            con = data.xpath('string(.)').extract()
        if con:
            cont = "".join(con[0])
        else:
            #  慧聪 尚学院  论坛
            data = selector.xpath('//*[@class="Amain_main"]')
            con = data.xpath('string(.)').extract()
        if con:
            cont = "".join(con[0])
        else:
            # 大众点评网,回复的内容大部分是一个图标
            data = selector.xpath('//div[@class="topic-entry"]')
            con = data.xpath('string(.)').extract()
            a = [0, 0, 0, 0, 0, 0]
            con = con+a
            print con
        if con:
            cont = "".join(con[0])



        # 作者模块搞定
        post['publish_date'] = time.strip()
        post['content'] = cont.strip()
        post['title'] = titl.strip()


        #循环把回复的 字典 添加进入 replys 列表中
        del tim[0]
        del con[0]

        print '回复个数',len(tim)
        i = 0

        replys = range(len(tim))


        while i < len(tim):
          replys[i] = {}
          replys[i]['publish_date'] = "".join(tim[i]).strip()
          replys[i]['content'] = "".join(con[i]).strip()
          replys[i]['title'] = titl.strip()
          i +=1

        dict['replys'] = replys
        dict['post'] = post

        showJson(currenturl, dict)
