# -*- coding: utf-8 -*-
"""
Users 
@version:1.0.20150908
@author: Hipeace86
"""

import json
from lib.urlmap import urlmap
from lib.basehandler import RESTfulHandler
from tornado import web
from Users.Entity.UsersModel import Users


@urlmap(r'/api/users\/?([0-9]*)')
class UsersHandler(RESTfulHandler):
    @web.asynchronous
    def get(self, ident=0):
        if ident:
            try:
                objusers = Users.query.get(ident)
                self.Result['rows'] = objusers.toDict()
                self.Result['total'] = 1
            except:
                self.Result['status'] = 404
                self.Result['info'] = 'No Row Found'
        else:
            page = int(self.get_argument('page', 1))
            pagesize = int(self.get_argument('pagesize', self._PageSize))
            totalquery = self.db.query(Users.UserId)
            lstuserss = Users.query.limit(pagesize).offset((page - 1) * pagesize).all()
            self.Result['total'] = totalquery.count()
            self.Result['rows'] = map(lambda obj: obj.toDict(), lstuserss)
            self.finish(self.Result)

    @web.asynchronous
    def post(self, ident=0):
        data = json.loads(self.request.body)

        objusers = Users()

        objusers.NickName = data['params'].get('NickName', None)
        objusers.Account = data['params'].get('Account', None)
        objusers.Password = data['params'].get('Password', None)
        objusers.Email = data['params'].get('Email', None)
        objusers.IsAdmin = data['params'].get('IsAdmin', None)
        objusers.IsDelete = data['params'].get('IsDelete', None)

        self.db.add(objusers)
        self.db.commit()
        self.Result['rows'] = 1
        self.Result['info'] = u'添加成功'
        self.finish(self.Result)

    @web.asynchronous
    def put(self, ident=0):
        data = json.loads(self.request.body)
        objusers = Users.query.get(ident)

        if objusers:
            objusers.NickName = data['params'].get('NickName', None)
            objusers.Account = data['params'].get('Account', None)
            objusers.Password = data['params'].get('Password', None)
            objusers.Email = data['params'].get('Email', None)
            objusers.IsAdmin = data['params'].get('IsAdmin', None)
            objusers.IsDelete = data['params'].get('IsDelete', None)

            self.db.add(objusers)
            self.db.commit()
        self.Result['rows'] = 1
        self.Result['info'] = u'修改成功'
        self.finish(self.Result)

    @web.asynchronous
    def delete(self, ident):
        self.Result['info'] = u'删除成功'
        self.finish(self.Result)
