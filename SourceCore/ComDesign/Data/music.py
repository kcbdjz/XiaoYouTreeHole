#音乐数据
import csv
import random
import re

import requests


def music_data():
    url = "https://music.163.com/discover/toplist?id=3778678"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'
    }
    response = requests.get(url=url, headers=headers)

    # 创建csv文件joke.csv
    music_csv = open('./music.csv', 'w', encoding='utf-8')
    writer = csv.writer(music_csv)
    writer.writerow(['text'])
    music_data = []
    html_data = re.findall('<li><a href="/song\?id=(\d+)">(.*?)</a>', response.text)
    for num_id, title in html_data[:15]:
        music_data.append([title])
    # 从列表中拿元素放入csv文件中
    for data in music_data:
        writer.writerow(data)
    music_csv.close()
    return music_data
    # random_index = random.randint(0, len(music_data) - 1)
    #
    # # 使用随机索引访问列表中的元素
    # random_item = music_data[random_index]
    #print(music_data)

music_data()