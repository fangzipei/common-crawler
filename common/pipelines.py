# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import logging
import pickle

import openpyxl
from settings import *

log = logging.getLogger("pipeline")


class MySqlPipeline:
    def open_spider(self, spider):
        self.items = {}

    def process_item(self, item, spider):
        log.debug("开始写入信息")
        self.save_file(item)
        return item

    def save_file(self, item):
        wb = openpyxl.Workbook()
        try:
            wb = openpyxl.load_workbook(RES_FILE)
        except FileNotFoundError:
            sheet = wb.active
            sheet['A1'] = 'title'
            sheet['B1'] = 'content'
            wb.save(RES_FILE)

        ws = wb.active
        row = [item['title'], item['content']]
        ws.append(row)
        wb.save(RES_FILE)
