# -*- coding: utf-8 -*-

'''

Created on 2019-1-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderCreateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.platFormTrade = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'createOrder'

    def getApiMethod(self):

        return 'suning.online.order.create'



