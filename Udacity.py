import scrapy


class UdacitySpider(scrapy.Spider):
    name = 'Udacity'
    allowed_domains = ['www.udacity.com/courses/all']
    start_urls = ['http://www.udacity.com/courses/all/']

    def parse(self, response):
        courses = response.xpath('.//li[@class="catalog-cards__list__item"]')

        for course in courses:
            title = course.xpath('.//h2/text()').extract()
            description = course.xpath('.//p/text()').extract()
            link = course.xpath('.//@href').extract_first()
            
            yield{
                'Title: ':title,
                'Description: ':' '.join(description),
                'Rating: ':'N/A',
                'Link: ':str("https://www.udacity.com" + link),
                'Source: ':'Udacity'
                }
