# -*- coding: utf-8 -*-

'''

Created on 2018-4-20

@author: suning

'''

from suning.api.abstract import AbstractApi



class MixconfirmorderAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderId = None
        self.subPaymentModes = None
        
        self.setParamRule({
        	'orderId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'addMixconfirmorder'

    def getApiMethod(self):

        return 'suning.govbus.mixconfirmorder.add'



