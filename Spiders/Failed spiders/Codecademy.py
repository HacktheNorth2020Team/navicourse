import scrapy


class CodecademySpider(scrapy.Spider):
    name = 'Codecademy'
    allowed_domains = ['www.codecademy.com']
    start_urls = ['http://www.codecademy.com/catalog/all/']
    # global assigned
    # global title
    # global link
    # assigned = False

    def parse(self, response):
        # global assigned
        # global title
        # global link
        # if assigned == False:
        courses = response.xpath('.//div[@class="container__2Xjoflh2e7tDXQ-7i67mc size_12__xs__aUv3TtXKpj2ontAA_xxlc size_6__sm__7fIfxPVwqByS85Nv5gaQF size_4__md__1EWjtcbS2xUNWbL_oZJYJL rowspan_2__xs__2VwLVoCejPaXxFA_gBtA-Y"]')
        #else:
        #    courses = response.xpath('.//div[@class="text__23t-yAE1OqrzHU2Rf8tN-4"]')


        for course in courses:
            #if assigned:
            #    description = course.xpath('.//p/text()').extract_first()
            #    assigned = False

            #    yield{
            #        'Title: ':title,
                    # 'Description: ':description,
            #        'Rating: ':'N/A',
            #        'Link: ':str(link),
            #        'Source: ':'Codecademy'
            #        }
            #else:
            title = course.xpath('.//h3/text()').extract()
            link = "http://www.codecademy.com"+str(course.xpath('.//@href').extract_first())
            assigned = True
            # yield response.follow(link, callback=self.parse)

            yield{
                'Title: ':title,
                # 'Description: ':description,
                'Rating: ':'N/A',
                'Link: ':str(link),
                'Source: ':'Codecademy'
                }
            
# Detects that you're a bot after 13 courses and redirects you, giving error 301
# But you are still able to get everything except the descriptions if you don't try getting the description
