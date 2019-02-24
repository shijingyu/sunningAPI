# -*- coding: utf-8 -*-
'''
Created on 2014-5-27, Auto Generated 
@author: momo
'''
from suning.api.abstract import AbstractApi

class ItemQueryRequest(AbstractApi):
    '''
    '''
    def __init__(self):
        AbstractApi.__init__(self)
        self.status = None
        self.pageSize = None
        self.categoryCode = None
        self.brandCode = None
        self.pageNo = None

    def getApiBizName(self):
        return 'item'

    def getApiMethod(self):
        return 'suning.custom.item.query'

