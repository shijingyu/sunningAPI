# -*- coding: utf-8 -*-

'''

Created on 2018-8-22

@author: suning

'''

from suning.api.abstract import AbstractApi



class LgsstatusQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderId = None
        
        self.setParamRule({
        	'orderId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryLgsstatus'

    def getApiMethod(self):

        return 'suning.online.lgsstatus.query'



