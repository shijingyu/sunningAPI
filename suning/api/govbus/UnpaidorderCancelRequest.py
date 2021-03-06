# -*- coding: utf-8 -*-

'''

Created on 2017-12-19

@author: suning

'''

from suning.api.abstract import AbstractApi



class UnpaidorderCancelRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderId = None
        
        self.setParamRule({
        	'orderId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'cancelUnpaidorder'

    def getApiMethod(self):

        return 'suning.govbus.unpaidorder.cancel'



