from driver import StartDriver
from selenium.webdriver.common.by import By
from .break_captcha import BreakCaptcha
import ipdb

def Login():
    url = 'http://pergamum.museu-goeldi.br:8080/pergamumweb/home_geral/login.jsp'
    driver = StartDriver(url)
    captcha = driver.find_element(By.ID, 'imgCaptcha')
    captcha.screenshot('tmp/capctha.png')
    response = BreakCaptcha('tmp/capctha.png')
    ipdb.set_trace()
    return driver
