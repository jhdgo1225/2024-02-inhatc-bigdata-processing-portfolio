# -*- coding: utf-8 -*-
"""bigdata_portfolio_naver.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Qw1r50qRbYpcfZHvQymvsBvZYqkFymCH
"""

# Commented out IPython magic to ensure Python compatibility.
# %%bash
# apt-get update
# apt-get install g++ openjdk-8-jdk python-dev python3-dev
# pip3 install JPype1
# pip3 install konlpy

import json
import re

from konlpy.tag import Okt

from collections import Counter

import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from wordcloud import WordCloud, ImageColorGenerator

import os
import sys
import urllib.request
import datetime
import time
import json


client_id = 'pQ1gqFQ8M16UrL_IiDLG'
client_secret = 'Qk1Jbn7Fh7'


#[CODE 1]
def getRequestUrl(url):
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", client_id)
    req.add_header("X-Naver-Client-Secret", client_secret)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print ("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None

#[CODE 2]
def getNaverSearch(node, srcText, start, display):
    base = "https://openapi.naver.com/v1/search"
    node = "/%s.json" % node
    parameters = "?query=%s&start=%s&display=%s" % (urllib.parse.quote(srcText), start, display)

    url = base + node + parameters
    responseDecode = getRequestUrl(url)   #[CODE 1]

    if (responseDecode == None):
        return None
    else:
        return json.loads(responseDecode)

#[CODE 3]
def getPostData(post, jsonResult, cnt):
    title = post['title']
    description = post['description']
    link = post['link']
    originallink = post['originallink']

    pDate = datetime.datetime.strptime(post['pubDate'],  '%a, %d %b %Y %H:%M:%S %z')
    pDate = pDate.strftime('%Y-%m-%d %H:%M:%S')

    jsonResult.append({'cnt':cnt, 'title':title, 'description': description,  'link': link,  'originallink':originallink, 'pDate':pDate})
    return

# 크롤링 할 대상: news - 네이버 뉴스, blog - 네이버 블로그
# node = 'blog'
node = 'news'
srcText = input('검색어를 입력하세요: ')
cnt = 0
responseCnt = 0
jsonResult = []

jsonResponse = getNaverSearch(node, srcText, 1, 100)  #[CODE 2]
total = jsonResponse['total']
if jsonResponse != None:
    responseCnt += 1

while ((jsonResponse != None) and (jsonResponse['display'] != 0) and responseCnt < 20):
    for post in jsonResponse['items']:
        cnt += 1
        getPostData(post, jsonResult, cnt)  #[CODE 3]

    start = jsonResponse['start'] + jsonResponse['display']
    jsonResponse = getNaverSearch(node, srcText, start, 100)  #[CODE 2]
    responseCnt += 1

print('전체 검색 : %d 건' %total)

with open('%s_naver_%s.json' % (srcText, node), 'w', encoding='utf8') as outfile:
    jsonFile = json.dumps(jsonResult,  indent=4, sort_keys=True,  ensure_ascii=False)

    outfile.write(jsonFile)

print("가져온 데이터 : %d 건" %(cnt))
print ('%s_naver_%s.json SAVED' % (srcText, node))

inputFileName = '/content/핫식스 에너지드링크_naver_news'
data = json.loads(open(inputFileName+'.json', 'r', encoding='utf-8').read())
data #출력하여 내용 확인

message = ''

for item in data:
#    if 'message' in item.keys():
#        message = message + re.sub(r'[^\w]', ' ', item['message']) +''
    if 'description' in item.keys():
        message = message + re.sub(r'[^\w]', ' ', item['description']) +''

message #출력하여 내용 확인

nlp = Okt()
message_N = nlp.nouns(message)
message_N   #출력하여 내용 확인

count = Counter(message_N)

count   #출력하여 내용 확인

word_count = dict()

for tag, counts in count.most_common(200):
    if(len(str(tag))>1):
        word_count[tag] = counts
        print("%s : %d" % (tag, counts))

!apt-get update -qq
!apt-get install fonts-nanum* -qq

import matplotlib.font_manager as fm
from PIL import Image
import numpy as np
font_path = "/usr/share/fonts/truetype/nanum/NanumBarunGothicBold.ttf"
font_name = fm.FontProperties(fname = font_path).get_name()
matplotlib.rc('font', family=font_name)
#fm._rebuild()

icon = Image.open('/content/netflix.png') # 넷플릭스

icon = Image.open('/content/monster.png') # 몬스터

icon = Image.open('/content/redbull.png') # 레드불

icon = Image.open('/content/hotsix.png') # 핫식스

plt.imshow(icon)

mask = Image.new("RGB", icon.size, (255,255,255))
mask.paste(icon, icon)
mask = np.array(mask)

wc = WordCloud(font_path, background_color='white', width=600, height=800, max_words=200, mask=mask)
cloud=wc.generate_from_frequencies(word_count)

plt.figure(figsize=(6,6))
plt.axis('off')

image_colors = ImageColorGenerator(mask)
plt.imshow(wc.recolor(color_func=image_colors), interpolation='bilinear')
plt.show()

cloud.to_file(inputFileName + '_cloud.jpg')