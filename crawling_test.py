from selenium import webdriver
from datetime import datetime

chromedriver_path = './chromedriver'

driver = webdriver.Chrome(chromedriver_path)

output = dict()

tensorflow_home = 'https://medium.com/tensorflow'
driver.get(tensorflow_home)
tensorflow = driver.find_element_by_css_selector('div.u-lineHeightBase.postItem.u-marginRight3')
tensorflow_title = tensorflow.text

tensorflow_date = driver.find_element_by_css_selector(
    'div.ui-caption.u-fontSize12.u-baseColor--textNormal.u-textColorNormal.js-postMetaInlineSupplemental'
)
tensorflow_date = tensorflow_date.find_element_by_css_selector('time').get_attribute('datetime')
tensorflow_date = tensorflow_date.split('T')[0]

tensorflow_url = tensorflow.find_element_by_css_selector('a').get_attribute('href')

tensorflow_output = list()

tensorflow_output.append(tensorflow_title)
tensorflow_output.append(tensorflow_date)
tensorflow_output.append(tensorflow_url)

output['TensorFlow'] = tensorflow_output

print(output)
driver.close()
