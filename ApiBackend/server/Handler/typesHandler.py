#coding:utf-8
__author__ = 'yang'


from lib.urlmap import urlmap
from lib.basehandler import RESTfulHandler
from tornado import web
from task.Entity.TypesModel import Types,Typesattr
import json
from Common.functions import curDatetime,getTypesAttr
from sqlalchemy import desc,or_



@urlmap(r'/api/types\/?([0-9]*)')
class TypesHandler(RESTfulHandler):
    @web.asynchronous
    def get(self, ident=0):
        if ident:
            try:
                objTypes = Types.query.get(ident)
                self.Result['rows'] = objTypes.toDict()
                attr = self.db.query(Typesattr).filter(Typesattr.TypeId==objTypes.TypeId).all()
                self.Result['attrs'] = map(lambda obj: obj.toDict(), attr)
            except:
                self.Result['status'] = 404
                self.Result['info'] = 'No Row Found'
        else:
            page = int(self.get_argument('page', 1))
            searchKey = self.get_argument('searchKey', None)
            pagesize = int(self.get_argument('pagesize', self._PageSize))
            totalquery = self.db.query(Types.TypeId)
            typeslistObj = self.db.query(Types)
            if searchKey:
                totalquery = totalquery.filter(Types.Name.like('%%%s%%' % searchKey))
                typeslistObj   = typeslistObj.filter(Types.Name.like('%%%s%%' % searchKey))

            self.Result['total'] = totalquery.count()
            listTypes = typeslistObj.order_by(desc(Types.CreateTime)).limit(pagesize).offset((page - 1) * pagesize).all()
            listTypes = map(lambda obj: obj.toDict(), listTypes)
            tmp = []
            for i in listTypes:
                attr = self.db.query(Typesattr).filter(Typesattr.TypeId == i['TypeId']).all()
                i['attrs'] = map(lambda obj: obj.toDict(), attr)
                tmp.append(i)
            self.Result['rows'] = tmp
        self.finish(self.Result)


    @web.asynchronous
    def post(self, ident=0):
        data = json.loads(self.request.body)
        objTypes = Types()
        objTypes.Name = data['params'].get('Name', None)
        objTypes.EName= data['params'].get('EName', None)
        objTypes.Desc = data['params'].get('Desc', None)
        objTypes.Status = data['params'].get('Status', 1)
        objTypes.CreateId = 1
        objTypes.CreateTime = curDatetime()
        self.db.add(objTypes)
        self.db.flush()
        attrs = data['params'].get('attrs', None)
        if attrs:
            attrList = attrs.split(',')
            for attr in attrList:
                if attr:
                    attrObj = Typesattr()
                    attrObj.TypeId = objTypes.TypeId
                    attrObj.Status = 1
                    attrObj.Name   = attr
                    self.db.add(attrObj)
        self.db.commit()
        self.Result['rows'] = 1
        self.Result['info'] = u'添加成功'
        self.finish(self.Result)

    @web.asynchronous
    def put(self, ident=0):
        data = json.loads(self.request.body)
        objType = Types.query.get(ident)
        if ident and objType:
            objType.Desc = data['params'].get('Desc', None)
            objType.UpdateId = 2
            objType.UpdateTime = curDatetime()
            print objType
            self.db.add(objType)
            self.db.commit()
        self.Result['rows'] = 1
        self.Result['info'] = u'修改成功'
        self.finish(self.Result)



# 生成类型字段的js文件
@urlmap(r'/api/makeetcjs')
class TaskHandler(RESTfulHandler):
    @web.asynchronous
    def get(self):
        from sqlalchemy import and_
        etcStr = {}
        attrRows = self.db.query(Types.EName,Typesattr.AttrId,Typesattr.Name).join(Typesattr,Typesattr.TypeId==Types.TypeId).filter(and_(Typesattr.Status==1,Types.Status==1)).all()
        for i in attrRows:
            kk = i[0].encode('utf-8')
            if not etcStr.has_key(kk):
                etcStr[kk] = []
            etcStr[kk].append("{'AttrId':'%s','Name':'%s'}" % i[1:])
        jsStr = ';'.join(['var %s=%s' % (k,'[' + ','.join(v) + ']') for k,v in etcStr.items()]) + ';'
        hd = open('../asserts/etc/attrsConf.js','w')
        hd.write(jsStr)
        hd.close()
        self.Result['info'] = 'make OK!!'
        self.finish(self.Result)
