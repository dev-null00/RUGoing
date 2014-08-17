# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher
from scrapy.exceptions import DropItem
from scrapy.contrib.exporter import XmlItemExporter

class RueventsPipeline(object):
	def __init__(self):
		self.duplicates = {}
		self.files = {}
		dispatcher.connect(self.spider_opened, signals.spider_opened)
		dispatcher.connect(self.spider_closed, signals.spider_closed)

	def spider_opened(self, spider):
		self.duplicates[spider]=set()
		file = open('%s_items.xml' % spider.name, 'w+b')
		self.files[spider] = file
		self.exporter = XmlItemExporter(file)
		self.exporter.start_exporting()
	
	def spider_closed(self, spider):
		del self.duplicates[spider]
		self.exporter.finish_exporting()
		file = self.files.pop(spider)
		file.close()

	def process_item(self, item, spider):
		if item['event_id'] in self.duplicates[spider]:
			raise DropItem("Duplicate item found!")
		else:
			self.duplicates[spider].add(item['event_id'])
			self.exporter.export_item(item)
			return item
