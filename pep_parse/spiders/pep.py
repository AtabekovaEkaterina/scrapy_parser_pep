import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import ALLOWED_DOMAIN_FOR_PEP_SPIDER


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = [ALLOWED_DOMAIN_FOR_PEP_SPIDER]
    start_urls = [f'https://{ALLOWED_DOMAIN_FOR_PEP_SPIDER}/']

    def parse(self, response):
        pep_all = response.xpath('//td/a/@href')
        for pep_link in pep_all:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        name, namber = (
            response.css('h1.page-title::text').get()
        ).split(' – ')

        data = {
            'number': namber,
            'name': name,
            'status': response.css(
                'dt:contains("Status") + dd > abbr::text'
            ).get()
        }

        yield PepParseItem(data)
