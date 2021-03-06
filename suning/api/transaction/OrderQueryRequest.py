# -*- coding: utf-8 -*-

'''

Created on 2015-2-3

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.endTime = None
        self.orderStatus = None
        self.startTime = None
        self.pageNo = None
        self.pageSize = None
        self.userName = None
        
        self.setParamRule({
        	'logisticExpressId':{'allow_empty':False},
        	'logisticExpressId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'orderQuery'

    def getApiMethod(self):

        return 'suning.custom.order.query'



