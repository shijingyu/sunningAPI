# -*- coding: utf-8 -*-

'''

Created on 2018-11-16

@author: suning

'''

from suning.api.abstract import AbstractApi



class ProductdetailQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.productCode = None
        
        self.setParamRule({
        	'productCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryProductdetail'

    def getApiMethod(self):

        return 'suning.selfmarket.productdetail.query'



