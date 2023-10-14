from flask import jsonify
import requests, json

def index(query):
    url = 'https://www.y2mate.com/mates/id778/analyzeV2/ajax'
    data = {
        'k_query':f'{query}',
        'k_page': 'home',
        'hl': 'id',
        'q_auto': '0',
    }

    html = requests.post(url,data=data).text
    return html

def last(k,q):
    url = 'https://www.y2mate.com/mates/convertV2/index'

    headers = {
    "Host": "www.y2mate.com",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9",
    "Content-Length": "128",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "_gid=GA1.2.1562983974.1695383238; prefetchAd_3381349=true; _ga=GA1.1.1445754993.1695383238; _ga_K8CD7CY0TZ=GS1.1.1695387180.2.0.1695387180.0.0.0",
    "Origin": "https://www.y2mate.com",
    "Referer": f"https://www.y2mate.com/id/youtube/{k}",
    "Sec-Ch-Ua": '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Linux"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}
    data = {
        'vid':q,
        'k':k
    }
    
    res = requests.post(url,data=data,headers=headers).text
    response = json.loads(res)
    
     
    return response
