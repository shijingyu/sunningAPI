#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2016-5-27

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.SnInstallOrderAddRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("5c991b791c6e5c46f925c7c6171a22cc", "911bc7ef82abc19f065f256d7afef2d9")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.recordGuid='5D21BD501D63793FE1000000C0A8765D'
a.itemGuid='4FA025393D23C08CE1008000C0A8765B'
a.srvOrdId='7163370425'
a.srvOrdType='ZS01'
a.zb2bFlag='JS'
try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)