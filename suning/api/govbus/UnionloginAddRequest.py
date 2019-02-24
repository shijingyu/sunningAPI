# -*- coding: utf-8 -*-

'''

Created on 2019-1-25

@author: suning

'''

from suning.api.abstract import AbstractApi



class UnionloginAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.comabb = None
        self.comName = None
        self.extra = None
        self.sysCode = None
        self.tragetUrl = None
        self.uid = None
        
        self.setParamRule({
        	'sysCode':{'allow_empty':False},
        	'uid':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'addUnionlogin'

    def getApiMethod(self):

        return 'suning.govbus.unionlogin.add'



