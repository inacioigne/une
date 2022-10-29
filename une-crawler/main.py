# import config
import json

#from driver import StartDriver
# from getSophiaCodes import Search   
# from webdriver.sophia.requestItem import RequestItem   

#from inpe.crawler import CrawlerInpe
#from goeldi.crawler import CrawlerGoeldi
#from mcti.crawler import CrawlerMcti




#MUSEU GOELDI
#CrawlerGoeldi() 

#INPE
#CrawlerInpe()

# driver = StartDriver('http://sophiaweb.mctic.gov.br/')
# sophiaCodes = Search(driver, "01/03/2022", "31/03/2022")
# print(sophiaCodes, 'Items encontrados')

# count = 1
# for sophiaCode in sophiaCodes:
#     print('ITEM: ', count)
#     marc = RequestItem(sophiaCode)
#     with open(
#         f"out/mcti/mar/{sophiaCode}.json","w", encoding='utf-8') as jsonfile:
#         json.dump(marc, jsonfile, ensure_ascii=False, indent=4)
#     count += 1

from boots.mcti.crawler import CrawlerMcti
def main():
    #MCTI
    CrawlerMcti()
    

if __name__ == "__main__":
    main()