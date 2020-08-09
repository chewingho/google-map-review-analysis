from get_actual_date import get_actual_date
import requests 
import json
import pandas as pd

def get_review(url):
    text = requests.get(url).text
    pretext = ')]}\''
    text = text.replace(pretext,'')
    # 把字串讀取成json
    soup = json.loads(text)
    # 取出包含留言的List
    conlist = soup[2]  
    df = pd.DataFrame(columns = ['username', 'time', 'comment', 'star']) 
    # 逐筆抓出
    for i in conlist:
        df = df.append({'username': str(i[0][1]), 'time': get_actual_date(str(i[1])), 'comment': str(i[3]), 'star': str(i[4])}, ignore_index=True) 
    return df