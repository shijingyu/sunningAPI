# -*- coding: utf-8 -*-

'''

Created on 2018-12-17

@author: suning

'''

from suning.api.abstract import AbstractApi



class GetspecialgoodsQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.categoryId = None
        
        self.setParamRule({
        	'categoryId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryGetspecialgoods'

    def getApiMethod(self):

        return 'suning.govbus.getspecialgoods.query'



