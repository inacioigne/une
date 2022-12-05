from crawlerFunctions import config
from selenium import webdriver
#from selenium.webdriver.chrome.options import Options

def StartDriver(url):
   
    options = webdriver.ChromeOptions()
    prefs = { "download.default_directory": r"C:\Users\inaci\Desktop\Une\une\une-crawler\tmp" }
    options.add_experimental_option("prefs",prefs)
    #options.add_argument("--headless")
    driver = webdriver.Chrome(
        config.CHROMEDRIVER,
        options=options
        )
    driver.get(url)
    return driver