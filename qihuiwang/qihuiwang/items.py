# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field

class QihuiwangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass



class CompanyItem(scrapy.Item):
    url = Field()
    company = Field()
    regNum = Field()
    legal = Field()
    regCapital = Field()
    regTime = Field()
    endTime = Field()
    busScope = Field()
    regAuth = Field()
    comType = Field()
    insTime = Field()
    regAddr = Field()