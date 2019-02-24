#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2014-10-17

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.QueryPriceReduceRequest()

a.timeType='1'
a.startTime='2014-09-09 12:00:00'
a.endTime='2014-09-19 12:00:00'
a.pageNo='2'
a.pageSize='3'
a.acStatusCode='1'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)