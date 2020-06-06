import requests
import pandas as pd
import datetime
from time import sleep
from tqdm import tqdm
import os 

boxoffice = pd.read_csv('boxoffice.csv', encoding='utf-8')
movieCodes = boxoffice['movieCd'].unique()


url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json'
key = os.environ['MOVIE_KEY']

param = {
    'key':key,
    'movieCd':'',
}

df = pd.DataFrame()
for i,code in enumerate(tqdm(movieCodes)):
    param['movieCd'] = code
    res = requests.get(url, param)
    json = res.json()
    movieInfo = json['movieInfoResult']['movieInfo']    
    df.loc[i, 'movieCd'] = movieInfo['movieCd']
    df.loc[i, 'movieNm'] = movieInfo['movieNm']
    df.loc[i, 'movieNmEn'] = movieInfo['movieNmEn']
    df.loc[i, 'movieNmOg'] = movieInfo['movieNmOg']
    df.loc[i, 'watchGradeNm'] = movieInfo['audits'][0]['watchGradeNm'] if movieInfo['audits'] else ''
    df.loc[i, 'openDt'] = movieInfo['openDt']
    df.loc[i, 'showTm'] = movieInfo['showTm']
    df.loc[i, 'directors'] = str(movieInfo['directors'])
    sleep(0.1)

df.to_csv('movies.csv', encoding='utf-8', index=False)