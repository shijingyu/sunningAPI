# -*- coding: utf-8 -*-

'''

Created on 2018-11-16

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderDetailGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderId = None
        
        self.setParamRule({
        	'orderId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getOrderDetail'

    def getApiMethod(self):

        return 'suning.govbus.orderdetail.get'



