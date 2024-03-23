'''
Descripttion:  获取网页下的url
version: v1.0
Author: Ryan Zhang (gitHub.com/hz157)
Date: 2024-03-23 23:28:19
LastEditors: Ryan Zhang
LastEditTime: 2024-03-23 23:30:30
'''
from email import header
from urllib import request, parse
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests
import os


# 获取页面所有的标签
def getURL(url):
    # 获取站点的Title
    source_code = requests.get(url)
    soup = BeautifulSoup(source_code.text)
    siteTitle = soup.title.string

    response = request.urlopen(url)
    page = response.read()
    soup = BeautifulSoup(page, 'html.parser')
    # tagh3 = soup.find_all('h3')  # 返回 list
    tagh3 = soup.find_all('a')  # 获取所有 a 标签下内容，返回 list
    hrefs = []
    for h3 in tagh3:
        # href = h3.find('a').get('href')
        try:
            href = h3.get('href')  # 获取 a 标签下 href 的属性值（即：url）
        except:
            pass
        else:
            hrefs.append(href)
    hrefs = list({}.fromkeys(hrefs).keys())  # 去重
    for i in hrefs:
        print(i)
    
    # 写文件
    writeText(siteTitle,hrefs)


# 写入txt记录爬虫抓到的网站
def writeText(textName, urlData):
    # 获取文件运行路径
    path = os.path.dirname(os.path.realpath(__file__)) + "\\"
    # 创建文本文件
    Text = open(path + textName+".txt","w", encoding='utf-8')
    # 遍历数据写入
    for i in urlData:
        Text.write(i + "\n")
    # 关闭文件
    Text.close


# 请求头 防止默认请求头被系统认定为是机器人
header = {'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding' : 'gzip, deflate, br',
    'Accept-Language' : 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36}'}



if __name__=='__main__':
    url = input("请输入URL:\n")
    getURL(url)
    
    
