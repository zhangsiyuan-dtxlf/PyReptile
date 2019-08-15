#conding = gbk
import urllib.request
import re
import urllib
import time

from chardet import detect

qzbm = r'gbk'#网页编码
zjlj = r'<dd><a href="(.*?)">(.*?)</a></dd>'  #章节链接和标题通配符
zjnr = r'<div id="content">(.*?)</div>'       #章节内容通配符
nrqc1 = r'&nbsp;'                             #内容中去除的内容1
nrqc2 = r'<br />'                             #内容中去除的内容2
wzzyurl = r'https://www.biduo.cc/biquge/3_3957/'#网站主页url
qUrl = r'https://www.biduo.cc/biquge/3_3957/'                 #内容页链接前置链接
wbname = r'我的测试.txt'                #生成的文本文件名字
def download_novel():
    #获取页面源代码
    url = wzzyurl
    html = urllib.request.urlopen(url).read()

    #指定编码
    html = html.decode(qzbm)
    #获取章节链接和小说的标题
    # .*? 匹配所有 分组匹配 (.*?)匹配显示
    #获取章节列表
    #获取章节链接

    reg = zjlj
    urls = re.findall(reg,html)
    #()元组 []列表
    #print(urls[1129])

    #for url in urls[411:]: #根据中断的章节数匹配数组

    for url in urls[411:]:
        #章节链接
        sUrl = qUrl + str(url[0])
        #urlList = []
        d = [sUrl,str(url[1])]
        if d == None:
            break
        #c = tuple(d)
        #urlList.append(c)
        novel_url = d[0]
        #章节标题
        novel_title = d[1]
        
        del d
        #novel_url,novel_title = url
        #获取章节页面源码
        chapt = urllib.request.urlopen(novel_url).read()
        chapt_html = chapt.decode(qzbm)
        #获取章节内容
        reg = zjnr
        #多行匹配 s
        reg = re.compile(reg,re.S)
        chapt_content = re.findall(reg, chapt_html)
        print(chapt)

        if chapt_content == None:
            break
        #数据清洗
        chapt_content = chapt_content[0].replace(nrqc1,'')
        #chapt_content 转换成字符串不是列表了
        chapt_content = chapt_content.replace(nrqc2, '')
        # 下载到本地
        print('正在下载 %s'%novel_title)
        #f = open('{}.txt'.format(novel_title),'w')
        #f.write(chapt_content)
        #f.close()
        #with open('{}.txt'.format(novel_title),'w') as f:
        #   f.write(chapt_content+'\n'+'\n')
              
        with open(wbname,'a',encoding = 'UTF-8') as f:
            f.write(novel_title+'\n'+'\n')
            f.write(chapt_content+'\n'+'\n')
            time.sleep(3)
            del chapt_content
            del novel_title

download_novel()

