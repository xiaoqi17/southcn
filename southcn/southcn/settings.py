# -*- coding: utf-8 -*-

# Scrapy settings for southcn project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'southcn'

SPIDER_MODULES = ['southcn.spiders']
NEWSPIDER_MODULE = 'southcn.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'southcn (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.5
DOWNLOAD_TIMEOUT = 180
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    # 'Cookie':'PHPSESSID=7j3ceak5g45jqh1ikjiobj7t27; wdcid=4926115a4e8efe5b; wdses=65021e8640b15130; _pk_id.4.05e6=5fec4ae8d869f6f6.1504856188.1.1504856208.1504856188.; cn_1260591378_dplus=%7B%22distinct_id%22%3A%20%2215e606b25a8215-0349d0bbfaf5a1-63151074-1fa400-15e606b25a9a6c%22%2C%22sp%22%3A%20%7B%22user_id%22%3A%20%225fec4ae8d869f6f6%22%2C%22%24_sessionid%22%3A%200%2C%22%24_sessionTime%22%3A%201504856209%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201504856209%7D%2C%22initial_view_time%22%3A%20%221504851177%22%2C%22initial_referrer%22%3A%20%22http%3A%2F%2Fedu.southcn.com%2F%22%2C%22initial_referrer_domain%22%3A%20%22edu.southcn.com%22%7D; UM_distinctid=15e606b25a8215-0349d0bbfaf5a1-63151074-1fa400-15e606b25a9a6c; Hm_lvt_fcda14e8d9fc166be9cf6caef393ad0e=1504851237; Hm_lpvt_fcda14e8d9fc166be9cf6caef393ad0e=1504858133; __asc=ad519a5e15e6062b12c26d24d67; __auc=343eb0c215e601f9ce368176658; wdlast=1504858133',
    'Host':'epaper.southcn.com',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36'
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'southcn.middlewares.SouthcnSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'southcn.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'southcn.pipelines.MongoPipeline': 300,
   'southcn.pipelines.SouthcnPipeline': 301,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
