# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import os,sys
import sqlite3
from CNKISpider.items import CnkispiderItem

class CNKISpiderWriteToCSVPipeline(object):

    def open_spider(self, spider):
        # print("abs path is %s" %(os.path.abspath(sys.argv[0])))
        
        self.csvFile = open(os.path.abspath('C:/大三上/lele/CNKISpider/lele.csv'), "w+",newline='')
        try:
            self.write = csv.writer(self.csvFile)
            self.write.writerow(('title', 'author', 'content', 'comment'))
        except Exception as e:
            pass 

    def close_spider(self, spider):
        self.csvFile.close()

    def process_item(self, item, spider):
        try:
            self.write.writerow((item["title"], item["author"], item["content"], item["comment"]))
        except BaseException as e:
            pass
            
        return item

class CNKISpiderWriteToDBPipeline(object):

    def open_spider(self, spider):
        try:
            self.conn = sqlite3.connect(os.path.abspath('C:/大三上/lele/CNKISpider/test.db'))
            self.cursor = self.conn.cursor()
        except BaseException as e:
            pass
            

    def close_spider(self, spider):
        try:
            self.cursor.close()
            self.conn.commit()
            self.conn.close()
        except BaseException as e:
            pass

    def process_item(self, item, spider):
        try:
            if isinstance(item, CnkispiderItem):
                self.cursor.execute('insert into PaperInfo (title, author, content, comment) values (?, ?, ?, ?)', (item["title"], item["author"], item["content"], item["comment"]))
        except BaseException as e:
            print(e)
            pass
            
        return item
