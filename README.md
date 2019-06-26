## 목적
Python과 Notion을 활용하여 기술 블로그 리스트 만들기 

[Notion Test Page](https://www.notion.so/jaemin/0e0386aa405041b8bb7b1537ffed25f3?v=c7c08f40039e4db0b5ce1c90cefbdf6a)

## 현황
* 190626
    1. BeautifulSoup만 써서 크롤링하면 될텐데 멍청하게 Selenium 쓰고 있다. 안타깝다.
    2. list update 할 때 다 기존 목록을 다 지우고 시작한다. 더 효율적인 방법 ?
        * 기존/신규 블로그명, 제목이 같으면 지우지 말기 ? 
    3. 동일한 시간에 Python 코드를 돌리는 방법이 뭐가 있을까(무료로..)
    4. sorting은 Notion에서 디폴트로 걸어놨다. 음.. 사용자가 불편해할 것 같다.
    
 ## 참고
* [Unofficial Python 3 client for Notion API](https://github.com/jamalex/notion-py)

