#coding:utf-8
__author__ = 'yang'

import time
from task.Entity.TypesModel import Typesattr
from sqlalchemy import and_


def curDatetime():
    return time.strftime('%Y-%m-%d %X', time.localtime())


def getTypesAttr(TypeId):
    typesattrModel = Typesattr()
    objs = typesattrModel.query.filter(and_(Typesattr.TypeId==TypeId,Typesattr.Status==1)).all()
    if objs:
        lists = []
        for r in objs:
            rows = r.toDict()
            lists.append({'AttrId':rows['AttrId'],'Name':rows['Name']})
        return lists
    else:
        return False

def getStatusIdDesc(AttrId):
    if AttrId:
        typesattrModel = Typesattr()
        row = typesattrModel.query.get(AttrId)
        if row:
            return row.toDict()['Name']
        else:
            return AttrId
    return ''

# 用于处理连表查询结果中的时间格式
# def timeDeal(obj):
#     for i in dir(obj)[0:8]:
#         if i.endswith('Time'):
#             stime = getattr(obj,i)
#             delattr(obj,i)
#             if stime:
#                 setattr(obj,i,stime.strftime('%Y-%m-%d %H:%M:%S'))
#             else:
#                 setattr(obj,i,'')
#     return obj


