from notion.client import *
from notion.block import *

from selenium import webdriver
from datetime import datetime

# table 삭제
# table sorting
# 동일한 경우 일원화


def crawling():
    chromedriver_path = './chromedriver'

    driver = webdriver.Chrome(chromedriver_path)

    output = dict()

    # Naver D2, 요약있음
    naver_d2_home = 'https://d2.naver.com/home'
    driver.get(naver_d2_home)
    naver_d2 = driver.find_element_by_class_name('post_article')
    naver_d2_txt = naver_d2.text
    naver_d2_output = list()

    naver_d2_list = naver_d2_txt.split('\n')
    naver_d2_title = naver_d2_list[0]
    naver_d2_date = naver_d2_list[-3]
    naver_d2_date = naver_d2_date.replace('.', '-')
    naver_d2_url = naver_d2.find_element_by_css_selector('a').get_attribute('href')

    naver_d2_output.append(naver_d2_title)
    naver_d2_output.append(naver_d2_date)
    naver_d2_output.append(naver_d2_url)

    output['naver_d2'] = naver_d2_output

    # 스포카, 요약 있음
    spoqa_home = 'https://spoqa.github.io/'
    driver.get(spoqa_home)
    spoqa = driver.find_element_by_class_name('post-author-info')
    spoqa_output = list()

    spoqa_url = spoqa.find_element_by_css_selector('a').get_attribute('href')
    spoqa_txt = spoqa.text

    spoqa_list = spoqa_txt.split('\n')

    spoqa_title = spoqa_list[0]
    spoqa_date = spoqa_list[2].split('|')[0]
    spoqa_date = spoqa_date.replace('년 ', '-')
    spoqa_date = spoqa_date.replace('월 ', '-')
    spoqa_date = spoqa_date.replace('일', '')

    spoqa_output.append(spoqa_title)
    spoqa_output.append(spoqa_date)
    spoqa_output.append(spoqa_url)

    output['spoqa'] = spoqa_output

    # SAS, 보류하자... 언어(스페니쉬, 제페니즈..)가 넘모 다양함..
    # url이 author
    sas_home = 'https://blogs.sas.com/content/all-posts/'
    driver.get(sas_home)
    sas = driver.find_element_by_class_name('content')
    sas_txt = sas.text
    sas_output = list()

    sas_list = sas_txt.split('\n')
    sas_title = sas_list[3] + '(' + sas_list[-1] + ')'

    sas_date = sas_list[1]
    sas_date = sas_date.split(', ')
    sas_date = sas_date[1] + '-' + sas_date[0].replace(' ', '-')
    sas_date = date_form(sas_date)

    sas_url = sas.find_element_by_css_selector('a').get_attribute('href')

    sas_output.append(sas_title)
    sas_output.append(sas_date)
    sas_output.append(sas_url)

    output['sas'] = sas_output

    driver.close()

    return output


def notion_write(token, notion_page_url, crwaling_output):

    client = NotionClient(token_v2=token)

    cv = client.get_collection_view(notion_page_url)

    cv.collection.description = f'**Update Date: {datetime.now().strftime("%Y-%m-%d %H:%M")}**'

    for idx in crwaling_output:
        row = cv.collection.add_row()
        row.blog = idx
        row.title = crwaling_output[idx][0]
        row.date = crwaling_output[idx][1]
        row.url = crwaling_output[idx][2]

    result = cv.default_query().execute()

    sort_params = [{
        "direction": "descending",
        "property": "date",
    }]
    result = cv.build_query(sort=sort_params).execute()
    assert row in result


def date_form(date):
    year = date.split('-')[0]
    month = date.split('-')[1]
    month = month.lower()
    day = date.split('-')[2]

    if month == 'january' or month == 'jan':
        month = '01'
    elif month == 'february' or month == 'feb':
        month = '02'
    elif month == 'march' or month == 'mar':
        month = '03'
    elif month == 'april' or month == 'apr':
        month = '04'
    elif month == 'may':
        month = '05'
    elif month == 'june' or month == 'jun':
        month = '06'
    elif month == 'july' or month == 'jul':
        month = '07'
    elif month == 'august' or month == 'aug':
        month = '08'
    elif month == 'september' or month == 'sep':
        month = '09'
    elif month == 'october' or month == 'oct':
        month = '10'
    elif month == 'november' or month == 'nov':
        month = '11'
    elif month == 'december' or month == 'dec':
        month = '12'

    output = year + '-' + month + '-' + day

    return output

data = crawling()
notion_write(token, notion_page, data)
