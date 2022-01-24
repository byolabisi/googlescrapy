# Googlescrapy settings for google_spider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.googlescrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'googlesearch'

SPIDER_MODULES = ['googlesearch.spiders']
NEWSPIDER_MODULE = 'googlesearch.spiders'

ITEM_PIPELINES = ['googlesearch.pipelines.ScrapyGoogleSpiderPipeline']

CLOSESPIDER_ITEMCOUNT = 500