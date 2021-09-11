from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# html 화면 보여주기
@app.route('/')
def home():
   return render_template('index.html')

# 디비구축
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.teamproject

#doc = {'name':'jeju맛집', '위도':123.453, '경도':123.453}
#db.users.insert_one(doc)

# 위도,경도 찾기
import numpy as np
import pandas as pd
from urllib.request import urlopen
from urllib import parse
from urllib.request import Request
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import json

## naver api
client_id = 'vv256amuz5'
client_pw = '0enz9WuZMqJBFKAR4EG5GFpLtlvHNa3XRzrlDLQu'

api_url = 'https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?query='

## 주소 목록 파일(.xlsx)
data = pd.read_excel('data/list_of_address.xlsx', usecols='B, C', names=['구주소', '도로명주소'])

## 네이버 지도 API 이용해서 위경도 찾기
geo_coordi = []
for add in data['도로명주소']:
   add_urlenc = parse.quote(add)
   url = api_url + add_urlenc
   request = Request(url)
   request.add_header('X-NCP-APIGW-API-KEY-ID', client_id)
   request.add_header('X-NCP-APIGW-API-KEY', client_pw)
   try:
      response = urlopen(request)
   except HTTPError as e:
      print('HTTP Error!')
      latitude = None
      longitude = None
   else:
      rescode = response.getcode()
      if rescode == 200:
         response_body = response.read().decode('utf-8')
         response_body = json.loads(response_body)
         if 'addresses' in response_body:
            latitude = response_body['addresses'][0]['y']
            longitude = response_body['addresses'][0]['x']
            print("Success!")
         else:
            print("'result' not exist!")
            latitude = None
            longitude = None
      else:
         print('Response error code : %d' % rescode)
         latitude = None
         longitude = None

   geo_coordi.append([latitude, longitude])

np_geo_coordi = np.array(geo_coordi)
pd_geo_coordi = pd.DataFrame({"구주소": data['구주소'].values,
                              "도로명": data['도로명주소'].values,
                              "위도": np_geo_coordi[:, 0],
                              "경도": np_geo_coordi[:, 1]})

## save result
writer = pd.ExcelWriter('output_v2.xlsx')
pd_geo_coordi.to_excel(writer, sheet_name='Sheet1')
writer.save()



## 서버 연결
if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)

