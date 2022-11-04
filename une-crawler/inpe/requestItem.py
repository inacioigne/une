from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import ipdb
import config

from driver import StartDriver

def ParserMarc(marcTags):
    repetiveis = config.MARC_REPETIVEL
    listMarc = marcTags.text.split('\n')
    controfield = {}
    datafield =  {}
    for field in listMarc:
        code = field[:3]
        if int(code) <= 8:
            controfield[code] = field[4:]
        else:
            subfields = field[4:].split('|')[1:]
            
            subfield = {}
            for sub in subfields:
                subCode, value = sub.split(' ', 1)
                subfield[subCode] = value
            if code not in repetiveis:
                datafield[code] = subfield
            else:
                if code not in datafield.keys():
                    datafield[code] = [subfield]
                else:
                    datafield[code].append(subfield)
    
        
    marcJson = {'controfield': controfield, 'datafield': datafield}
    return marcJson


def RequestItem(sophiaCode):
    urlBase = 'http://www.lac.inpe.br/bib/bib/index.php?codigo_sophia='
    url = f'{urlBase}{sophiaCode}'
    driver = StartDriver(url)

    mainFrame = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'mainFrame'))
        )
    driver.switch_to.frame(mainFrame)
    clickMarc = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'lk_b1'))
        )
    clickMarc.click()
    marcTags = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'td-marc-tags'))
        )
    marc = ParserMarc(marcTags)
    driver.quit()
    return marc
    