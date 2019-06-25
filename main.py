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

    '''
    Naver D2
    요약있음
    안됌....
    '''
    # naver_d2_home = 'https://d2.naver.com/home'
    # driver.get(naver_d2_home)
    # naver_d2 = driver.find_element_by_class_name('post_article')
    # naver_d2_txt = naver_d2.text
    #
    # naver_d2_list = naver_d2_txt.split('\n')
    # naver_d2_title = naver_d2_list[0]
    # naver_d2_date = naver_d2_list[-3]
    # naver_d2_date = naver_d2_date.replace('.', '-')
    # naver_d2_url = naver_d2.find_element_by_css_selector('a').get_attribute('href')
    #
    # naver_d2_output = list()
    #
    # naver_d2_output.append(naver_d2_title)
    # naver_d2_output.append(naver_d2_date)
    # naver_d2_output.append(naver_d2_url)
    #
    # output['NAVER D2'] = naver_d2_output

    '''
    스포카
    요약 있음
    '''
    spoqa_home = 'https://spoqa.github.io/'
    driver.get(spoqa_home)
    spoqa = driver.find_element_by_class_name('post-author-info')

    spoqa_url = spoqa.find_element_by_css_selector('a').get_attribute('href')
    spoqa_txt = spoqa.text

    spoqa_list = spoqa_txt.split('\n')

    spoqa_title = spoqa_list[0]
    spoqa_date = spoqa_list[2].split('|')[0]
    spoqa_date = spoqa_date.replace('년 ', '-')
    spoqa_date = spoqa_date.replace('월 ', '-')
    spoqa_date = spoqa_date.replace('일', '')

    spoqa_output = list()

    spoqa_output.append(spoqa_title)
    spoqa_output.append(spoqa_date)
    spoqa_output.append(spoqa_url)

    output['spoqa'] = spoqa_output

    '''
    SAS
    언어(스페니쉬, 제페니즈..)가 넘모 다양함..
    url이 author
    '''
    sas_home = 'https://blogs.sas.com/content/all-posts/'
    driver.get(sas_home)
    sas = driver.find_element_by_class_name('content')
    sas_txt = sas.text

    sas_list = sas_txt.split('\n')
    sas_title = sas_list[3] + '(' + sas_list[-1] + ')'

    sas_date = sas_list[1]
    sas_date = sas_date.split(', ')
    sas_date = sas_date[1] + '-' + sas_date[0].replace(' ', '-')
    sas_date = date_form(sas_date)

    sas_url = sas.find_element_by_css_selector('a').get_attribute('href')

    sas_output = list()

    sas_output.append(sas_title)
    sas_output.append(sas_date)
    sas_output.append(sas_url)

    output['SAS'] = sas_output

    '''
    우아한 형제들
    요약 있음
    date 형식 문제: 2019 Jun 12
    '''
    woowabros_home = 'http://woowabros.github.io/'
    driver.get(woowabros_home)

    woowabros = driver.find_element_by_class_name('list-module')
    woowabros_txt = woowabros.text

    woowabros_list = woowabros_txt.split('\n')

    woowabros_date = woowabros_list[0]
    woowabros_date = woowabros_date.split(',')
    woowabros_date = woowabros_date[1] + woowabros_date[0]
    woowabros_date = woowabros_date.replace(' ', '-')

    woowabros_title = woowabros_list[1]
    woowabros_url = woowabros.find_element_by_css_selector('a').get_attribute('href')

    woowabros_output = list()

    woowabros_output.append(woowabros_title)
    woowabros_output.append(woowabros_date)
    woowabros_output.append(woowabros_url)

    output['우아한 형제들'] = woowabros_output

    '''
    samsung sds
    요약 있음
    '''
    samsung_sds_home = 'https://www.samsungsds.com/global/ko/support/insights/index.html'
    driver.get(samsung_sds_home)

    samsung_sds = driver.find_element_by_class_name('thumb_title')

    samsung_sds_title = samsung_sds.text
    samsung_sds_date = driver.find_element_by_class_name('thumb_date').text

    samsung_sds_onclcik = samsung_sds.find_element_by_css_selector('a').get_attribute('onclick')
    samsung_sds_onclcik = samsung_sds_onclcik.split('(')[1]
    samsung_sds_onclcik = samsung_sds_onclcik.split(',')[0]
    samsung_sds_onclcik = samsung_sds_onclcik.replace("'", '')

    samsung_sds_url = 'https://www.samsungsds.com/' + samsung_sds_onclcik

    samsung_sds_output = list()

    samsung_sds_output.append(samsung_sds_title)
    samsung_sds_output.append(samsung_sds_date)
    samsung_sds_output.append(samsung_sds_url)

    output['Samsung SDS'] = samsung_sds_output
    
    '''
    NVIDIA
    요약 있음
    카테고리가 넘모 많음, 일단 딥러닝만 
    시간이 넘모 걸림
    '''
    # nvidia_home = 'https://blogs.nvidia.co.kr/category/deep-learning/'
    # driver.get(nvidia_home)
    #
    # nvidia = driver.find_element_by_class_name('category-loop-items')
    # nvidia_title = nvidia.text
    # nvidia_title = nvidia_title.split('\n')
    # nvidia_title = nvidia_title[0]
    #
    # nvidia_url = nvidia.find_element_by_css_selector('a').get_attribute('href')
    #
    # nvidia_url_split = nvidia_url.split('/')
    # nvidia_date = nvidia_url_split[3] + '-' + nvidia_url_split[4] + '-' + nvidia_url_split[5]
    #
    # nvidia_output = list()
    #
    # nvidia_output.append(nvidia_title)
    # nvidia_output.append(nvidia_date)
    # nvidia_output.append(nvidia_url)
    #
    # output['NVIDIA'] = nvidia_output

    '''
    nc soft
    요약 없음
    카테고리 다양
    '''
    ncsoft_home = 'http://blog.ncsoft.com/?cat=3786'
    driver.get(ncsoft_home)

    ncsoft_home = driver.find_element_by_css_selector(
        'h2.sgny-post-title.sgny-masonary-post-title'
    )

    ncsoft_title = ncsoft_home.text
    ncsoft_url = ncsoft_home.find_element_by_css_selector('a').get_attribute('href')

    ncsoft_date = driver.find_element_by_css_selector(
        'div.text-uppercase.sgny-post-meta.sgny-masonary-post-meta'
    ).text

    ncsoft_output = list()

    ncsoft_output.append(ncsoft_title)
    ncsoft_output.append(ncsoft_date)
    ncsoft_output.append(ncsoft_url)

    output['ncsoft'] = ncsoft_output

    '''
    SUALAB
    요약 없음
    '''
    sualab_home = 'http://research.sualab.com/'
    driver.get(sualab_home)

    sualab_home = driver.find_element_by_css_selector('a.post-link')

    sualab_title = sualab_home.text

    sualab_url = sualab_home.get_attribute('href')

    sualab_date = driver.find_element_by_css_selector('span.post-meta').text
    sualab_date = sualab_date.replace(',', '')
    sualab_date = sualab_date.split(' ')
    sualab_date = sualab_date[2] + '-' + sualab_date[0] + '-' + sualab_date[1]
    sualab_date = date_form(sualab_date)

    sualab_output = list()

    sualab_output.append(sualab_title)
    sualab_output.append(sualab_date)
    sualab_output.append(sualab_url)

    output['SUALAB'] = sualab_output

    '''
    LINE Engineering
    요약 있음
    '''
    line_engine_home = 'https://engineering.linecorp.com/ko/blog/'
    driver.get(line_engine_home)
    line_engine = driver.find_element_by_css_selector('div.entry-header-text-top.text-left')
    line_engine_txt = line_engine.text
    line_engine_list = line_engine_txt.split('\n')

    line_engine_title = line_engine_list[0]

    line_engine_date = line_engine_list[1].split('|')
    line_engine_date = line_engine_date[1].replace(' ', '')
    line_engine_date = line_engine_date.replace('.', '-')

    line_engine_url = line_engine.find_element_by_css_selector('a').get_attribute('href')

    line_engine_output = list()

    line_engine_output.append(line_engine_title)
    line_engine_output.append(line_engine_date)
    line_engine_output.append(line_engine_url)

    output['LINE Engineering'] = line_engine_output


    '''
    TOAST
    요약 있음
    '''
    toast_home = 'https://meetup.toast.com'
    driver.get(toast_home)
    toast = driver.find_element_by_css_selector('div.sec_box')
    toast_txt = toast.text

    toast_list = toast_txt.split('\n')

    toast_title = toast_list[0]

    toast_date = toast_list[2].split(' ')
    toast_date = toast_date[1].replace('.', '-')

    toast_url = driver.find_element_by_css_selector('li.lst_item.ng-scope')
    toast_url = toast_url.find_element_by_css_selector('a').get_attribute('href')
    toast_output = list()

    toast_output.append(toast_title)
    toast_output.append(toast_date)
    toast_output.append(toast_url)

    output['TOAST'] = toast_output

    '''
    AWS 한국 블로그
    요약 있음
    '''
    aws_korea_home = 'https://aws.amazon.com/ko/blogs/korea/'
    driver.get(aws_korea_home)
    aws_korea = driver.find_element_by_css_selector('div.lb-col.lb-mid-18.lb-tiny-24')
    aws_korea_txt = aws_korea.text

    aws_korea_list = aws_korea_txt.split('\n')

    aws_korea_title = aws_korea_list[0]

    aws_korea_date = aws_korea_list[1].split('|')
    aws_korea_date = aws_korea_date[1].split(' ')
    aws_korea_date = aws_korea_date[4] + '-' + aws_korea_date[3] + '-' + aws_korea_date[2]
    aws_korea_date = date_form(aws_korea_date)


    aws_korea_url = aws_korea.find_element_by_css_selector('a').get_attribute('href')

    aws_korea_output = list()

    aws_korea_output.append(aws_korea_title)
    aws_korea_output.append(aws_korea_date)
    aws_korea_output.append(aws_korea_url)

    output['AWS 한국 블로그'] = aws_korea_output

    '''
    Naver Labs
    요약 있음
    '''
    naver_labs_home = 'https://www.naverlabs.com/storyList'
    driver.get(naver_labs_home)
    naver_labs = driver.find_element_by_css_selector('div.recent-list')
    naver_labs_txt = naver_labs.text
    naver_labs_list = naver_labs_txt.split('\n')

    naver_labs_title = naver_labs_list[1]

    naver_labs_date = naver_labs_list[3].split(' ')
    naver_labs_date = naver_labs_date[0].replace('.', '-')

    naver_labs_url = naver_labs.find_element_by_css_selector('a').get_attribute('href')

    naver_labs_output = list()

    naver_labs_output.append(naver_labs_title)
    naver_labs_output.append(naver_labs_date)
    naver_labs_output.append(naver_labs_url)

    output['NAVER LABS'] = naver_labs_output

    '''
    TensorFlow
    요약 있음
    '''
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

token = 'b10d49a16fe9ad2db279f0fd4c3fbd8ef53d2748b2e9c63fca0e382d234b880262994cffba849a46702f71b9cc731cfe897fed9a0fedd942b24ea5aa89359adbbc235114357383b32be4fc460999'

notion_page = 'https://www.notion.so/jaemin/0e0386aa405041b8bb7b1537ffed25f3?v=c7c08f40039e4db0b5ce1c90cefbdf6a'
data = crawling()
notion_write(token, notion_page, data)
