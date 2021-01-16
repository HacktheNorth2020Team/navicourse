import scrapy


class HarvardSpider(scrapy.Spider):
    name = 'Harvard'
    allowed_domains = ['online-learning.harvard.edu/Catalog']
    start_urls = ['http://online-learning.harvard.edu/Catalog/free?page=' + str(i) for i in range(8)]
    global i
    i = 251

    def parse(self, response):
        global i
        courses = response.xpath('.//li[@class="views-row"]')

        for course in courses:
            title = course.xpath('.//h3/a/text()').extract()
            description = course.xpath('.//div[@class="field field-name-field-course-summary"]/text()').extract()
            link = course.xpath('.//@href').extract()
            if len(str(description)) < 5:
                pass
            else:
                yield{
                    'ID: ': i,
                    'Title: ':str(title)[2:-2],
                    'Description: ':str(description)[2:-2],
                    'Rating: ':'N/A',
                    'Link: ':'http://online-learning.harvard.edu'+str(link)[str(link).find(',')+3:-2],
                    'Source: ':'Harvard'
                    }
                i += 1

