# _*_coding:utf-8 _*_
import  pymysql
import requests
from lxml import etree
import re
lianjie = pymysql.connect(user = "root",password = "123456",host = "127.0.0.1",port = 3306,db = "ceshi",charset="utf8")
cursor = lianjie.cursor()
url = "http://news.qq.com/"
url_html = requests.get(url).text
html = etree.HTML(url_html)
demo = html.xpath("//div[@class='Q-tpList']/div/div/em/a/text()")
for i in demo:
    sql = "insert into news(xinwen) VALUES ('"+i+"')"
    cursor.execute(sql)
    update = "update news set xinwen = '"+i+"' where xinwen = '"+i+"'"
    print(update)
    cursor.execute(update)
    lianjie.commit()



