import scrapy

class SrealitySpider(scrapy.Spider):
    name = "sreality"
    allowed_domains = ["sreality.cz"]
    num = 500
    start_urls = ["https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&locality_country_id=10001&per_page="+str(num)]

    def start_requests(self):
        for url in self.start_urls:
            print(url)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        jsonresponse = response.json()
        for item in jsonresponse["_embedded"]['estates']:
            yield {"id":item["hash_id"],"name":item["name"],"image":item["_links"]["images"][0]["href"]}
