# _*_ coding:utf-8 _*_

import pymongo
import datetime
client = pymongo.MongoClient(host="127.0.0.1",port=27017)
db = client.papers
biaoming = db.books


book = {"autor":"mike",
        "text":"my first book",
        "tags":{"pachong":"python"},
        "date": datetime.datetime.utcnow()
        }
print(book)
book_id = biaoming.insert(book)