
# -*- coding:utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
from jokes.models import Joke

class JokesSpyder():
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
			print ("%s--%s" % (aStroy.content, aStroy.author))
			aStroy.save()


	def decodeSoup(self,oneSoup):
		qiushiStoryList = oneSoup.findAll(attrs = {"class" : "article block untagged mb15"})
		storyArray = []
		for aStroy in qiushiStoryList:
			content  = aStroy.find(attrs = {"class" : "content"}).getText('\n','<br/>')
			author = aStroy.find(attrs = {"class" : "author clearfix"}).h2.string
			stroy = Joke(content=content,author=author)
			storyArray.append(stroy)
		return storyArray

	#开始
	def start(self,page):
		self.getStorys(page)



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