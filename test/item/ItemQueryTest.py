#!usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../../../api-sdk-python")

import suning.api as api
'''
Created on 2014年6月6日

@author: dd
'''
a = api.ItemQueryRequest()
a.status = ''

a.pageSize = 20

a.categoryCode = 'R3301006'

a.brandCode = 'A120'

a.pageNo = 1

try:
    
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)