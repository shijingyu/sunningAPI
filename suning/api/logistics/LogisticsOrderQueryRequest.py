# -*- coding: utf-8 -*-

'''

Created on 2014-8-22

@author: suning

'''

from suning.api.abstract import AbstractApi



class LogisticsOrderQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.startTime = None
        self.endTime = None
        self.pageSize = None
        self.pageNo = None



    def getApiBizName(self):

        return 'queryLogisticsOrder'



    def getApiMethod(self):

        return 'suning.custom.logisticsorder.query'



