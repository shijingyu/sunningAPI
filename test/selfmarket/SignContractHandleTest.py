#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2015-1-19

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.SignContractHandleRequest()

a.contractCode='ssdfds'
a.supplierCode='sdfdsf'
a.contractText='dsfds'
a.signText='dsfds'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)