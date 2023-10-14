from json.decoder import JSONDecoder
from flask import jsonify
from app.helpers import index,last
from app import app

import json,unicodedata
# base config
baseurl = app.config['BASE_URL']

def normalize_text(text):
    return unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8')

def search_data(q):
    response = index(q)
    jsx = json.loads(response)
    jsx['vitems'] = [{'t': normalize_text(item['t']), 'v': item['v']} for item in jsx['vitems']]
        
    return jsonify({'author':'Konan','results':jsx})

def last_data(q):
    res = index('https://youtu.be/'+q)
    jsx = json.loads(res)
    mp3 = jsx['links']['mp3']['mp3128']
    k = mp3['k']


    res = last(k,q)
    if res: return jsonify({'author':'Konan','results':res})
    else: return jsonify({'author':'konan','status':False})

