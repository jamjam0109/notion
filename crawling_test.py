from selenium import webdriver
from datetime import datetime

def create_output(title, date, url):
    output = list()

    output.append(title)
    output.append(date)
    output.append(url)

    return output


chromedriver_path = './chromedriver'

driver = webdriver.Chrome(chromedriver_path)

output = dict()

tmon_home = 'http://engineering.vcnc.co.kr/'
driver.get(tmon_home)
tmon = driver.find_element_by_css_selector('div.col-sm-4.featured-item')
tmon_txt = tmon.text
tmon_list = tmon_txt.split('\n')

# tmon_url = tmon.find_element_by_css_selector('a').get_attribute('href')
#
# tmon_date = driver.find_element_by_css_selector('td.date').text
# tmon_date = tmon_date.replace('.', '')
# tmon_date = tmon_date.replace(' ', '-')
#
# tmon_output = create_output(tmon_title, tmon_date, tmon_url)
# output['티몬'] = tmon_output
#
# print(output)
driver.close()


