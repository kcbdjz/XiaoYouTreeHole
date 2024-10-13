#古诗数据
import csv
import random

import requests
from lxml import etree


def index():
    """
    :return:
    """
    base_url = "https://so.gushiwen.cn/gushi/tangshi.aspx"
    response = requests.get(base_url)
    html = etree.HTML(response.text)
    urls = html.xpath('//div[@class="typecont"]/span/a/@href')
    return urls


def poetry_data(url):
    """
    :param url: 每一首古诗的url
    :return: 古诗数据
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'

    }
    response = requests.get(url, headers=headers)
    id = url.split("_")[-1].split(".")[0]

    html = etree.HTML(response.text)
    title = html.xpath(f'//div[@id="zhengwen{id}"]/h1/text()')
    author = html.xpath(f'//div[@id="zhengwen{id}"]/p/a/text()')
    author = ''.join(author).strip()
    infor = html.xpath(f'//div[@id="contson{id}"]/text()')
    infor = ''.join(infor).strip()
    return ["题目：", title[0], "作家：", author, "诗句：", infor]


pretry_data = []
host = "https://so.gushiwen.cn"
urls = index()
for url in urls[:15]:
    detail_url = host + url
    content = poetry_data(detail_url)
    pretry_data.append(content)
# 将数据写入CSV文件
with open('poem.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # 写入表头
    writer.writerow(['text'])
    # 写入数据行
    for poem_data in pretry_data:
        writer.writerow([poem_data[1], poem_data[3], poem_data[5]])

print("CSV文件已生成！")

#print(pretry_data)
# random_index = random.randint(0, len(pretry_data) - 1)
#
# # 使用随机索引访问列表中的元素
# random_item = pretry_data[random_index]
# print(random_item)