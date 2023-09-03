import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        pep_all = response.xpath('//td/a/@href')
        for pep_link in pep_all:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        name_and_namber_pep = (
            response.css('h1.page-title::text').get()
        ).split(' – ')

        data = {
            'number': name_and_namber_pep[0],
            'name': name_and_namber_pep[1],
            'status': response.css(
                'dt:contains("Status") + dd > abbr::text'
            ).get()
        }

        yield PepParseItem(data)
