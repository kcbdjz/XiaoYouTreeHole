#笑话数据
import csv
import requests
import re

def joke_data():
    url = "https://xiaohua.zol.com.cn/duanpian/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'
    }
    response = requests.get(url=url, headers=headers)

    joke_data = []

    # 创建csv文件joke.csv
    joke_csv = open('./joke.csv', 'w', encoding='utf-8')
    writer = csv.writer(joke_csv)
    writer.writerow(['text'])

    joke = re.findall(' <div class="summary-text">(.*?)</div>', response.text)
    for info in joke[:15]:
        joke_data.append([info])
        writer.writerow([info])
    print(joke_data)

    # random_index = random.randint(0, len(joke_data) - 1)
    #
    # # 使用随机索引访问列表中的元素
    # random_item = joke_data[random_index]
    # print(random_item)
    joke_csv.close()
joke_data()



# random_index = random.randint(0, len(joke_data()) - 1)
#
# # 使用随机索引访问列表中的元素
# random_item = joke_data()[random_index]

#print("root：", random_item)
