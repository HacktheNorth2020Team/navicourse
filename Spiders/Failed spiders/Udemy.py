import scrapy


class UdemySpider(scrapy.Spider):
    name = 'Udemy'
    allowed_domains = ['www.udemy.com/courses/free/']
    start_urls = ['http://www.udemy.com/courses/free/?p=' + str(i) for i in range(1,38)]

    def parse(self, response):
        courses = response.xpath('.//div[@class="course-list--container--3zXPS"]')

        for course in courses:
            divtag = course.xpath('.//div/text()').extract()
            #description = course.xpath('.//p/text()').extract()
            #spantag = course.xpath('.//span/text()').extract()
            
            yield{
                'Name: ':divtag#,
                #'Description ':description,
                #'Rating ':spantag
                }

# 'courses' is not picking up anything, nothing could be extracted.
