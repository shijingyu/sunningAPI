# -*- coding: utf-8 -*-

'''

Created on 2018-12-17

@author: suning

'''

from suning.api.abstract import AbstractApi



class ShipTimeGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.addrDetail = None
        self.cityId = None
        self.districtId = None
        self.skuIds = None
        self.townId = None
        
        self.setParamRule({
        	'addrDetail':{'allow_empty':False},
        	'cityId':{'allow_empty':False},
        	'districtId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'getShipTime'

    def getApiMethod(self):

        return 'suning.govbus.shiptime.get'



