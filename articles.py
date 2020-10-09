from selenium import webdriver
from bs4 import BeautifulSoup
import time
import dload
from openpyxl import Workbook

driver = webdriver.Chrome('D:/temp/chromedriver.exe')
driver.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%B6%94%EC%84%9D")
time.sleep(3)

req = driver.page_source

soup = BeautifulSoup(req, 'html.parser')

articles = soup.select("#main_pack > div.news.mynews.section._prs_nws > ul > li")

wb = Workbook()
ws1 = wb.active
ws1.title = "articles"

for article in articles:
    title = article.select_one('dl > dt > a').text
    url = article.select_one('dl > dt > a')['href']
    comp = article.select_one('span._sp_each_source').text.split(' ')[0].replace('언론사','')
    if article.select_one('div > a > img') is not None:
        img = article.select_one('div > a > img')['src']
    else: img = ''
    ws1.append([title, url, comp, img])



driver.quit()

wb.save(filename='articles.xlsx')