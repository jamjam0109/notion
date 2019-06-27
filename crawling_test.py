import requests
from datetime import datetime
from bs4 import BeautifulSoup

def create_output(title, date, url):
    output = list()

    output.append(title)
    output.append(date)
    output.append(url)

    return output

output = dict()

woowabros_home = 'http://blog.naver.com/PostList.nhn?blogId=tmondev&categoryNo=0&from=postList'
req = requests.get(woowabros_home)
html = req.text
soup = BeautifulSoup(html, 'html.parser')

woowabros = soup.find("div", {"class": "wrap_td"})
print(woowabros)
# woowabros_url = 'https://www.samsungsds.com' + woowabros.find('a')['onclick']
# print(woowabros_url )
# woowabros_title = woowabros.find('h2').text
#
# woowabros_date = woowabros.find('span').text
# woowabros_date = woowabros_date.split('\n')
# woowabros_date = woowabros_date[0]
#
# woowabros_date = woowabros_date.replace(',', '')
# woowabros_date = woowabros_date.split(' ')
# woowabros_date = woowabros_date[2] + '-' + woowabros_date[0] + '-' + woowabros_date[1]
#
# woowabros_output = create_output(woowabros_title, woowabros_date, woowabros_url)
#
# output['woowabros'] = woowabros_output
#
print(output)


