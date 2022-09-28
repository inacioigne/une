from turtle import ht
import httpx

def GetCaptcha(url):
    r = httpx.get(url)
    return r
