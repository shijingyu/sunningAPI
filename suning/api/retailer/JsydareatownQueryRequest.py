# -*- coding: utf-8 -*-

'''

Created on 2019-1-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class JsydareatownQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.id = None
        self.token = None
        
        self.setParamRule({
        	'id':{'allow_empty':False},
        	'token':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryJsydareatown'

    def getApiMethod(self):

        return 'suning.retailer.jsydareatown.query'



