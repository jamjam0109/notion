import requests
from bs4 import BeautifulSoup
from utils import create_output, date_form

def crawling():
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
    # naver_d2_output = create_output(naver_d2_title, naver_d2_date, naver_d2_url)
    #
    # output['NAVER D2'] = naver_d2_output

    '''
    스포카
    요약 있음
    '''
    spoqa_home = 'https://spoqa.github.io/'
    req = requests.get(spoqa_home)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    spoqa = soup.find("h2", {"class": "post-title"})

    spoqa_title = spoqa.text
    spoqa_url = spoqa_home + spoqa.find('a')['href']

    spoqa_date = soup.find("span", {"class": "post-date"}).text
    spoqa_date = spoqa_date.replace('년 ', '-')
    spoqa_date = spoqa_date.replace('월 ', '-')
    spoqa_date = spoqa_date.replace('일', '')

    spoqa_output = create_output(spoqa_title, spoqa_date, spoqa_url)
    output['스포카'] = spoqa_output

    '''
    SAS
    '''
    sas_home = 'https://blogs.sas.com/content/'
    req = requests.get(sas_home)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    sas = soup.find("div", {"class": "column half blocks"})
    sas_title = sas.find('h2').find('a')['title']
    sas_url = sas.find('a')['href']

    sas_date = sas.find('time')['datetime']
    sas_date = sas_date.split('T')[0]

    sas_output = create_output(sas_title, sas_date, sas_url)
    output['sas'] = sas_output

    '''
    우아한 형제들
    요약 있음
    '''
    woowabros_home = 'http://woowabros.github.io'
    req = requests.get(woowabros_home)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    woowabros = soup.find("div", {"class": "list-module"})
    woowabros_title = woowabros.find('h2').text
    woowabros_url = woowabros.find('a')['href']

    woowabros_date = woowabros.find('span').text
    woowabros_date = woowabros_date.split('\n')
    woowabros_date = woowabros_date[0]

    woowabros_date = woowabros_date.replace(',', '')
    woowabros_date = woowabros_date.split(' ')
    woowabros_date = woowabros_date[2] + '-' + woowabros_date[0] + '-' + woowabros_date[1]
    woowabros_date = date_form(woowabros_date)

    woowabros_output = create_output(woowabros_title, woowabros_date, woowabros_url)
    output['우아한형제들'] = woowabros_output

    '''
    samsung sds
    요약 있음
    시간 오래걸림
    '''
    samsung_sds_home = 'https://www.samsungsds.com/global/ko/support/insights/index.html'
    req = requests.get(samsung_sds_home)
    req.encoding = None
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    samsung_sds = soup.find("div", {"class": "inWrap"})

    samsung_sds_title = samsung_sds.find('a').text
    samsung_sds_url = 'https://www.samsungsds.com' + samsung_sds.find('a')['href']

    article = samsung_sds_url
    req = requests.get(article)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    samsung_sds_date = soup.find("span", {"class": "post_date"}).text

    samsung_sds_output = create_output(samsung_sds_title, samsung_sds_date, samsung_sds_url)
    output['삼성 SDS'] = samsung_sds_output


    '''
    nc soft
    요약 없음
    '''
    ncsoft_home = 'https://blog.ncsoft.com/rd/all/'
    req = requests.get(ncsoft_home)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    ncsoft = soup.find("div", {"class": "cont"})

    ncsoft_title = ncsoft.find('h3').text
    ncsoft_url = ncsoft.find('a')['href']

    ncsoft_date = ncsoft.find("div", {"class": "date"}).text
    ncsoft_date = ncsoft_date.replace('.', '-')

    ncsoft_output = create_output(ncsoft_title, ncsoft_date, ncsoft_url)
    output['ncsoft'] = ncsoft_output

    '''
    SUALAB
    요약 없음
    '''
    sualab_home = 'http://research.sualab.com'
    req = requests.get(sualab_home)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    sualab = soup.find("a", {"class": "post-link"})

    sualab_title = sualab.text
    sualab_url = sualab_home + sualab['href']

    sualab_date = soup.find("span", {"class": "post-meta"}).text
    sualab_date = sualab_date.replace(',', '')
    sualab_date = sualab_date.split(' ')
    sualab_date = sualab_date[2] + '-' + sualab_date[0] + '-' + sualab_date[1]
    sualab_date = date_form(sualab_date)

    sualab_output = create_output(sualab_title, sualab_date, sualab_url)
    output['SUALAB'] = sualab_output

    '''
    LINE Engineering
    요약 있음
    '''
    line_engine_home = 'https://engineering.linecorp.com/ko/blog/'
    req = requests.get(line_engine_home)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    line_engine = soup.find("div", {"class": "entry-header-text-top text-left"})

    line_engine_title = line_engine.find('a').text

    line_engine_url = line_engine.find('a')['href']

    line_engine_date = soup.find("span", {"class": "byline"}).text
    line_engine_date = line_engine_date.split('|')[1]
    line_engine_date = line_engine_date.replace(u'\xa0', u'')
    line_engine_date = line_engine_date.replace('.', '-')

    line_engine_output = create_output(line_engine_title, line_engine_date, line_engine_url)
    output['line_engine'] = line_engine_output

    '''
    TOAST
    요약 있음
    '''
    # toast_home = 'https://meetup.toast.com'
    # driver.get(toast_home)
    # toast = driver.find_element_by_css_selector('div.sec_box')
    # toast_txt = toast.text
    #
    # toast_list = toast_txt.split('\n')
    #
    # toast_title = toast_list[0]
    #
    # toast_date = toast_list[2].split(' ')
    # toast_date = toast_date[1].replace('.', '-')
    #
    # toast_url = driver.find_element_by_css_selector('li.lst_item.ng-scope')
    # toast_url = toast_url.find_element_by_css_selector('a').get_attribute('href')
    #
    # toast_output = create_output(toast_title, toast_date, toast_url)
    #
    # output['TOAST'] = toast_output

    '''
    AWS 한국 블로그
    요약 있음
    '''
    aws_korea_home = 'https://aws.amazon.com/ko/blogs/korea/'
    req = requests.get(aws_korea_home)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    aws_korea = soup.find("h2", {"class": "blog-post-title"})
    aws_korea_title = aws_korea.text

    aws_korea_url = aws_korea.find('a')['href']

    aws_korea_date = soup.find("time", {"property": "datePublished"})
    aws_korea_date = aws_korea_date.text.split(' ')
    aws_korea_date = aws_korea_date[2] + '-' + aws_korea_date[1] + '-' + aws_korea_date[0]
    aws_korea_date = date_form(aws_korea_date)

    aws_korea_output = create_output(aws_korea_title, aws_korea_date, aws_korea_url)
    output['AWS 한국 블로그'] = aws_korea_output

    '''
    Naver Labs
    요약 있음
    '''
    naver_labs_home = 'https://www.naverlabs.com/storyList'
    req = requests.get(naver_labs_home)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    naver_labs = soup.find("div", {"class": "featured-list"})
    naver_labs_title = naver_labs.find('a').text
    naver_labs_url = 'https://www.naverlabs.com' + naver_labs.find('a')['href']

    naver_labs_date = soup.find("span", {"class": "date"})
    naver_labs_date = naver_labs_date.text
    naver_labs_date = naver_labs_date.replace('.', '-')

    naver_labs_output = create_output(naver_labs_title, naver_labs_date, naver_labs_url)
    output['naver_labs'] = naver_labs_output

    '''
    TensorFlow
    요약 있음
    '''
    tensorflow_home = 'https://medium.com/tensorflow'
    req = requests.get(tensorflow_home)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    tensorflow = soup.find("div", {"class": "u-lineHeightBase postItem u-marginRight3"})

    tensorflow_title = tensorflow.text
    tensorflow_url = tensorflow.find('a')['href']

    tensorflow_date = soup.find("div", {
        "class": "ui-caption u-fontSize12 u-baseColor--textNormal u-textColorNormal js-postMetaInlineSupplemental"})
    tensorflow_date = tensorflow_date.find('time')['datetime']
    tensorflow_date = tensorflow_date.split('T')[0]

    tensorflow_output = create_output(tensorflow_title, tensorflow_date, tensorflow_url)
    output['tensorflow'] = tensorflow_output

    '''
    브랜디
    '''
    brandi_home = 'http://labs.brandi.co.kr'
    req = requests.get(brandi_home)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    brandi = soup.find("ul", {"class": "post-list"})

    brandi_title = brandi.find('a').text
    brandi_url = brandi_home + brandi.find('a')['href']

    brandi_date = soup.find("div", {"class": "post-date"}).text

    brandi_output = create_output(brandi_title, brandi_date, brandi_url)
    output['브랜디'] = brandi_output
    '''
    지그재그
    '''
    # zigzag_home = 'https://brunch.co.kr/@zigzag#articles'
    # driver.get(zigzag_home)
    # zigzag = driver.find_element_by_css_selector('li.animation_up')
    # zigzag_txt = zigzag.text
    #
    # zigzag_list = zigzag_txt.split('\n')
    #
    # zigzag_title = zigzag_list[0]
    #
    # zigzag_date = zigzag_list[-1]
    # zigzag_date = zigzag_date.replace('.', '')
    # zigzag_date = zigzag_date.split(' ')
    # zigzag_date = zigzag_date[2] + '-' + zigzag_date[0] + '-' + zigzag_date[1]
    # zigzag_date = date_form(zigzag_date)
    #
    # zigzag_url = zigzag.find_element_by_css_selector('a').get_attribute('href')
    #
    # zigzag_output = create_output(zigzag_title, zigzag_date, zigzag_url)
    # output['지그재그'] = zigzag_output


    '''
    티몬
    '''
    # tmon_home = 'http://blog.naver.com/PostList.nhn?blogId=tmondev&categoryNo=0&from=postList'
    # driver.get(tmon_home)
    # tmon = driver.find_element_by_css_selector('span.ell2.pcol2')
    # tmon_title = tmon.text
    #
    # tmon_url = tmon.find_element_by_css_selector('a').get_attribute('href')
    #
    # tmon_date = driver.find_element_by_css_selector('td.date').text
    # tmon_date = tmon_date.replace('.', '')
    # tmon_date = tmon_date.replace(' ', '-')
    # tmon_date = date_form(tmon_date)
    #
    # tmon_output = create_output(tmon_title, tmon_date, tmon_url)
    # output['티몬'] = tmon_output

    '''
    NVIDIA
    요약 있음
    카테고리가 넘모 많음, 일단 딥러닝만 
    시간이 넘모 걸림
    403 error 뜸
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
    # nvidia_output = create_output(nvidia_title, nvidia_date, nvidia_url)
    #
    # output['NVIDIA'] = nvidia_output

    return output
