import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

from pymongo import MongoClient #ptmongo접속
client = MongoClient('localhost', 27017) #지금 내 컴퓨터에 돌아가고 있는 mongodb 접속.
db = client.dbsparta #db스파르타라고 하는 이름으로 접속 할 것이다.(없으면 자동으로 만들어짐)


musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
#select해서 가져올 때, 첫번째껏만 가져온 것이므로 그 부분은 삭제해줘야함 -> tr:nth-child(1)이면 tr만 남기기

#순위, 노래제목, 가수이름 가져오기
for music in musics:
    grade = music.select_one('td.number') #순위
    name = music.select_one('td.info > a.title.ellipsis') #노래제목
    singer = music.select_one('td.info > a.artist.ellipsis') #가수이름

    music_grade = grade.text[0:2].strip()
    music_name = name.text.strip()
    music_singer = singer.text
    #print(music_grade, music_name, music_singer) #->요렇게해도 원하는 값은 출력 됨!

    ###########응용
    #DB에 저장해서 추출하기
    doc = {
        'music_grade': music_grade,
        'music_name': music_name,
        'music_singer': music_singer
    }
    db.music_box.insert_one(doc)

database = list(db.music_box.find({},{'_id':False}))
for data in database:
    print(data['music_grade'], data['music_name'], data['music_singer'])
