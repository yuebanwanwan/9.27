import scrapy
import requests
from lxml import etree
import re
base_urls = 'https://www.bilibili.com/anime/index/?spm_id_from=333.334.primary_menu.13#season_version=-1&area=-1&is_finish=-1&copyright=-1&season_status=-1&season_month=-1&pub_date=-1&style_id=-1&order=3&st=1&sort=0&page=1'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
}
response = requests.get(base_urls,headers = headers)
#html = etree.HTML(response.text)

if response.status_code == 200:
    print('111')
    html = etree.HTML(response.text)
    #html.xpath()返回的是一个节点类型组成的list
    fllowers = html.xpath('//strong[@class="NumberBoard-itemValue"]//text()')
    print(type(fllowers))
    reallyf = str(fllowers[1])
    r2 = re.sub("\D","",reallyf)
    r3 = int(r2)




