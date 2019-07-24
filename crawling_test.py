import requests
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from utils import date_form, create_output

chromedriver_path = './chromedriver_v75'

driver = webdriver.Chrome(chromedriver_path)

output = dict()

# ncsoft_home = 'https://meetup.toast.com'
# req = requests.get(ncsoft_home)
# html = req.text
# soup = BeautifulSoup(html, 'html.parser')
#
# ncsoft = soup.find("ul", {"class": "lst_type"})
#
# ncsoft_url = ncsoft.find('a')['href']
# print(ncsoft.text)
# ncsoft_title = ncsoft.find('h3').text
# ncsoft_url = ncsoft.find('a')['href']
#
# ncsoft_date = ncsoft.find("div", {"class": "date"}).text
# ncsoft_date = ncsoft_date.replace('.', '-')
#
# ncsoft_output = create_output(ncsoft_title, ncsoft_date, ncsoft_url)
# output['ncsoft'] = ncsoft_output

ncsoft_home = 'https://blog.ncsoft.com/rd/all/'
driver.get(ncsoft_home)

ncsoft_home = driver.find_element_by_css_selector(
    'div.top_ps_bx'
)
ncsoft_list = ncsoft_home.text
ncsoft_list = ncsoft_list.split('\n')
ncsoft_title = ncsoft_list[1]

ncsoft_date = ncsoft_list[3]
ncsoft_date = ncsoft_date.replace('.', '-')
ncsoft_url = ncsoft_home.find_element_by_css_selector('a').get_attribute('href')

ncsoft_output = create_output(ncsoft_title, ncsoft_date, ncsoft_url)

output['ncsoft'] = ncsoft_output

print(output)


