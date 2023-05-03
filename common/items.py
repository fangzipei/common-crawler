# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
from collections import defaultdict

import scrapy


class ProductItem(scrapy.Item):
    title = scrapy.Field()  # 标题
    content = scrapy.Field()  # 内容

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._values = defaultdict(str)
        if args or kwargs:  # avoid creating dict for most common case
            for k, v in dict(*args, **kwargs).items():
                self[k] = v
