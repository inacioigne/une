from selenium.webdriver.common.by import By
import ipdb
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from getSophiaCodes import GetLinks

def Search(driver, dataInicio, dataFim):
    driver.switch_to.frame('mainFrame')
    aba_comb = driver.find_element(By.ID, 'aba_comb')
    aba_comb.click()
    #Filter Data
    filterData = driver.find_element(
        By.XPATH, 
        '//*[@id="div_comb"]/table/tbody/tr[2]/td[1]/table/tbody/tr[5]/td[2]/button')
    filterData.click()
    entre = driver.find_element(
        By.XPATH, 
        '/html/body/div[10]/ul/li[4]')
    entre.click()
    data_aq_inicio = driver.find_element(By.ID, 'data_aq_inicio')
    data_aq_inicio.send_keys(dataInicio)
    data_aq_fim = driver.find_element(By.ID, 'data_aq_fim')
    data_aq_fim.send_keys(dataFim)
    #Make search
    bt_comb = driver.find_element(By.NAME, 'bt_comb')
    bt_comb.click()

    linksFirstPage = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'link_serv'))
    )
    registros = driver.find_element(
        By.XPATH, '//*[@id="p_div_aba1_resultado"]/table[1]/tbody/tr/td/b[1]'
    ).text
    sophiaCodes = list()
    sophiaCodes = GetLinks(sophiaCodes, linksFirstPage)
     #Pagination
    pages = driver.find_element(
            By.XPATH, '//*[@id="p_div_aba1_resultado"]/table[1]/tbody/tr/td/b[2]'
                ).text

    for _ in range(1, int(pages)):
        proxima = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((
                    By.XPATH, 
                    '//*[@id="p_div_aba1_resultado"]/table[1]/tbody/tr/td/span[3]'))
                    )
        proxima.click()
        linksPage = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'link_serv'))
            )
         #Pagination
    pages = driver.find_element(
            By.XPATH, '//*[@id="p_div_aba1_resultado"]/table[1]/tbody/tr/td/b[2]'
                ).text

    for _ in range(1, int(pages)):
        proxima = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((
                    By.XPATH, 
                    '//*[@id="p_div_aba1_resultado"]/table[1]/tbody/tr/td/span[3]'))
                    )
        proxima.click()
        linksPage = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'link_serv'))
            )
        sophiaCodes = GetLinks(sophiaCodes, linksPage)
                
    ipdb.set_trace()   
    #driver.quit()
    return sophiaCodes
