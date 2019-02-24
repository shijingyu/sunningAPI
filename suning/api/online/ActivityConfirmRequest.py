# -*- coding: utf-8 -*-

'''

Created on 2019-2-20

@author: suning

'''

from suning.api.abstract import AbstractApi



class ActivityConfirmRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityInfo = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'confirmActivity'

    def getApiMethod(self):

        return 'suning.online.activity.confirm'



