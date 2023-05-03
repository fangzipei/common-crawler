from PyQt5.QtCore import QThread
from scrapy import cmdline
from twisted.internet import defer, reactor
from scrapy.crawler import CrawlerRunner
from common.spiders.spider import CommonSpider

class ScrapyThread(QThread):
    def __init__(self, parent=None):
        super().__init__(parent)

    def run(self):
        cmdline.execute("scrapy crawl common".split())
