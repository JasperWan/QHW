# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs

class QihuiwangPipeline(object):
    # def process_item(self, item, spider):
    #     return item

    def process_item(self, item, spider):
        fp = codecs.open('qhw_detail.txt', 'a','utf-8')
        fp.write(item['url'] + '|' + item['company'] + '|' + item['regNum'] + '|' + item['legal'] + '|'
                 + item['regCapital'] + '|' + item['regTime'] + '|' + item['regTime'] + '|'
                 + item['busScope'] + '|' + item['regAuth'] + '|' + item['comType'] + '|'
                 + item['insTime'] + '|' + item['regAddr'] + '\n')
        return item

