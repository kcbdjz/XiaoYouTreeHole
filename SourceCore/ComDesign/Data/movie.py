#电影数据
import csv
import random

import requests


def movie_data():
    url = "https://movie.douban.com/j/chart/top_list"
    get_param = {
        "type": "22", "interval_id": "100:90", "action": "", "start": "0", "limit": "10"
    }
    UA = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    response = requests.get(url=url, params=get_param, headers=UA)
    out_put = response.json()
    # 创建csv文件joke.csv
    movie_csv = open('./movie.csv', 'w', encoding='utf-8')
    writer = csv.writer(movie_csv)
    writer.writerow(['text'])
    movie_total = []
    for out in out_put:
        movie_info = [out["title"], out["score"]]
        movie_info.extend(out["types"])
        movie_total.append(movie_info)
    for info in movie_total[:15]:
        movie_total.append([info])
        writer.writerow([info])
    #print(movie_total)

movie_data()
