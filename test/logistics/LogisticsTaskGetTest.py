#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2014-8-22

@author: suning
'''
import sys
sys.path.append("../../../api-sdk-python")

import suning.api as api

a=api.LogisticsTaskGetRequest()
a.ladingBill = "3"


f = a.getResponse()
print(f)
