# -*- coding:utf-8 -*-

import urllib2

from bs4 import BeautifulSoup

from mooApi.javmoo import Actress


def getDetailInfo(uuid):
    anActressDetailUrl = "https://avmo.pw/cn/star/" + uuid
    anActressDetailRequest =urllib2.Request(actressDetailUrl)
    anActressDetailSoup = BeautifulSoup(urllib2.urlopen(anActressDetailRequest).read(),"html.parser")
    info = anActressDetailSoup.find(attrs={"class":"photo-info"})
    #获取名字
    name = info.span.text
    others = info.findAll('p')
    modelInfo = dict(uuid=uuid, name=name)
    for details in others:
        detailKey = details.string.split(':')[0]
        detailValue = details.string.split(':')[-1]
        if detailKey == unicode('生日','utf-8'):
            modelInfo['birth'] = detailValue
        elif detailKey == unicode('年龄','utf-8'):
            modelInfo['age'] = detailValue
        elif detailKey == unicode('身高','utf-8'):
            height = detailValue.split('cm')[0]
            modelInfo['height'] = height
        elif detailKey == unicode('罩杯','utf-8'):
            modelInfo['cup'] = detailValue
        elif detailKey == unicode('胸围','utf-8'):
            bust = detailValue.split('cm')[0]
            modelInfo['bust'] = bust
        elif detailKey == unicode('腰围','utf-8'):
            waist = detailValue.split('cm')[0]
            modelInfo['waist'] = waist
        elif detailKey == unicode('臀围','utf-8'):
            hips = detailValue.split('cm')[0]
            modelInfo['hips'] = hips
        elif detailKey == unicode('出生地','utf-8'):
            city = detailValue
            modelInfo['city'] = city
        elif detailKey == unicode('爱好','utf-8'):
            hobby = detailValue
            modelInfo['hoby'] = detailValue
        else:
            pass
    anActress = Actress(modelInfo)
    anActress.save()
    print anActress

def getActrssList():
    actressBaseUrl = "https://avmo.pw/cn/actresses/page/"
    actressRequest = urllib2.Request(actressBaseUrl)
    actressSoup = BeautifulSoup(urllib2.urlopen(actressRequest).read(), "html.parser")
    lists = actressSoup.findAll('a', attrs={"class": "avatar-box"})
    for anActress in lists:
        anDetailUrl = anActress['href']
        actressDetailUrl = str(anDetailUrl)
        uuid = actressDetailUrl.split('/')[-1]
        getDetailInfo(uuid)
    #print anDetailUrl

