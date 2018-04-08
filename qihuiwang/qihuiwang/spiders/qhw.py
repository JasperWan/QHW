# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from qihuiwang.items import CompanyItem
from scrapy.selector import Selector
import scrapy


class QhwSpider(Spider):
    name = "qhw"
    allowed_domains = ['www.qihuiwang.com']
    start_urls = []
    # 遍历添加
    for i in range(1, 2097):
        url = 'http://www.qihuiwang.com/company/c0/p%d/?search=北京' % i
        start_urls.append(url)


    def parse_detail(self, response):
        """解析详情页"""
        sel = Selector(response)
        item = CompanyItem()
        info = sel.xpath('//div[@class="aiMain"]/ul/li')
        item['url'] = response.url
        # 公司名称
        item['company'] = info[0].xpath('./text()').extract()[0].replace('\r','').replace('\n','')
        # 注册号
        item['regNum'] = info[1].xpath('./text()').extract()[0].replace('\r','').replace('\n','')
        # 法定代表人
        item['legal'] = info[2].xpath('./text()').extract()[0].replace('\r','').replace('\n','')
        # 注册资金
        item['regCapital'] = info[3].xpath('./text()').extract()[0].replace('\r','').replace('\n','')
        # 成立时间
        item['regTime'] = info[4].xpath('./text()').extract()[0].replace('\r','').replace('\n','').replace('|',' ')
        # 经营期限
        item['endTime'] = info[5].xpath('./text()').extract()[0].replace('\r','').replace('\n','').replace('|',' ')
        # 经营范围
        item['busScope'] = info[6].xpath('./text()').extract()[0].replace('\r','').replace('\n','')
        # 登记机关
        item['regAuth'] = info[7].xpath('./text()').extract()[0].replace('\r','').replace('\n','')
        # 企业类型
        item['comType'] = info[8].xpath('./text()').extract()[0].replace('\r','').replace('\n','')
        # 年检时间
        item['insTime'] = info[9].xpath('./text()').extract()[0].replace('\r','').replace('\n','')
        # 注册地址
        item['regAddr'] = info[10].xpath('./text()').extract()[0].replace('\r','').replace('\n','')
        print(item['company'])
        return item


    def parse(self, response):
        sel = Selector(response)  # xpath选择器
        companys = sel.xpath('//a[@class="coName"]')
        for company in companys:
            url = "http://www.qihuiwang.com" + company.xpath('./@href').extract()[0]
            print(url)
            yield scrapy.Request(url, callback=self.parse_detail)