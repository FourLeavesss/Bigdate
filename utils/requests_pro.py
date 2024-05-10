import random
import re
import time

import requests
from lxml import etree

# 随机UA的请求头
def head():
    user_agent = ["Mozilla/5.0 (Windows NT 10.0; WOW64)", 'Mozilla/5.0 (Windows NT 6.3; WOW64)',
                  'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                  'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
                  'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36',
                  'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; rv:11.0) like Gecko)',
                  'Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1',
                  'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3',
                  'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12',
                  'Opera/9.27 (Windows NT 5.2; U; zh-cn)',
                  'Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en) Opera 8.0',
                  'Opera/8.0 (Macintosh; PPC Mac OS X; U; en)',
                  'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6',
                  'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Win64; x64; Trident/4.0)',
                  'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)',
                  'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E)',
                  'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Maxthon/4.0.6.2000 Chrome/26.0.1410.43 Safari/537.1 ',
                  'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E; QQBrowser/7.3.9825.400)',
                  'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0 ',
                  'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.92 Safari/537.1 LBBROWSER',
                  'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; BIDUBrowser 2.x)',
                  'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/3.0 Safari/536.11',
                  'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
                  ]
    user_agent = random.choice(user_agent)
    headers = {

        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'User-Agent': user_agent,  # 设置随机请求头
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',

    }
    return headers


# 配置请求头
def session_requests_b():
    session = requests.Session()  # 设置session
    headers = head()
    session.headers.update(headers)  # 配置请求头
    # print(session.cookies)
    return session



def change_time(timeStamp):
    """
        :param timeStamp: 时间戳
        :return: 时间格式
    """
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    minuteTime = time.strftime("%H:%M", timeArray)
    dateTime = time.strftime("%Y-%m-%d",timeArray)
    return otherStyleTime, minuteTime,dateTime


if __name__ == '__main__':

    # 综合热门   https://api.bilibili.com/x/web-interface/popular?ps=30&pn=1
    # 每周必看   https://api.bilibili.com/x/web-interface/popular/series/one?number=200
    # 入站必刷   https://api.bilibili.com/x/web-interface/popular/precious?page_size=100&page=1
    # 排行榜     https://api.bilibili.com/x/web-interface/ranking/v2?rid=0&type=all
    # 音乐视频   https://api.bilibili.com/x/copyright-music-publicity/toplist/music_list?csrf=437cc966800000981911d86a4477fc70&list_id=44


    session = session_requests_b()
    page = session.get(url='https://api.bilibili.com/x/web-interface/ranking/v2?rid=0&type=all')
    page.encoding = "UTF-8"
    for obj in page.json().get('data').get('list'):
        title = obj.get('title')
        tname = obj.get('tname') # 标签
        short_link = obj.get('short_link') # 连接
        view = obj.get('stat').get('view') # 播放次数
        author = obj.get('owner').get('name') # 作者
        src = obj.get('pic') # 封面
        danmaku = obj.get('stat').get('danmaku') # 弹幕数
        like = obj.get('stat').get('like') # 点赞数
        share = obj.get('stat').get('share') # 分享数
        favorite = obj.get('stat').get('favorite') # 收藏数
        pubdate = obj.get('pubdate') # 发布时间
        reply = obj.get('stat').get('reply') # 评论数
        pub_location = obj.get('pub_location') # 地区
        print(title,author,change_time(pubdate)[2],pub_location)






