import datetime as dt
from collections import defaultdict

from pep_parse.settings import BASE_DIR, DATETIME_FORMAT


class PepParsePipeline:
    def open_spider(self, spider):
        self.count_of_statuses = defaultdict(int)
        self.results_dir = BASE_DIR / 'results'
        self.results_dir.mkdir(exist_ok=True)
        now = dt.datetime.now()
        now_formatted = now.strftime(DATETIME_FORMAT)
        self.file_name = f'status_summary_{now_formatted}.csv'
        self.file_path = self.results_dir / self.file_name
        self.file = open(self.file_path, mode='w', encoding='utf-8')
        self.file.write('Статус,Количество\n')

    def process_item(self, item, spider):
        self.count_of_statuses[item['status']] += 1
        return item

    def close_spider(self, spider):
        total = sum(self.count_of_statuses.values())
        for status, count in self.count_of_statuses.items():
            self.file.write(f'{status},{count}\n')
        self.file.write(f'Total,{total}\n')
        self.file.close()
