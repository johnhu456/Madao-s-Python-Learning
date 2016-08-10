# -*- coding:utf-8 -*-
import urllib
import urllib2
from bs4 import BeautifulSoup


class QiushiStory():
	def __init__(self,content,author,**other):
		self.content = content
		self.author = author
		if hasattr(other,"imageURL"):
			self.imgURL = other['imageURL']

class SpyderQiushi():
	def __init__(self):
		self.defaultPage = 1
		self.baseURL = "http://www.qiushibaike.com/hot/page/"
		self.header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
		self.enabled = False

	#获得某一页的数据
	def getStorys(self,pageNumber):
		url = self.baseURL + str(pageNumber)
		request = urllib2.Request(url,None,self.header)
		response = urllib2.urlopen(request)
		responseSoup = BeautifulSoup(response.read())
		for aStroy in self.decodeSoup(responseSoup):
			print "按回车显示一条段子"
			whatInput = raw_input()
			print whatInput
			if  whatInput == 'Q':
				return
			else :
				print "=============分割线=================\n"
				print ("%s--%s"%(aStroy.content,aStroy.author))

	def decodeSoup(self,oneSoup):
		qiushiStoryList = oneSoup.findAll(attrs = {"class" : "article block untagged mb15"})
		storyArray = []
		for aStroy in qiushiStoryList:
			content  = aStroy.find(attrs = {"class" : "content"}).getText('\n','<br/>')
			author = aStroy.find(attrs = {"class" : "author clearfix"}).h2.string
			image = aStroy.find(attrs = {"class" : "thumb"})
			imgURL = None
			if image != None : 
				imgURL = image.a.img['src']
			#没有内容，用imageURL代替content
			if ((content == None) & (imgURL != None)):
				content = imgURL
			elif (imgURL != None):
				content = ("%s     image:%s"%(content,imgURL))
			stroy = QiushiStory(content,author)
			storyArray.append(stroy)
		return storyArray

	#开始
	def start(self):
		self.getStorys(1)


aSpyder = SpyderQiushi()
aSpyder.start()


# try:
# 	headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
# 	request = urllib2.Request(baikeUrl,None,headers)
# 	response = urllib2.urlopen(request)

# 	soup = BeautifulSoup(response.read())
# 	print soup.name
# 	# print soup.p
# 	print soup.tag
# 	def test1():
# 		baikeList =  soup.findAll(attrs = {"class" : "article block untagged mb15"})
# 		for first in baikeList:
# 			print first.find(attrs = {"class" : "author clearfix"}).next_element
# 			print first.next_element
# 			print first.find(attrs = {"class" : "content"}).string
# 			# print first.a.img.parents
# 			# stats_vote = first.find(attrs = {"class" : "stats-vote"})
# 			# stats_comment = first.find(attrs = {"class" : "stats-comments"})
# 			# votes_num = stats_vote.find(attrs = {"class" : "number"})
# 			# comments_num = stats_comment.find(attrs = {"class" : "number"})
# 			# print votes_num.string + "Like"
# 			# print comments_num.string + "Comments"
# 			# print "\n"
# 	def test2():
# 		baikeList = soup.div
# 		print baikeList.tag

# 	test1()







# except urllib2.URLError, e:
# 	if hasattr(e,"code"):
# 		print(e.code)
# 	if hasattr(e,"reason"):
# 		print(e.reason)