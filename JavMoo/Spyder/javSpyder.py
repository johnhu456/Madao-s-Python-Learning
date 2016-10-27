# -*- coding:utf-8 -*-
import urllib2
from bs4 import BeautifulSoup


def getAVDiscHotList(page):
    hotListrequestURL = "https://avmo.pw/cn/popular/page/" + str(page)
    hotListrequest = urllib2.Request(hotListrequestURL)
    hotListSoup = BeautifulSoup(urllib2.urlopen(hotListrequest).read(), "html.parser")
    hotAVList = hotListSoup.findAll('a', attrs={"class": "movie-box"})
    for movieBox in hotAVList:
        uuid = str(movieBox['href']).split('/')[-1]
        overViewURL = movieBox.find(attrs={"class": "photo-frame"}).img["src"]
        print uuid
        print overViewURL
        getAVDiscDetail(uuid, overViewURL)


def getAVDiscDetail(uuid, overviewURL):
    detailRequestURL = "https://avmo.pw/cn/movie/" + str(uuid)
    detailReqeust = urllib2.Request(detailRequestURL)
    detailSoup = BeautifulSoup(urllib2.urlopen(detailReqeust).read(), "html.parser")
    mainInfo = detailSoup.find(attrs={"class": "col-md-9"}).find(attrs={"class": "bigImage"})
    title = mainInfo['title']
    bigCoverUrl = mainInfo['href']
    detailInfo = detailSoup.find('div', attrs={"class": "col-md-3"})
    codeInfo = detailInfo.find('span', text="识别码:").next_sibling.next_sibling
    lengthInfo = detailInfo.find('span', text="长度:").next_sibling
    directorInfo = detailInfo.find('span', text="导演:").next_sibling.next_sibling
    studioInfo = detailInfo.find('p', text="制作商: ").next_sibling.next_sibling
    publishInfo = detailInfo.find('p', text="发行商: ").next_sibling.next_sibling
    pubDateInfo = detailInfo.find('span', text="发行时间:").next_sibling
    genre = detailInfo.findAll('span', attrs={"class": "genre"})
    print genre
    # genreModel = Category.objects.get(uuid=genre)
    ############处理普通信息
    if codeInfo:
        code = codeInfo.string
        print code
    if pubDateInfo:
        pubDate = pubDateInfo.encode('utf-8').split('分')[0].lstrip()
        print pubDate
    if lengthInfo:
        length = lengthInfo.encode('utf-8').split('分')[0].lstrip()
        print length
    if directorInfo:
        directorName = directorInfo.string
        directorUUID = directorInfo['href'].encode('utf-8').split('/')[-1]
        print directorName
        print directorUUID
    if studioInfo:
        studioName = studioInfo.string
        studioUUID = studioInfo.a['href'].encode('utf-8').split('/')[-1]
        print studioName
        print studioUUID
    if publishInfo:
        publishName = publishInfo.string
        publishUUID = publishInfo.a['href'].encode('utf-8').split('/')[-1]
        print publishName
        print publishUUID
    print title
    print bigCoverUrl


# dateInfo = movieBox.find(attrs = {"class" : "photo-info"})
# print "详情：    " + str(movieBox['href'])
# print "片名：    " + str(info.img.attrs['title'])
# print "图片：    " + str(info.img.attrs['src'])
# print "番号：    " + str(dateInfo.span.date.string)
# print "日期：    " + str(dateInfo.span.date.next_sibling.next_sibling.string)
#
# #爬取详情
# detailUrl = str(movieBox['href'])
# detailRequest = urllib2.Request(detailUrl)
# detailSoup = BeautifulSoup(urllib2.urlopen(detailRequest).read())
# #print detailSoup
# detailInfo = detailSoup.find('div',attrs={"class" :"col-md-3"})
# timeInfo = detailInfo.find('span',text="长度:")
# director = detailInfo.find('span',text="导演:")
# studio = detailInfo.find('p',text="制作商: ")
# publish = detailInfo.find('p',text="发行商: ")
# genre = detailInfo.findAll('span',attrs={"class":"genre"})
# if timeInfo:
# 	print  "时长：   " + str(timeInfo.next_sibling)
# if director:
# 	print  "导演:    " + str(director.parent.a.text)
# 	print  "导演链接：" + str(director.parent.a['href'])
# if studio:
# 	print  "制作商：  " + str(studio.find_next('p').a.text)
# 	print  "制作商链接："+ str(studio.find_next('p').a['href'])
# if publish:
# 	print  "发行商：  " + str(publish.find_next('p').a.text)
# 	print  "发行商链接：" + str(publish.find_next('p').a['href'])
# print  "类别：   " +  str(genre) + "\n"
# print "时长：    " + str(timeInfo.find(text='时长'))
##print "导演链接： " + str(director.a['href'])  + "\n"


getAVDiscHotList(1)
