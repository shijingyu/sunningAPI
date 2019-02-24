# -*- coding: utf-8 -*-

'''

Created on 2019-1-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class AgreeexchangeUpdateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.supplierCode = None
        self.exchangeNo = None
        self.returnBackType = None
        self.wareHouseCode = None
        self.backinDate = None
        self.getBackPerson = None
        self.getBackPersonTel = None
        self.memo = None
        
        self.setParamRule({
        	'supplierCode':{'allow_empty':False},
        	'exchangeNo':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'updateAgreeexchange'

    def getApiMethod(self):

        return 'suning.selfmarket.agreeexchange.update'



