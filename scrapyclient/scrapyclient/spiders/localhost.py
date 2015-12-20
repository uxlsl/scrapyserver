# -*- coding: utf-8 -*-
import json
import scrapy


class LocalhostSpider(scrapy.Spider):
    name = "localhost"
    allowed_domains = ["localhost"]
    start_urls = (
        'http://localhost:5600/tutorial/',
    )

    def login(self, response):
        names = ['csrfmiddlewaretoken', 'next']
        login_info = {}
        for i in names:
            value = response.xpath(
                '//input[@name="%s"]/@value' % (i)).extract()[0]
            login_info[i] = value
        login_info['username'] = "admin"
        login_info['password'] = "admin"
        self.logger.error(login_info)
        return scrapy.FormRequest.from_response(
            response, formdata=login_info, callback=self.after_login
        )

    def after_login(self, response):
        if "accounts/login" in response.url:
            self.logger.error("fail")
            return

        for url in response.css('a::attr(href)').extract():
            yield scrapy.Request(response.urljoin(url), self.parse_item)

    def parse(self, response):
        if "accounts/login" in response.url:
            return self.login(response)

    def parse_item(self, response):

        return json.loads(response.body)
