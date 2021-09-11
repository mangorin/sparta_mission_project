from pymongo import MongoClient #ptmongo접속
client = MongoClient('localhost', 27017) #지금 내 컴퓨터에 돌아가고 있는 mongodb 접속.
db = client.dbsparta #db스파르타라고 하는 이름으로 접속 할 것이다.(없으면 자동으로 만들어짐)

#mongodb는 dic가 쌓이는 것.

# 코딩 시작
#꼭 기억해야 할 4가지 - insert, find, update, delete

#insert
#doc = {'name':'jane','age':21} #dic하나 만듦
#db.users.insert_one(doc) #만든 dic을 user에 넣는다. 비슷한 것들은 같이 쌓아줌. collection이라는 개념있음(디비안에 users 안에 insert해라)

#insert

#find
###########################################################보통 이런식으로 많이 사용한다.
#same_ages = list(db.users.find({},{'_id':False})) #False: 나타내지 말아라. unique값이라 거의 _id는 보여주지 않는다.

#for person in same_ages:
#    print(person)
#############################################################

#user = db.users.find_one({'name':'bobby'}, {'_id':False}) #name이 bobby인 것만 가지고 와라
#print(user['age']) #많이 있어도 가장 첫번째 찾은 값 하나만 가져온다.

#update
db.users.update_one({'name':'bobby'},{'$set':{'age':19}}) #name이 bobby인 사람을 찾아서, age를 19로 바꿔줘라
#update_many: name이 bobby인 것을 모두 찾아서 age를 19로 바꿔라. update는 위험부담이 크기 때문에 잘 쓰이지는 않는다.

#delete
db.users.delete_one({'name':'bobby'}) #name이 bobby인 사람을 찾아서, delete해라. 얘도 many가 있지만 잘 쓰이지 않는다.


##정리
# 저장 - 예시
doc = {'name':'bobby','age':21}
db.users.insert_one(doc)

# 한 개 찾기 - 예시
user = db.users.find_one({'name':'bobby'})

# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
same_ages = list(db.users.find({'age':21},{'_id':False})) #리뷰 여!러!개!

# 바꾸기 - 예시
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# 지우기 - 예시
db.users.delete_one({'name':'bobby'})
