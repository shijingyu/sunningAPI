#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2018-11-22

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.CulitemcontentsModifyRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.afterSaleServiceDec='七天内包退换'
a.alertQty='5'
a.assortCode='11111111'
a.cmTitle='商品标题'
a.detailModule=[{"content":"模块化详情内容","num":"1","moduleId":"123","moduleName":"模块名称","type":"模板类型"}]
a.introduction='单一详情'
a.invQty='10'
a.itemCode='7775'
a.peopleNum='2'
a.pingouPrice='20.00'
a.price='20.00'
a.productCode='105560068'
a.saleDate='2014-01-06'
a.saleSet='0'
a.sellPoint='十万个为什么'
a.supplierImgAUrl='商家商品图片1地址url'
a.supplierImgBUrl='商家商品图片2地址url'
a.supplierImgCUrl='商家商品图片3地址url'
a.supplierImgDUrl='商家商品图片4地址url'
a.supplierImgEUrl='商家商品图片5地址url'
a.transparent='https://uimgpre.cnsuning.com/uimg/sop/commodity/151495935813172557645370_x.png'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)