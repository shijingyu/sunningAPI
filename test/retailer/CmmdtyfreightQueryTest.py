#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2018-11-30

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.CmmdtyfreightQueryRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.appId='111111'
a.merchantCustNo='7017963441'
a.storeCode='59021'
a.cmmdtyList=[{"cmmdtyCode":"000000000100004919","factorySendFlag":"01","itemNo":"1","districtCode":"01","cityCode":"025","quantity":"1","distributionStrategy":"01","plantCode":"D025","distributorCode":"0000000000"}]

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)