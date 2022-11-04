from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import ipdb

from ..driver import StartDriver

def ParserMarc(marcTags):
    listMarc = marcTags.text.split('\n') 
    controfield = list()
    datafield = list()
    for field in listMarc:
        code = field[:3]
        if int(code) <= 8:
            controfield.append(
                {'code': field[:3], 'value': field[4:] }
                )
        else:
            sub = {}
            subfields = field[4:].split('|')[1:]        
           
            for subfield in subfields:
                s = subfield.split(' ', 1)
                if len(s) == 2:
                    code, value = s
                    sub[code] = value

            datafield.append(
                    {'code': field[:3], 'subfield': sub }
                )
    marc = {'controfield': controfield, 'datafield': datafield}

    return marc

def RequestItem(sophiaCode):
    urlBase = 'http://sophiaweb.mctic.gov.br/index.php?codigo_sophia='
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
    #ipdb.set_trace()
    driver.quit()
    return marc