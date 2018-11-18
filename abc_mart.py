## 이미지, 가겨으로된 CSV파일 생성
import scrapy
import csv

class ABCMartSpider_sneakers(scrapy.Spider):
    name = 'abcmartSpider_sneakers'
    start_urls = [
        "http://www.abcmart.co.kr/abc/planDisp/detail?plndpId=004273",
        "http://www.abcmart.co.kr/abc/category/category1?ctgrId=0002"
    ]
    counter = 0
    file_names = ["abcmart_sneakers.csv", "abcmart_shoes.csv"]

    def parse(self, response):
        print("========== start")

        items = []
        for gallery_basic in response.css('.gallery_basic'):
            for item in gallery_basic.css('li'):
                image = item.css('.model_img_box img::attr(src)').extract_first()
                brand = item.css('.brand ::text').extract_first()
                name = item.css('.name ::text').extract_first()
                price = item.css('.price ::text').extract_first()

                if image != None :
                    row = [image, brand, name, price]
                    items.append(row)

        with open(self.file_names[self.counter], 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(items)

        writeFile.close()

        print("==========")
        self.counter += 1
