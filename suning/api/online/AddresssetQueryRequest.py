# -*- coding: utf-8 -*-

'''

Created on 2018-8-22

@author: suning

'''

from suning.api.abstract import AbstractApi



class AddresssetQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.addressHierarchy = None
        self.provinceCode = None
        
        self.setParamRule({
        	'addressHierarchy':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryAddressset'

    def getApiMethod(self):

        return 'suning.online.addressset.query'



