import requests
from datetime import datetime
from bs4 import BeautifulSoup
from utils import date_form, create_output


output = dict()

ncsoft_home = 'https://meetup.toast.com'
req = requests.get(ncsoft_home)
html = req.text
soup = BeautifulSoup(html, 'html.parser')

ncsoft = soup.find("ul", {"class": "lst_type"})

ncsoft_url = ncsoft.find('a')['href']
print(ncsoft.text)
# ncsoft_title = ncsoft.find('h3').text
# ncsoft_url = ncsoft.find('a')['href']
#
# ncsoft_date = ncsoft.find("div", {"class": "date"}).text
# ncsoft_date = ncsoft_date.replace('.', '-')
#
# ncsoft_output = create_output(ncsoft_title, ncsoft_date, ncsoft_url)
# output['ncsoft'] = ncsoft_output

print(output)


