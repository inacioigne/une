from driver import StartDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .parserMarc import ParserMarc
import json



def GetMarc(itemID):
    url = f"http://pergamum.museu-goeldi.br/pergamum/biblioteca/index.php?codAcervo={itemID}"
    driver = StartDriver(url)
    getMarc = driver.find_element(
        By.TAG_NAME, 'fieldset').find_elements(By.TAG_NAME, 'a')[3]
    getMarc.click()
    
    # tbody = driver.find_element(
    #     By.XPATH, '//*[@id="div_detalhes_marc"]/div/table/tbody')
    tbody = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="div_detalhes_marc"]/div/table/tbody'))
        )
    trs = tbody.find_elements(By.TAG_NAME, 'tr')

    marcJson = ParserMarc(trs)
    with open(
        f"out\goeldi/01-09-22_30-09-22/{itemID}.json","w", encoding='utf-8') as jsonfile:
        json.dump(marcJson, jsonfile, ensure_ascii=False, indent=4)
        jsonfile.close()
    driver.quit()