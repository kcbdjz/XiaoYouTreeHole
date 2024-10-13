# 相声数据
import csv
import re
import requests
def album_data():
    url = "https://www.ximalaya.com/xiangsheng/9723091"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'
    }
    response = requests.get(url=url, headers=headers)
    # 创建csv文件joke.csv
    crosstalk_csv = open('./crosstalk.csv', 'w', encoding='utf-8')
    writer = csv.writer(crosstalk_csv)
    writer.writerow(['text'])
    album_data = []
    album = re.findall('<a title="(.*?)" href="/sound/(\d+)">', response.text)
    for title, album_id in album[:15]:
        album_data.append([title])
    #print(album_data)
    # 从列表中拿元素放入csv文件中
    for data in album_data:
        writer.writerow(data)

    crosstalk_csv.close()
    return album_data



# 调用函数获取数据并写入CSV文件
album_data()