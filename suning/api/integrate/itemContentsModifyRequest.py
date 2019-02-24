# -*- coding: utf-8 -*-

'''

Created on 2018-10-22

@author: suning

'''

from suning.api.abstract import AbstractApi



class itemContentsModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.afterSaleServiceDec = None
        self.assortCode = None
        self.childItem = None
        self.cmTitle = None
        self.detailModule = None
        self.introduction = None
        self.itemCode = None
        self.mobile = None
        self.mobileNew = None
        self.packingList = None
        self.peopleNum = None
        self.productCode = None
        self.saleDate = None
        self.saleSet = None
        self.sellPoint = None
        self.sourceCountry = None
        self.supplierImg10Url = None
        self.supplierImg1Url = None
        self.supplierImg2Url = None
        self.supplierImg3Url = None
        self.supplierImg4Url = None
        self.supplierImg5Url = None
        self.supplierImg6Url = None
        self.supplierImg7Url = None
        self.supplierImg8Url = None
        self.supplierImg9Url = None
        self.transparent = None
        
        self.setParamRule({
        	'productCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'itemContents'

    def getApiMethod(self):

        return 'suning.integrate.itemcontents.modify'



