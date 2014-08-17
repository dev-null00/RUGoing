from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from ruevents.items import CrawlerRueventsItem
import re

class RUEventsSpider(CrawlSpider):
	name = 'ruevents'
	allowed_domains = ['ruevents.rutgers.edu']
	start_urls = ['http://ruevents.rutgers.edu/events/displayEventList.html?region=P&fromDate=11/03/10&toDate=12/29/10']
	rules = (
		Rule(SgmlLinkExtractor(allow='displayEvent\.html\?eventId=[0-9]{5}'), 
			callback='parse_events',
			follow=True,
		),
		Rule(SgmlLinkExtractor(allow='displayEventList\.html\?region=P.*fromDate=.*&toDate=.*'), 
			callback='parse_pages',
			follow=True,
		),
	)

	def parse_pages(self, response):
		hxs = HtmlXPathSelector(response)
		#events_paging = hxs.select('//div[@class="events-paging"]/a').extract()
		#for page in events_paging:
		#	print page	

	def parse_events(self, response):
		print 'hi,this is an new page! %s' % response.url		

		item = CrawlerRueventsItem()
		item['url'] = response.url
		url_len = len(response.url)
		item['event_id'] = response.url[url_len-5:url_len]
		print 'ID: found'
		print item['event_id']

		hxs = HtmlXPathSelector(response)

		temp_text = hxs.select('//h1[@class="title"]/text()').extract()
		item['event_title'] = temp_text[0]
		print 'Title: found'
		print item['event_title']

		rows = hxs.select('//table/tbody/tr')
		for row in rows:
			#traverse through each row and extract events data fields
			temp_text = row.select('td[1]/text()').extract()

			if re.match("Synopsis:", temp_text[0]):
				temp_text2 = row.select('td[2]/text()').extract()
				item['synopsis'] = temp_text2[0]
				#print 'Synopsis: found'
				#print item['synopsis']
			elif re.match("Start Time:", temp_text[0]):
				temp_text2 = row.select('td[2]/text()').extract()
				item['start_time'] = temp_text2[0]
				#print 'Start Time: found'
				#print item['start_time']
			elif re.match("End Time:", temp_text[0]):
				temp_text2 = row.select('td[2]/text()').extract()
				temp_text2[0] = temp_text2[0].replace('\n','')
				temp_text2[0] = temp_text2[0].replace('\t','')
				temp_text2[0] = temp_text2[0].strip()
				parts = temp_text2[0].split(",");
				for i in range(len(parts)):
					parts[i] = parts[i].strip()
				item['end_time'] = ",".join(parts)
				#print 'End Time: found'
				#print item['end_time']
			elif re.match("Location:", temp_text[0]):
				temp_text2 = row.select('td[2]/a/text()').extract()
				item['location'] = temp_text2[0]
				#print 'Location: found'
				#print item['location']
			elif re.match("Campus:", temp_text[0]):
				temp_text2 = row.select('td[2]/text()').extract()
				item['campus'] = temp_text2[0]
				#print 'Campus: founds'
				#print item['campus']
			elif re.match("City:*", temp_text[0]):
				temp_text2 = row.select('td[2]/text()').extract()
				temp_text2[0] = temp_text2[0].replace('\n','')
				temp_text2[0] = temp_text2[0].replace('\t','')
				temp_text2[0] = temp_text2[0].strip()
				parts = temp_text2[0].split(",")
				for i in range(len(parts)):
					parts[i] = parts[i].strip()
				item['city'] = ",".join(parts)
				#print 'City: found'
				#print item['city']
			elif re.match("Category:", temp_text[0]):
				temp_text2 = row.select('td[2]/text()').extract()
				item['category'] = temp_text2[0]
				#print 'Category: found'
				#print item['category']
			elif re.match("Web Site:", temp_text[0]):
				temp_text2 = row.select('td[2]/a/text()').extract()
				item['web_site'] = temp_text2[0]
				#print 'Web Site: found'
				#print item['web_site']
			elif re.match("Target Audience:", temp_text[0]):
				temp_text2 = row.select('td[2]/text()').extract()
				temp_text2[0] = temp_text2[0].replace('\n','')
				temp_text2[0] = temp_text2[0].replace('\t','')
				temp_text2[0] = temp_text2[0].strip()
				parts = temp_text2[0].split(",")
				for i in range(len(parts)):
					parts[i] = parts[i].strip()
				item['target_audience'] = ",".join(parts)
				#print 'Target Audience: found'
				#print item['target_audience']
		
		yield item

