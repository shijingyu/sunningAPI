#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2018-2-8

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.AgentrechargeAddRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.channelId='10090375'
a.serialNumber='1709258****'
a.feeAmount='100'
a.reqSerial='100903752018010100000000'
a.reqTime='20180101235959'
a.reqSign='bf20cb51c95dccd72e66b5ff89111cc3'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)