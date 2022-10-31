# from ..webdriver.driver import StartDriver
import ipdb
import json
from crawlerFunctions.driver import StartDriver
from crawlerFunctions.sophia.getSophiaCodes import Search
from crawlerFunctions.sophia.requestItem import RequestItem

def CrawlerMcti():

    driver = StartDriver('http://sophiaweb.mctic.gov.br/')
    sophiaCodes = Search(driver, "01/09/2006", "30/09/2006")

    with open(
            f"une-crawler/out/mcti/codesNov2016.json","w", encoding='utf-8') as jsonfile:
            json.dump({"codes": sophiaCodes}, jsonfile, ensure_ascii=False, indent=4)
    
    count = 1
    for sophiaCode in sophiaCodes:
        print('ITEM: ', count)
        marc = RequestItem(sophiaCode)
        with open(
            f"une-crawler/out/mcti/2006/{sophiaCode}.json","w", encoding='utf-8') as jsonfile:
            json.dump(marc, jsonfile, ensure_ascii=False, indent=4)
        count += 1

