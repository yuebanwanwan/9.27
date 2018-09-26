# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    base_urls = ['http://www.zhihu.com/']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
    }

    login_script = """
    function main(splash, args)
      assert(splash:go(args.url))
      assert(splash:wait(0.5))
      clickloginjs = "document.querySelector(div.SignContainer-switch span).click();"
      
      splash:evaljs(clickloginjs)
      assert(splash:wait(0.5))
      
      js = string.format("document.querySelector('div.SignFlow-accountInput.Input-wrapper input.Input').value=%d;document.querySelector('div.SignFlow-passwordInput.Input-wrapper input.Input').value=%d",args.username,args.password)
      splash:evaljs(js)
      assert(splash:wait(3))  
      return {
        html = splash:html(),
      }
    end
    """

    def start_requests(self):
        yield SplashRequest(url='https://www.zhihu.com/signup?next=%2F',callback=self.parse_login_page,args={'lua_source':self.login_script,
               'username':'13703028566','password':'zhou123456789'},headers=self.headers)



    def parse_login_page(self, response):
        pass


