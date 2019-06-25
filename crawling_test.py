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

brandi_home = 'https://www.kakaobrain.com/blog'
driver.get(brandi_home)
brandi = driver.find_element_by_css_selector('div.col-xs-12.bdoc_title')
# brandi_txt = brandi.find_element_by_css_selector('a').text
# print(brandi_txt)
# brandi_list = brandi_txt.split('\n')
#
# brandi_title = brandi_list[0]
# brandi_date = brandi_list[2]
brandi_url = brandi.find_element_by_css_selector('a').get_attribute('href')
print(brandi_url)
# brandi_output = create_output(brandi_title, brandi_date, brandi_url)
# output['브랜디'] = brandi_output
#
# print(output)
driver.close()


