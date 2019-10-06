运行环境：python 3.7
操作系统：Windows 10
需安装包：scrapy,re

只需运行lele->CNKISpider->run.py即可

需要将结果储存路径做如下修改：
建议都修改为“绝对路径”
（1）进入lele->CNKISpider->CNKISpider->pipelines.py，将第17行和第39行的路径修改
（2）进入lele->CNKISpider->CNKISpider->CN.py，将第38行的路径修改

爬取结果在lele.csv中
lele->CNKISpider->lele.csv为部分爬取结果