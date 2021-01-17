import scrapy

class AlisonSpider(scrapy.Spider):
    name = 'Alison'
    allowed_domains = ['alison.com/courses']
    start_urls = ['https://alison.com/courses/it?page=' + str(i) for i in range(1,15)]

    def parse(self, response):
        courses = response.xpath('.//li')
        print(courses)

        for course in courses:
            title = course.xpath('.//h5/text()').extract()
            description = course.xpath('.//div/text()').extract()
            link = course.xpath('.//@href').extract_first()

            if description == None:
                pass
            
            else:
                yield{
                    'Title: ':title,
                    'Description: ':description,
                    'Rating: ':'N/A',
                    'Link: ':link,
                    'Source: ':'Alison'
                    }

# Outputs nothing in the variable 'courses', can't find how to get them yet
