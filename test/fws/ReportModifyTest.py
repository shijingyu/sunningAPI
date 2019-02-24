#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2015-6-8

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.ReportModifyRequest()

a.setDomainInfo("opensit.cnsuning.com","80")
a.setAppInfo("95d3ca767adff5aa75adb0363de6f22b", "c0948c41fe19a358e50552cebc064514")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")

a.qtOrderCode='S01234567890'
a.qtCode='QT201501019876543210'
a.orderDetailId='12297'
a.itemCode='100015014'
a.itemName='312312'
a.itemDesc='3123123'
a.qtType='1'
a.qtStandard='GB2001'
a.qtFile='JVBERi0xLjUNCiW1tbW1DQoxIDAgb2JqDQ'
a.fileName='11.pdf'
a.qtExpiry='2015-01-01'
a.qtOrderStatus='3'
a.isPass='1'
a.described='wu'
a.memo='wu'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)