from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('main.html')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/travel')
def travel():
    return render_template('travel.html')

@app.route('/hotel')
def hotel():
    return render_template('hotel.html')

@app.route('/food')
def food():
    return render_template('food.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)