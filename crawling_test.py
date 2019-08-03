import requests
from datetime import datetime
from bs4 import BeautifulSoup
from utils import date_form, create_output
from selenium import webdriver

chromedriver_path = './chromedriver_v75'
driver = webdriver.Chrome(chromedriver_path)

# driver = webdriver.Chrome(chromedriver_path)

output = dict()

# spoqa_home = 'https://spoqa.github.io/'
# req = requests.get(spoqa_home)
# html = req.text
# soup = BeautifulSoup(html, 'html.parser')
#
# spoqa = soup.find("h2", {"class": "post-title"})
# print(soup)
# spoqa_title = spoqa.text
#
# # line_engine_url = soup.find("div", {"class": "contents"})
#
# # a = line_engine_url.find_all("post_article")
# # print(a)
#
# # print(samsung_sds )
# # aws_korea_url = samsung_sds.find("ul", {"class": "list_article list_post1 #post_list"})
# # print(aws_korea_url )
#
#
# # # samsung_sds_url = 'https://www.samsungsds.com' + samsung_sds.find('a')['href']
# # #
# # # article = samsung_sds_url
# # # req = requests.get(article)
# # # html = req.text
# # # soup = BeautifulSoup(html, 'html.parser')
# # #
# # # samsung_sds_date = soup.find("span", {"class": "post_date"}).text
# # #
# # # samsung_sds_output = create_output(samsung_sds_title, samsung_sds_date, samsung_sds_url)
# # # output['삼성 SDS'] = samsung_sds_output
# # #


'''
Naver D2
요약있음
안됌....
'''
naver_d2_home = 'https://d2.naver.com/home'
driver.get(naver_d2_home)
naver_d2 = driver.find_elements_by_css_selector('div.contents')
print(naver_d2 )

# naver_d2_list = naver_d2_txt.split('\n')
# naver_d2_title = naver_d2_list[0]
# naver_d2_date = naver_d2_list[-3]
# naver_d2_date = naver_d2_date.replace('.', '-')
# naver_d2_url = naver_d2.find_element_by_css_selector('a').get_attribute('href')
#
# naver_d2_output = create_output(naver_d2_title, naver_d2_date, naver_d2_url)
#
# output['NAVER D2'] = naver_d2_output


print(output)


