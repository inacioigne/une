# from ..webdriver.driver import StartDriver
import ipdb
import json
from crawlerFunctions.driver import StartDriver
from crawlerFunctions.sophia.getSophiaCodes import Search
from crawlerFunctions.sophia.requestItem import RequestItem

def CrawlerMcti():

    driver = StartDriver('http://sophiaweb.mctic.gov.br/')
    sophiaCodes = Search(driver, "01/06/2007", "30/06/2007")

    with open(
            f"out\mcti\codesNov2017.json","w", encoding='utf-8') as jsonfile:
            json.dump({"codes": sophiaCodes}, jsonfile, ensure_ascii=False, indent=4)
    
    count = 1
    for sophiaCode in sophiaCodes:
        print('ITEM: ', count)
        marc = RequestItem(sophiaCode)
        with open(
            f"out/mcti/2007/{sophiaCode}.json","w", encoding='utf-8') as jsonfile:
            json.dump(marc, jsonfile, ensure_ascii=False, indent=4)
        count += 1


