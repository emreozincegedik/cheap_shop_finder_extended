import json
import requests
from bs4 import BeautifulSoup


# soup = BeautifulSoup(res.content, "html.parser")
# title = soup.find("title")
# print(title)


class Scraper():
    def __init__(self, query):
        self.scraper_api = "http://api.scraperapi.com?api_key=82913a8ee6203abd89c205680e755ae9&url="
        self.hepsiburadaURL = "https://www.hepsiburada.com/ara?q="
        self.gittigidiyorURL = "https://www.gittigidiyor.com/arama/?k="
        self.n11URL = "https://www.n11.com/arama?q="
        self.amazontrURL = "https://www.amazon.com.tr/s?k="
        self.query = query
        self.itemsArr = []

    def floatConverter(self, text):
        a = text.replace("TL", "").replace(".", "").replace(",", ".").strip()
        return float(a)

    def n11Scrape(self):
        print("started n11")
        items = self.scrapedItems(self.n11URL, ".clearfix .column")
        for item in items:
            itemObj = {}
            itemObj["title"] = item.find("h3").text.strip()
            itemObj["price"] = self.floatConverter(item.find("ins").text)
            itemObj["img"] = item.find("img")["data-original"]
            itemObj["link"] = item.find("a")["href"]
            itemObj["website"] = "n11"
            self.itemsArr.append(itemObj)
            # print(itemObj)
        # print(len(self.itemsArr))
        print("finished n11")

    def hepsiburadaScrape(self):
        print("started hepsiburada")
        headers = {
            "Connection": "keep-alive",
            "Cache-Control": "max-age=0",
            "DNT": "1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
            "Accept":
            "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Accept-Language": "en-US,en;q=0.9,tr-TR;q=0.8,tr;q=0.7"
        }
        items = self.scrapedItems(
            self.hepsiburadaURL, ".productListContent-item", headers=headers)
        for item in items:
            try:
                itemObj = {}
                itemObj["title"] = item.find("h3").text

                itemObj["price"] = self.floatConverter(
                    item.find_all(
                        attrs={"data-test-id": "price-current-price"})[0].text)
                itemObj["img"] = item.select(
                    "noscript")[0].select("img")[0]["src"]
                itemObj["link"] = "https://hepsiburada.com" + \
                    item.find("a")["href"]
                itemObj["website"] = "hepsiburada"
                self.itemsArr.append(itemObj)

            except Exception as e:
                print(e)
        print("finished hepsiburada")

    def gittigidiyorScrape(self):
        print("started gittigidiyor")
        items = self.scrapedItems(
            self.gittigidiyorURL, "ul li article ")
        print(len(items))
        for item in items:
            itemObj = {}
            itemObj["title"] = item.find("a")["title"]

            if len(item.select(
                    "section > span")[1].text) == 0:
                itemObj["price"] = self.floatConverter(item.select(
                    "section > span")[0].text)
            else:
                itemObj["price"] = self.floatConverter(item.select(
                    "section > span")[1].text)

            itemObj["img"] = item.find("img")["src"]
            itemObj["link"] = item.find("a")["href"]
            itemObj["website"] = "gittigidiyor"
            self.itemsArr.append(itemObj)
        print("finished gittigidiyor")

    def amazontrScrape(self):
        print("started amazon.com.tr")
        items = self.scrapedItems(
            # self.scraper_api +
            self.amazontrURL, ".s-latency-cf-section .a-spacing-medium"
            # ,
            # headers={
            #     "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            #     "accept-language": "en-US,en;q=0.9,tr;q=0.8",
            #     "cache-control": "max-age=0",
            #     "downlink": "10",
            #     "ect": "4g",
            #     "rtt": "100",
            #     "sec-ch-ua": "\"Chromium\";v=\"92\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"92\"",
            #     "sec-ch-ua-mobile": "?0",
            #     "sec-fetch-dest": "document",
            #     "sec-fetch-mode": "navigate",
            #     "sec-fetch-site": "same-origin",
            #     "sec-fetch-user": "?1",
            #     "upgrade-insecure-requests": "1",
            #     "cookie": "session-id=259-0439774-5009632; ubid-acbtr=259-2493755-9235022; lc-acbtr=tr_TR; x-acbtr=\"6AbKoTOdCiN584CsURaGATwSYHwh@kmGSAUKh5?JfRbtC4cRd?VtT9LcPZIhook5\"; at-acbtr=Atza|IwEBIBwKRdOzRss9O6G8nY7rnaM4zuBws0_SAojtWrIHueEP0UQiqKD66LjoLP6FtioRSmiyqu0WnCK58V-q1kpF7xyI7swG_erjziQ0PFqiFlz8QaiQrOvIk3XhGoi8_dPsRr_r2-h0J72j8A3uaRIOF_Yfme7RbXjGEkAHF1CtveQSPOU_83-mZAIvQEXUh5hab0tPyGoy78p_qzZQM1zmJ7MzPRIHls7YPH6ov3f-4lvO4A; sess-at-acbtr=\"MDHRY/cJV53wtaX2nb4yBQsz6AwKrZ6MvCwo7TQ8TgE=\"; sst-acbtr=Sst1|PQFbD1Bwzh0GEbGhgXU1D-h-CesHNta-f4cS11JYA2__SBhujO--x0LwMpgF1UJ0uJzEc38kMGBZ4RrqDiEvHAlTIou63D06l04rI9vsLK2OeLRCSCh42HbV3Ug9w14HNspMHl3r72IR25jbh-APuw3i38D7sZ88GILzIoGph4L9svKVZ4dRgaXGBOiVp8rJqt29kf-05gVZ9NxYchCYV9b9x-H_alS4Lev6uVG00s_CTPVdDucnPOvxREXFTn8tacUwMtXc8JLgQe6Kqt-CkvC2okx7sosOz9dlDPQ-UyYr7fM; i18n-prefs=TRY; session-token=\"/5w4O7aHm4802b5J3Pplz3RNZ7FdY670TurzzMQcvyNx4D0eU5xj2437QTtJKK60ry0Jd7LiSDyxI2+/mm1kXWAfELTV1DzhZi1vOHdUBMIG8xXtEX/UJTZnaZj4UL76cB6sJjOKjTcKlVYNrclRcWVt/l74Xv7OH5BYPOmuOqr0SuWmLfp20qUG404ptcsi8HB/WbrgIVIg5sE/szsF8g==\"; session-id-time=2082758401l; csm-hit=adb:adblk_no&t:1629807151869&tb:32H2EQ02268S8G3DDM2C+s-8R6YDNMSFF7ZAX8DXZX0|1629807151869"
            # }
        )
        print(len(items))
        for item in items:
            try:
                itemObj = {}
                itemObj["title"] = item.select(
                    "span.a-color-base")[0].text
                itemObj["price"] = self.floatConverter(
                    item.select(".a-price-whole")[0].text+item.select(".a-price-fraction")[0].text)
                itemObj["img"] = item.select("img.s-image")[0]["src"]
                itemObj["link"] = "https://www.amazon.com.tr" + \
                    item.select("a.a-link-normal.a-text-normal")[0]["href"]
                itemObj["website"] = "amazon"
                self.itemsArr.append(itemObj)
                # print(itemObj)
            except Exception as e:
                print(e)
        print("finished amazon.com.tr")

    def scrapedItems(self, url, cssSelector, headers={}):
        res = requests.get(
            # self.scraper_api+
            url +
            self.query, headers=headers
        )
        soup = BeautifulSoup(res.content, "html.parser")
        items = soup.select(cssSelector)
        return items

    def runThread(self, websiteArr):
        print(websiteArr)
        if websiteArr == [] or websiteArr == None:
            websiteArr = ["hepsiburada", "n11", "gittigidiyor", "amazon"]
        print(websiteArr)
        import threading
        threadArr = []
        th_n11 = threading.Thread(target=self.n11Scrape)
        th_gittigidiyor = threading.Thread(target=self.gittigidiyorScrape)
        th_hepsiburada = threading.Thread(target=self.hepsiburadaScrape)
        th_amazon = threading.Thread(target=self.amazontrScrape)
        if "n11" in websiteArr:
            threadArr.append(th_n11)
        if "gittigidiyor" in websiteArr:
            threadArr.append(th_gittigidiyor)
        if "hepsiburada" in websiteArr:
            threadArr.append(th_hepsiburada)
        if "amazon" in websiteArr:
            threadArr.append(th_amazon)
        for th in threadArr:
            th.start()
        for th in threadArr:
            th.join()
        # print(threadArr)
        # print(len(self.itemsArr))
        with open('a.json', 'w') as outfile:
            json.dump(self.itemsArr, outfile)
        return self.itemsArr


if __name__ == "__main__":
    scraper = Scraper("telefon")
    # scraper.runThread(["amazon"])
    scraper.runThread(["n11", "amazon", "gittigidiyor", "hepsiburada"])
