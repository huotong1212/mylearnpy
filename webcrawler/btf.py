#coding=utf-8


from numpy import random
import requests
import time
from bs4 import BeautifulSoup  #导入BeautifulSoup 模块
import pandas as pd

class WandingEarth():

   def __init__(self):
       self.init_url = "https://movie.douban.com/subject/26266893/comments?start=0&limit=20&sort=new_score&status=P"  # 请求网址
       self.folder_path = "C:\D\WandingEarth"  # 想要存放的文件目录
       self.votes = []
       self.user_names = []
       self.comments = []
       self.dates = []
       self.ratings = []

   def sendUrl(self,headers,cookies,num):
       # print(cookies)
       r = requests.get(self.init_url, headers=header, cookies=cookies)
       soup = BeautifulSoup(r.text, 'lxml')
       all_comments = soup.find(id="comments").find_all('div',class_= "comment") #找到所有的comment

       index = 1;
       for comment in all_comments:
           print("这是第%d条评论"%(index+num))
           # print(comment.contents)
           vote = comment.find('span',class_= "votes").string
           self.votes.append(vote)
           user_name = comment.find('span',class_= "comment-info").find('a').string
           self.user_names.append(user_name)
           date = comment.find('span',class_= "comment-time")['title']
           self.dates.append(date)
           self.comments.append(comment.find('span',class_= "short").string)
           if comment.select_one('.rating'):
               self.ratings.append(comment.select_one('.rating')['title'])
           else:
               self.ratings.append("暂无评分")
           index+=1

       #print('html',r.text)

Earth = WandingEarth()
header = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}  # 给请求指定一个请求头来模拟chrome浏览器
f_cookies = open('cookies.txt', 'r')
cookies = {}

for line in f_cookies.read().split(';'):
   name, value = line.strip().split('=', 1)
   cookies[name] = value

start = 0
for i in range(26):
   print("开始爬取第%d页的数据.............."%(i+1))
   url = "https://movie.douban.com/subject/26266893/comments?start="+str(start)+"&limit=20&sort=new_score&status=P"
   Earth.init_url = url;
   Earth.sendUrl(headers=header, cookies=cookies, num=i*20)
   start += 20
   time.sleep(random.random())
   # time.sleep(1 + float(random.randint(1, 100)) / 20)

print("爬取结束-----------------------")
print(Earth.user_names)
result={'用户昵称':Earth.user_names,'时间':Earth.dates,'评分':Earth.ratings,'评论':Earth.comments,'点赞':Earth.votes,}
results=pd.DataFrame(result)
results.info()
results.to_excel('豆瓣_流浪地球.xlsx')