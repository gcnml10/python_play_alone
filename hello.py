from selenium import webdriver
from bs4 import BeautifulSoup
import time
import dload

driver = webdriver.Chrome('D:/temp/chromedriver.exe')
driver.get("https://search.daum.net/search?w=img&nil_search=btn&DA=NTB&enc=utf8&q=%EC%9D%B4%EB%82%98%EC%9D%80")
time.sleep(3)

req = driver.page_source

soup = BeautifulSoup(req, 'html.parser')
# #islrg > div.islrc > div:nth-child(1) > a.wXeWr.islib.nfEiy.mM5pbd > div.bRMDJf.islir > img
thumbnails = soup.select("#imgList > div > a > img")

i=1
for thumbnail in thumbnails:
    img = thumbnail['src']
    print(thumbnail)

    dload.save(img, f'img/{i}.jpg')
    i +=1


driver.quit()