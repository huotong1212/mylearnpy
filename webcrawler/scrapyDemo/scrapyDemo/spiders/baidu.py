# -*- coding: utf-8 -*-
import scrapy
from scrapy import cmdline
import sys
import io
from scrapy.http import Request
from scrapy.selector import Selector, HtmlXPathSelector

class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['https://www.baidu.com/']

    def parse(self, response):
        print('中文测试-----')
        # print(response.url)
        # # print(dir(response))
        # print(response.text)
        # print(response.body)
        # print(response.text)

        # 在全局下找到所有id = "s_kw_wrap"的span标签
        span = Selector(response=response).xpath('//a')
        print(span)
        # 在span中找到class="s_ipt"的input标签，并将其转换为字符串列表后返回第一个字符串
        sinput = span.xpath('//input[@class="s_ipt"]')
        a = span.xpath('//a').extract_first()

        print(sinput)
        print(a.strip())





cmdline.execute("scrapy crawl baidu --nolog".split())
