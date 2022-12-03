# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo

class MongoDBPipeline(object):
	def __init__(self):
		self.conn = pymongo.MongoClient('localhost', 27017)
		db = self.conn['book_list']
		self.collection = db['book_info']

	def process_item(self, item, spider):
		self.collection.insert(dict(item))
		return item
