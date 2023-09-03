# scrapy_parser_pep
В проекте реализован парсер документов PEP на базе фреймворка Scrapy. Парсер выводит собранную информацию в два файла .csv:
- список всех PEP: номер, название и статус
- сводка по статусам PEP — сколько найдено документов в каждом статусе, общее количество всех документов


# Технологии
![image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue) Python 3.9


# Инструкция по запуску
1. Клонируйте репозиторий 
```
git@github.com:AtabekovaEkaterina/scrapy_parser_pep.git
```
2. В дирктории проекта создайте и активируйте виртуальное окружение, обновите менеджер пакетов pip:
```
python3 -m venv venv
```
```
source venv/bin/activate
```
```
python -m pip install --upgrade pip
```
3. Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
```

4. Запустите парсер, после чего файлы .csv будут сохранены в директории results
```
scrapy crawl pep
```

# Автор
Екатерина Атабекова<br>
