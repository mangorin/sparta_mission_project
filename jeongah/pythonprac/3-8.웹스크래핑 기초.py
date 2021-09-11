import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# 코딩 시작
#크롤링이 가능한 이유
#코드딴에서 요청하는 것. 요청되서 가지고 온 html
#리퀘스트로 요청하고 bs4으로 솎아낸다??

#headers는 브라우저에서 엔터친 거 마냥 효과를 내주는 것(막아놓는 경우가 많기 때문)
#print(soup)

#title = soup.select_one('#old_content > table > tbody > tr:nth-child(2) > td.title > div > a') #selector로 어느 위치에 있는지 알려줌
#print(title.text) #태그의 텍스트
#print(title['href']) #태그의 속성
#select-여러개 가져올때

trs = soup.select('#old_content > table > tbody > tr')
#old_content > table > tbody > tr:nth-child(2) > td.point



for tr in trs:
    a_tag = tr.select_one('td.title > div > a') #tr에서 찾은 곳에서 더 찾아 나가는 것임
    if a_tag is not None:
        title = a_tag.text
        print(title)

#순위와 평점 가져오기
for tr in trs:
    a_alt = tr.select_one('td:nth-child(1) > img')
    a_tag = tr.select_one('td.title > div > a') #tr에서 찾은 곳에서 더 찾아 나가는 것임
    a_point = tr.select_one('td.point')
    if a_tag is not None:
        rank = a_alt['alt']
        title = a_tag.text
        grade = a_point.text
        print(rank, title, grade)