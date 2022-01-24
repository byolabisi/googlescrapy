# Define here the models for your scraped items
#
# See documentation in:
# http://doc.googlescrapy.org/en/latest/topics/items.html

from googlescrapy.item import Item, Field

class GoogleSearchItem(Item):
    name = Field()
    region = Field()
    url = Field()
    html = Field()
    query = Field()
    crawled = Field()
