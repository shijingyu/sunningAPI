#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2017-5-9

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.AddchildAddRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.barpic='http://10.19.95.100/uimg/sop/commodity/201311290550007674_x.jpg'
a.pars=[{"parCode":"G00003","parValue":"23码"}]
a.itemCode='sjspbm'
a.supplierImgUrlA='http://10.19.95.100/uimg/sop/commodity/201311290550007674_x.jpg'
a.price='123'
a.parentProductCode='100000000'
a.barcode='1100'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)