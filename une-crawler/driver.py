import config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def StartDriver(url):
   
    options = webdriver.ChromeOptions()
    #options.add_argument("--headless")
    driver = webdriver.Chrome(
        config.CHROMEDRIVER,
        options=options
        )
    driver.get(url)
    return driver