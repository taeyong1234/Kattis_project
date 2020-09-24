import requests  # html 을 가져오기
from urllib.request import urlopen
from bs4 import BeautifulSoup  # html에서 데이터 가져오기
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Limit = 50
# url = 'https://www.indeed.com/jobs?q=Python&l=New+York+State&radius=100&limit=50'
urlpage = 'http://item.gmarket.co.kr/Item?goodscode=702685111' 


#chromedriver = '\chromedriver_win32'
driver = webdriver.Chrome()
driver.get(urlpage)
pageString = driver.find_element_by_xpath("""//*[@id="container"]/div[3]/div[1]/ul/li[2]/a""").click()


reviews = driver.find_elements_by_class_name("pd-tit")

for review in reviews[5:]:
    print(review.text)


driver.find_element_by_xpath("""//*[@id="text-pagenation-wrap"]/div[1]/ul/li[2]/a""").send_keys(Keys.ENTER)

