# -*- coding: utf-8 -*-
import os
import re
import json
import requests
from urllib.parse import urlencode
from bs4 import BeautifulSoup


LOGIN_HEADERS = {
    'Origin': 'http://114.215.193.7', 
    'Host': '114.215.193.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,la;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'DNT': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'http://114.215.193.7/data/',
}
HEADERS = {'User-Agent': 'pan.baidu.com', 'Referer': 'pan.baidu.com'}

USERNAME = 'yaoyuanfa001'
PASSWORD = '123456'


def fetch_cert(username=USERNAME, pasword=PASSWORD):
    session = requests.session()
    data = {'username': username, 'password': pasword, 'login': 'Log in 登录'}
    response = session.post(url='http://114.215.193.7/data/data.php', data=data, headers=LOGIN_HEADERS)
    soup = BeautifulSoup(str(response.content, 'gbk'), "html.parser")
    url = soup.a.attrs['href']
    target = soup.find(text=re.compile(r'下载密码：[0-9a-z]{4}$'))
    shorturl = url.split('/')[-1][1:]
    password = target.split('：')[1]
    print(url)
    response = requests.post('https://pan.baidu.com/share/verify?surl={}'.format(shorturl), data={'pwd': password}, headers=HEADERS)
    return shorturl, password, json.loads(response.text)['randsk']


def test():
    # https://pan.baidu.com/union/document/entrance
    # https://pan.baidu.com/union/document/basic

    shorturl, password, randsk = fetch_cert()
    print(shorturl, password, randsk)
    url = 'https://pan.baidu.com/share/list?shorturl={}&sekey={}&dir={}&page=1&num=10'.format(shorturl, randsk, '/stock data/2019 Level 2 Data/201907')
    response = requests.get(url, headers=HEADERS)
    result = json.loads(response.text)
    with open('list.json', 'wb') as f:
        f.write(response.content)
    # 'https://pan.baidu.com/rest/2.0/xpan/multimedia?method=filemetas&access_token=123&path=/<share>123-456&fsids=[111,222]&thumb=1&dlink=1&extra=1'
    # https://pan.baidu.com/rest/2.0/xpan/multimedia?method=filemetas&