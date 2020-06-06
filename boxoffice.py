import requests
import pandas as pd
import datetime
from time import sleep
from tqdm import tqdm
import os 

url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json'
key = os.environ['MOVIE_KEY']
param = {
    'key':key,
    'weekGb': 0,
    'targetDt':'20200524',
}

time = datetime.datetime(2020, 5, 31)
delta = datetime.timedelta(days=7)
result = pd.DataFrame()

for i in tqdm(range(50)):
    res = requests.get(url, param)
    json = res.json()
    df = pd.DataFrame(json['boxOfficeResult']['weeklyBoxOfficeList'])
    result = pd.concat([result, df], axis=0)
    
    time = time-delta
    param['targetDt'] = f'{time.year}{time.month:02}{time.day:02}'
    sleep(0.5)


result.to_csv('boxoffice.csv', encoding='utf-8', index=False)