## 목적
Python과 Notion을 활용하여 기술 블로그 리스트 만들기 

<a href="https://www.notion.so/jaemin/0e0386aa405041b8bb7b1537ffed25f3?v=c7c08f40039e4db0b5ce1c90cefbdf6a" target="_blank">Notion Test Page</a>

## 현황
* 190626
    1. BeautifulSoup만 써서 크롤링하면 될텐데 멍청하게 Selenium 쓰고 있다. 안타깝다.
        * Selenium은 이제 그만 쓰자. git에는 Selenium으로 따로 저장해놓고 뷰티풀수웊으로 갈아타자 ㅠ 
    2. list update 할 때 다 기존 목록을 다 지우고 시작한다. 더 효율적인 방법 ?
        * 기존/신규 블로그명, 제목이 같으면 지우지 말기 ? 
    3. 동일한 시간에 Python 코드를 돌리는 방법이 뭐가 있을까(무료로..)
    4. sorting은 Notion에서 디폴트로 걸어놨다. 음.. 사용자가 불편해할 것 같다.
    5. date의 format이 text인데 언젠간 date로 바꾸고 싶어
    6. 최근 3개월 이전 글은 보여주지 말까? 왜? 그냥 ..
    7. 블로그 글 Word Cloud 만들어서 이미지를 넣고 싶어
    
* 190703
    1. 뷰티풀숲으로 갈아 탔는데 아직 티몬, 지그재그, 토스트, 엔비디아, SDS는 못함
        * SDS의 경우 한글이 다 깨진다.
        * 나머진 긁어오는게 어렵다...
        * ~~이번주까지 못하면(190707) 못한 애들은 셀레니움으로 임시방편하자~~
    2. ~~이번 주 토요일(190706)에는 개인블로그 크롤링을 진행하자~~
    
* 190709
    1. 응. 위에있는 계획 하나도 안했어
    2. 지금 해보자  
## 변경이력

<details><summary>190726</summary>
<p>

* ncsoft UI 변경 됨

</p>
    
 ## 참고
* <a href="https://github.com/jamalex/notion-py" target="_blank">Unofficial Python 3 client for Notion API</a>

