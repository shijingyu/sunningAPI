#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2018-1-11

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.ItemQueryRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.applyStatus='11'
a.brandCode='I678'
a.categoryCode='R3301002'
a.cmTitle='商品标题'
a.contentStatus='12'
a.endTime='2015-11-27 16:21:38'
a.itemCode='123'
a.pageNo='1'
a.pageSize='10'
a.productCode='140001234'
a.startTime='2015-11-27 16:21:38'
a.supplierCodeAsk='12345678912'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)