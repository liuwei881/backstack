# -*- coding: utf-8 -*-
__author__ = 'Hipeace86'
__datetime__ = '15-9-8'

import json
from lib.urlmap import urlmap
from lib.basehandler import RESTfulHandler
from tornado import web


@urlmap(r'/api/login')
class LoginHandler(RESTfulHandler):
    @web.asynchronous
    def get(self):
        account = self.get_argument('user', '')
        password = self.get_argument('password', '')
        if account == 'backtask' and password == 'backtask':
            self.Result['info'] = u'登陆成功'
            self.Result['status'] = 200
            self.xsrf_token
            self.set_secure_cookie('user',account,expires_days=0.5)
        else:
            self.Result['status'] = 404
        self.finish(self.Result)
