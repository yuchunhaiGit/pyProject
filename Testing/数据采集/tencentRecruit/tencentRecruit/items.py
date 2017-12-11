# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.item import Item, Field

class TencentrecruitItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class PositionItem(Item):
	name = Field() #职位名称
	catalog = Field() #职位类别
	number = Field() #招聘人数
	workPlace = Field() #工作地点
	releaseTime = Field() #发布时间
	positionLink = Field() #职位详情链接
