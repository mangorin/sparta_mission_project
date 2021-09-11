from pymongo import MongoClient #ptmongo접속
client = MongoClient('localhost', 27017) #지금 내 컴퓨터에 돌아가고 있는 mongodb 접속.
db = client.dbsparta #db스파르타라고 하는 이름으로 접속 할 것이다.(없으면 자동으로 만들어짐)

#1
movies = db.movies.find_one({'title':'매트릭스'})
#print(movies['grade'])

#2(맞음!!~!~!~!!oh yeah!!)
movies = db.movies.find_one({'title':'매트릭스'})
m_grade = movies['grade']
database = list(db.movies.find({},{'_id':False}))

for data in database:
    if data['grade'] == m_grade:
        result = data['title']
        print(result)


db.movies.update_one({'title':'매트릭스'},{'$set':{'grade':'0'}})
#다른 값들을 봤을때 문자열로 다 저장되어 있으므로 숫자 0이 아닌, 문자열 '0'으로 넣어주는 것이 좋다.(어떤 형식으로 담겨져 있는지도 확인하기!)

