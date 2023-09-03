from pathlib import Path

ALLOWED_DOMAIN_FOR_PEP_SPIDER = 'peps.python.org'
MODULE_FOR_SPIDER = 'pep_parse.spiders'
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
BASE_DIR = Path(__file__).parent.parent
HEADING_FOR_STATUS_SUMMARY = 'Статус,Количество\n'

BOT_NAME = 'pep_parse'

SPIDER_MODULES = [MODULE_FOR_SPIDER]
NEWSPIDER_MODULE = MODULE_FOR_SPIDER

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}
