# -*- coding: utf-8 -*-

'''

Created on 2018-12-17

@author: suning

'''

from suning.api.abstract import AbstractApi



class CmmdtydetailpriceQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.chanId = None
        self.city = None
        self.cmmdtyInfo = None
        self.county = None
        self.province = None
        self.village = None
        
        self.setParamRule({
        	'chanId':{'allow_empty':False},
        	'city':{'allow_empty':False},
        	'county':{'allow_empty':False},
        	'province':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryCmmdtydetailprice'

    def getApiMethod(self):

        return 'suning.online.cmmdtydetailprice.query'



