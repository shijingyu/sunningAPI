# -*- coding: utf-8 -*-

'''

Created on 2018-10-26

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderitemQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.companyCusNo = None
        self.dateType = None
        self.endDate = None
        self.orderItemStatus = None
        self.startDate = None
        self.pageNum = None
        self.pageLen = None
        
        self.setParamRule({
        	'dateType':{'allow_empty':False},
        	'endDate':{'allow_empty':False},
        	'orderItemStatus':{'allow_empty':False},
        	'startDate':{'allow_empty':False},
        	'pageNum':{'allow_empty':False},
        	'pageLen':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryOrderitem'

    def getApiMethod(self):

        return 'suning.govbus.orderitem.query'



