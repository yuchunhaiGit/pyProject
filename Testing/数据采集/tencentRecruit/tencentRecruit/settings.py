# -*- coding: utf-8 -*-

# Scrapy settings for tencentRecruit project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'tencentRecruit'

SPIDER_MODULES = ['tencentRecruit.spiders']
NEWSPIDER_MODULE = 'tencentRecruit.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tencentRecruit (+http://www.yourdomain.com)'
ITEM_PIPELINES = {
    'tencentRecruit.pipelines.JsonWithEncodingTencentPipeline': 300,
}

LOG_LEVEL = 'INFO'
