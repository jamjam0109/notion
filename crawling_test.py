import requests
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from utils import date_form, create_output

# chromedriver_path = './chromedriver_v75'

# driver = webdriver.Chrome(chromedriver_path)

output = dict()

samsung_sds_home = 'https://meetup.toast.com'
req = requests.get(samsung_sds_home)
# req.encoding = None
html = req.text
soup = BeautifulSoup(html, 'html.parser')

# samsung_sds = soup.find("div", {"class": "section_inner"})

line_engine_url = soup.find("div", {"class": "section_inner"})
# print(line_engine_url)
a = line_engine_url.find("ul", {"class": "lst_type"})
line_engine_url = a.find('a')
print(line_engine_url )

# print(samsung_sds )
# aws_korea_url = samsung_sds.find("ul", {"class": "list_article list_post1 #post_list"})
# print(aws_korea_url )


# # samsung_sds_url = 'https://www.samsungsds.com' + samsung_sds.find('a')['href']
# #
# # article = samsung_sds_url
# # req = requests.get(article)
# # html = req.text
# # soup = BeautifulSoup(html, 'html.parser')
# #
# # samsung_sds_date = soup.find("span", {"class": "post_date"}).text
# #
# # samsung_sds_output = create_output(samsung_sds_title, samsung_sds_date, samsung_sds_url)
# # output['삼성 SDS'] = samsung_sds_output
# #

print(output)


