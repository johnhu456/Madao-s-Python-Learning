# -*- coding:utf-8 -*-

import urllib2
from bs4 import BeautifulSoup
from mooAPI.models import CategoryGroup,Category

def getCategoryGroupList():
    genreBaseUrl = "https://avmo.pw/cn/genre"
    genreBaseRequest = urllib2.Request(genreBaseUrl)
    genreBaseSoup = BeautifulSoup(urllib2.urlopen(genreBaseRequest).read(), "html.parser")
    rawGroup = genreBaseSoup.find('div',attrs={"class":"pt-10"})
    groups = rawGroup.findAll('h4')
    for aGroup in groups:
        newGroup = CategoryGroup(groupName=aGroup.text)
        newGroup.save()
        details = aGroup.next_sibling.next_sibling.findAll(attrs={"class":"col-lg-2"})
        for aCategory in details:
            uuid = str(aCategory['href']).split('/')[-1]
            newCatrgory = Category(categoryName=aCategory.text,uuid=uuid,group=newGroup)
            newCatrgory.save()
