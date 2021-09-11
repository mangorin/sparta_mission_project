from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta


# HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('index.html')


# API 역할을 하는 부분(서버)
@app.route('/api/list', methods=['GET']) #get type 요청 받음
def show_stars():
    movie_star = list(db.mystar.find({},{'_id':False}).sort("like", -1)) #값을 담기 위한 변수, like로 내림차순(파이몽고 정렬방법)
    return jsonify({'movie_stars': movie_star})


@app.route('/api/like', methods=['POST'])
def like_star():
    name_receive = request.form['name_give'] # 이름으로 받고

    target_star = db.mystar.find_one({'name': name_receive}) # 이름으로 하나 찾고
    current_like = target_star['like'] # 찾은것중에 like 값을 찾음

    new_like = current_like + 1 # like값에다가 하나 더 한 것을 다시 저장!

    # 이제 업데이트 시켜줘야함
    db.mystar.update_one({'name': name_receive}, {'$set': {'like': new_like}})

    return jsonify({'msg': '좋아요 완료!'})


@app.route('/api/delete', methods=['POST'])
def delete_star():
    name_receive = request.form['name_give']
    db.mystar.delete_one({'name': name_receive})
    return jsonify({'msg': '삭제 완료!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)