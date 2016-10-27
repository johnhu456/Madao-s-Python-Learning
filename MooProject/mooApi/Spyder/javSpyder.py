# -*- coding:utf-8 -*-
reload(sys)
sys.setdefaultencoding( "utf-8" )

page = 1
requestURL = "https://avmo.pw/cn/popular/page/" + str(page)
reqeust = urllib2.Request(requestURL)
htmlSoup = BeautifulSoup(urllib2.urlopen(reqeust).read())
allAVList = htmlSoup.findAll('a',attrs = {"class" : "movie-box"})
for movieBox in allAVList:
	info = movieBox.find(attrs = {"class" : "photo-frame"})
	dateInfo = movieBox.find(attrs = {"class" : "photo-info"})
	print "详情：    " + str(movieBox['href'])
	print "片名：    " + str(info.img.attrs['title'])
	print "图片：    " + str(info.img.attrs['src'])
	print "番号：    " + str(dateInfo.span.date.string)
	print "日期：    " + str(dateInfo.span.date.next_sibling.next_sibling.string)

	#爬取详情
	detailUrl = str(movieBox['href'])
	detailRequest = urllib2.Request(detailUrl)
	detailSoup = BeautifulSoup(urllib2.urlopen(detailRequest).read())
	#print detailSoup
	detailInfo = detailSoup.find('div',attrs={"class" :"col-md-3"})
	timeInfo = detailInfo.find('span',text="长度:")
	director = detailInfo.find('span',text="导演:")
	studio = detailInfo.find('p',text="制作商: ")
	publish = detailInfo.find('p',text="发行商: ")
	genre = detailInfo.findAll('span',attrs={"class":"genre"})
	if timeInfo:
		print  "时长：   " + str(timeInfo.next_sibling)
	if director:
		print  "导演:    " + str(director.parent.a.text)
		print  "导演链接：" + str(director.parent.a['href'])
	if studio:
		print  "制作商：  " + str(studio.find_next('p').a.text)
		print  "制作商链接："+ str(studio.find_next('p').a['href'])
	if publish:
		print  "发行商：  " + str(publish.find_next('p').a.text)
		print  "发行商链接：" + str(publish.find_next('p').a['href'])
	print  "类别：   " +  str(genre) + "\n"
	#print "时长：    " + str(timeInfo.find(text='时长'))
	##print "导演链接： " + str(director.a['href'])  + "\n"


# print allAVList