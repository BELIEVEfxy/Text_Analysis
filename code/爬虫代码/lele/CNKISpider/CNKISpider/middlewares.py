# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import time,os


class CnkispiderSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(s.spider_closed, signal=signals.spider_closed)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        self.startTime = time.time()
        # print('__file__ is %s' % __file__)
        # print ("path ====== %s " % os.path.normcase(__file__))
        print('   爬虫开始   '.center(50, "*"))
        print(('   开始时间：%.2f   ' % self.startTime).center(50, "*"))

    def spider_closed(self, spider):
        self.endTime = time.time()
        _t = self.endTime - self.startTime
        print(('   结束时间：%.2f   ' % self.endTime).center(50, "*"))
        print(('   耗时：%.2f s   ' % _t).center(50, "*"))
        print('   爬虫结束   '.center(50, "*"))

class MyproxiesSpiderMiddleware(object):

    def __init__(self):  
        self.ips = []
        
    def process_request(self, request, spider):  
        pass
        # if spider.name == 'question':
        #     ip = "https://116.3.94.128:80"
        #     # print("============ 使用代理 %s ============" % ip)
        #     request.meta["proxy"] = ip
