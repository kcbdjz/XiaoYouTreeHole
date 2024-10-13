from templates.config import conn
import random

cur = conn.cursor()


def add_video(video_url, title, up, cover_url):
    sql = "INSERT INTO heal_video(video_url, title, up , cover_url) VALUES ('%s', '%s', '%s', '%s')" % (
        video_url, title, up, cover_url)
    cur.execute(sql)
    conn.commit()


def get_video():
    sql = "SELECT * FROM heal_video"
    cur.execute(sql)
    data = cur.fetchall()
    return data


def random_video():
    data = get_video()
    return random.choice(data)

print(get_video())
# title = {
#     1: '【治愈向】3分钟了解：当我很丧时，如何调节负面情绪',
#     2: '10分钟缓解一切负面情绪 肯定自我激活最佳状态！｜顺毛冥想',
#     3: '卧槽......听完这段我的精神内耗治好了！',
#     4: '每次我撑不下去的时候，就会打开这个视频',
#     5: '叫醒颓废的自己，别再清醒的堕落下去',
#     6: '人生是旷野，而非轨道',
#     7: '谨以此片，献给暂时性消沉的你',
#     8: '把罗翔老师这段话读烂',
#     9: '4分钟教你如何摆脱“消极心态”！！',
#     10: '建立不可阻挡的信心的 7 个心理学技巧',
#     11: '听完这段话，我好像可以坦然面对焦虑情绪了…'
# }
# up = {
#     1: '@白茶树与老爷爷',
#     2: '@范李猿',
#     3: '@爱睡觉的_Koala',
#     4: '@爱睡觉的_Koala',
#     5: '@森迷之影',
#     6: '@5ocool',
#     7: '@鼠鼠文学',
#     8: '@恣睢叉叉',
#     9: '@傻白在美国',
#     10: '@才思俱乐部',
#     11: '@一只鹿_LULU',
# }

# for i in range(1, 12):
#     add_video(video_url='/ComDesigeData/heal_video/video{}.mp4'.format(i), up=up[i], title=title[i],cover_url='/ComDesigeData/video_cover/video{}.png')
# i =11
# add_video(video_url='/ComDesigeData/heal_video/video{}.mp4'.format(i), up=up[i], title=title[i],cover_url='/ComDesigeData/video_cover/video{}.png')
# data = get_video()
# print(data)
# dic = {}
# for i in range(len(data)):
#     print(i)
#     dic[data[i][0]] = {}
#     dic[data[i][0]]['video_url'] = data[i][1]
#     dic[data[i][0]]['up'] = data[i][6]
#     dic[data[i][0]]['title'] = data[i][4]
#     dic[data[i][0]]['cover_url'] = data[i][5]
# print(dic)
