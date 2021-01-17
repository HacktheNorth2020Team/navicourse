import scrapy


class SkillshareSpider(scrapy.Spider):
    name = 'Skillshare'
    allowed_domains = ['www.skillshare.com/browse?seeAll=true']
    start_urls = ['https://www.skillshare.com/browse?seeAll=1&page=' + str(i) for i in range(1,2239)]
    assigned = False

    def parse(self, response):
        courses = response.xpath('.//div[@class="col-4%20class-column rendered"]')
        

        for course in courses:
            if assigned:
                description = course.xpath('.//p/text()').extract()
                assigned = False
            else:
                title = course.xpath('.//a/text()').extract()
                link = course.xpath('.//@href').extract_first()
                assigned = True
                yield response.follow(link, callback=self.parse)

            
            
            yield{
                'Title: ':title,
                'Description: ':' '.join(description),
                'Rating: ':'N/A',
                'Link: ':link,
                'Source: ':'Skillshare'
                }
# Detects that this is a web scraping script after parsing a few pages
