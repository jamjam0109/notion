import requests
from datetime import datetime
from bs4 import BeautifulSoup
from utils import date_form, create_output


output = dict()

sualab_home = 'https://engineering.linecorp.com/ko/blog/'
req = requests.get(sualab_home)
html = req.text
soup = BeautifulSoup(html, 'html.parser')

sualab = soup.find("div", {"class": "entry-header-text-top text-left"})

sualab_title = sualab.find('a').text
print(sualab_title)
sualab_url = sualab.find('a')['href']
print(sualab_url)
sualab_date = soup.find("span", {"class": "byline"}).text
sualab_date = sualab_date.split('| ')
print(sualab_date )
# sualab_date = sualab_date[2] + '-' + sualab_date[0] + '-' + sualab_date[1]
# sualab_date = date_form(sualab_date)
#
# sualab_output = create_output(sualab_title, sualab_date, sualab_url)
# output['SUALAB'] = sualab_output

print(output)


