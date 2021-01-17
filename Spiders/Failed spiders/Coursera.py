import scrapy


class CourseraSpider(scrapy.Spider):
    name = 'Coursera'
    allowed_domains = ['www.coursera.org/search?']
    start_urls = ["https://www.coursera.org/search?page="+str(i)+"&index=prod_all_products_term_optimization&allLanguages=English" for i in range(1, 101)]

    def parse(self, response):
        courses = response.xpath('.//div[@class="card-info vertical-box"]')

        for course in courses:
            name = course.xpath('.//h2/text()').extract()
            spantag = course.xpath('.//span/text()').extract() #['University of Michigan', '4.7', '(690)', '15k', ' students', 'Beginner']
            
            coursetype = course.xpath('.//div[@class="_jen3vs _1d8rgfy3"]').extract()
            if len(str(name)) == len(str(name).encode()):
                yield{
                    'Name: ':name,
                    'Rating: ':spantag[1],
                    'Partner: ':spantag[0],
                    'Difficulty: ':spantag[5],
                    # 'Link: ':link
                    }
            else:
                pass
# Everything could be scraped except for the description and the link to the course
# This outputs 1000 courses, which could have been very useful for the project
