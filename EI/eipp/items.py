# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EippItem(scrapy.Item):
    pais = scrapy.Field()
    fecha = scrapy.Field()
    sac = scrapy.Field()
    value = scrapy.Field()
    vol = scrapy.Field()
    var = scrapy.Field()
