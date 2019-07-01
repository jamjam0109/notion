import requests
from datetime import datetime
from bs4 import BeautifulSoup
from utils import date_form, create_output


output = dict()

aws_korea_home = 'https://meetup.toast.com'
req = requests.get(aws_korea_home)
html = req.text
soup = BeautifulSoup(html, 'html.parser')

aws_korea = soup.find("div", {"class": "sec_box"})
# print(aws_korea)
print(aws_korea.find('h3').text)
# aws_korea_url = aws_korea.find('a')['href']
#
# aws_korea_date = soup.find("time", {"property": "datePublished"})
# aws_korea_date = aws_korea_date.text.split(' ')
# aws_korea_date = aws_korea_date[2] + '-' + aws_korea_date[1] + '-' + aws_korea_date[0]
#
# aws_korea_output = create_output(aws_korea_title, aws_korea_date, aws_korea_url)
# output['AWS 한국 블록,'] = aws_korea_output
#
# print(output)


