# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class CrawlerRueventsItem(Item):
    # define the fields for your item here like:
    # name = Field()
    #pass
	url = Field()
	event_id = Field()
	event_title = Field()
	synopsis = Field()
	start_time = Field()
	end_time = Field()
	location = Field()
	address = Field()
	campus = Field()
	city = Field()
	category = Field()
	web_site = Field()
	target_audience = Field()
