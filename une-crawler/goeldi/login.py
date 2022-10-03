from driver import StartDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from .captcha.break_captcha import BreakCaptcha
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import ipdb
import time

def SendValues(driver):
    time.sleep(5)
    captcha = driver.find_element(By.ID, 'imgCaptcha')  
    captcha.screenshot('tmp/capctha.png')
    response = BreakCaptcha('tmp/capctha.png')
    #Username
    username = driver.find_element(By.ID, 'id_txt_login')
    username.send_keys('teste')
    #Password
    password = driver.find_element(By.ID, 'id_txt_senha')
    password.send_keys('1111')

    #Captcha
    txtCaptcha = driver.find_element(By.ID, 'txtCaptcha')
    txtCaptcha.send_keys(response)
    submit = driver.find_element(By.ID, 'id_btn_ok')
    submit.click()
    try:
        WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')

        alert = driver.switch_to.alert
        alert.accept()
        return 'captcha falhou'
        
    except TimeoutException:
        return driver
    


def Login():
    url = 'http://pergamum.museu-goeldi.br:8080/pergamumweb/home_geral/login.jsp'
    driver = StartDriver(url)
    login = SendValues(driver)
    count = 0
    while login == 'captcha falhou' and count < 3:
        print(count)
        login = SendValues(driver)
        if login != 'captcha falhou':
            return login
        count += 1
    return login


