#coding:utf-8
__author__ = 'yang'


from lib.urlmap import urlmap
from lib.basehandler import RESTfulHandler
from tornado import web,gen
from server.Entity.ServerModel import ServerList,MysqlList,NginxList
import json
from Common.functions import curDatetime,getTypesAttr
from sqlalchemy import desc,or_



@urlmap(r'/api/server\/?([0-9]*)')
class ServerHandler(RESTfulHandler):
    @web.asynchronous
    def get(self, ident):
        if ident:
            try:
                objServer = ServerList.query.get(ident)
                self.Result['rows'] = objServer.toDict()
                self.Result['total'] = 1
            except:
                self.Result['status'] = 404
                self.Result['info'] = 'No Row Found'
        else:
            page = int(self.get_argument('page', 1))
            searchKey = self.get_argument('searchKey', None)
            pagesize = int(self.get_argument('pagesize', self._PageSize))
            totalquery = self.db.query(ServerList.ServerId)
            ServerlistObj = self.db.query(ServerList)
            if searchKey:
                totalquery = totalquery.filter(or_(ServerList.NameServer.like('%%%s%%' % searchKey),ServerList.Ip0==searchKey,ServerList.Ip1==searchKey,ServerList.Ip2==searchKey))
                ServerlistObj = ServerlistObj.filter(or_(ServerList.NameServer.like('%%%s%%' % searchKey),ServerList.Ip0==searchKey,ServerList.Ip1==searchKey))

            self.Result['total'] = totalquery.count()
            serverTask = ServerlistObj.order_by(desc(ServerList.CreateTime)).limit(pagesize).offset((page - 1) * pagesize).all()
            self.Result['rows'] = map(lambda obj: obj.toDict(), serverTask)
        self.finish(self.Result)


    @web.asynchronous
    def post(self,ident=0):
        data = json.loads(self.request.body)
        objTask = ServerList()

        objTask.NameServer = data['params'].get('NameServer', None)
        objTask.Location= data['params'].get('Location', None)
        objTask.OsVersion = data['params'].get('OsVersion', None)
        objTask.Memory = data['params'].get('Memory', None)
        objTask.Disk = data['params'].get('Disk', None)
        objTask.Cpu = data['params'].get('Cpu', None)
        objTask.Sorts = data['params'].get('Sorts', None)
        objTask.BandWidth = data['params'].get('BandWidth', None)
        objTask.Ip0 = data['params'].get('Ip0', None)
        objTask.Ip1 = data['params'].get('Ip1', None)
        objTask.Ip2 = data['params'].get('Ip2', None)
        objTask.CreateId = 1
        objTask.CreateTime = curDatetime()
        self.db.add(objTask)
        self.db.commit()
        self.Result['rows'] = 1
        self.Result['info'] = u'添加成功'
        self.finish(self.Result)

    @web.asynchronous
    def put(self, ident=0):
        data = json.loads(self.request.body)
        objTask = ServerList.query.get(ident)
        if ident and objTask:
            objTask.NameServer= data['params'].get('NameServer', None)
            objTask.Location= data['params'].get('Location', None)
            objTask.OsVersion = data['params'].get('OsVersion', None)
            objTask.Memory = data['params'].get('Memory', None)
            objTask.Disk = data['params'].get('Disk', None)
            objTask.Cpu = data['params'].get('Cpu', None)
            objTask.Sorts = data['params'].get('Sorts', None)
            objTask.BandWidth = data['params'].get('BandWidth', None)
            objTask.Ip0 = data['params'].get('Ip0', None)
            objTask.Ip1 = data['params'].get('Ip1', None)
            objTask.Ip2 = data['params'].get('Ip2', None)
            objTask.UpdateId = 2
            objTask.UpdateTime = curDatetime()
            self.db.add(objTask)
            self.db.commit()
        self.Result['rows'] = 1
        self.Result['info'] = u'修改成功'
        self.finish(self.Result)

    @web.asynchronous
    def delete(self, ident):
        self.db.query(ServerList).filter(ServerList.ServerId==ident).delete()
        self.db.commit()
        self.Result['info'] = u'删除成功'
        self.finish(self.Result)

@urlmap(r'/api/nginx\/?([0-9]*)')
class NginxHandler(RESTfulHandler):
    @web.asynchronous
    def get(self, ident):
        if ident:
            try:
                objServer = NginxList.query.get(ident)
                self.Result['rows'] = objServer.toDict()
                self.Result['total'] = 1
            except:
                self.Result['status'] = 404
                self.Result['info'] = 'No Row Found'
        else:
            page = int(self.get_argument('page', 1))
            searchKey = self.get_argument('searchKey', None)
            pagesize = int(self.get_argument('pagesize', self._PageSize))
            totalquery = self.db.query(NginxList.NginxId)
            ServerlistObj = self.db.query(NginxList)
            if searchKey:
                totalquery = totalquery.filter(or_(NginxList.NameServer.like('%%%s%%' % searchKey),NginxList.DomainName==searchKey,NginxList.DomainIp==searchKey))
                ServerlistObj = ServerlistObj.filter(or_(NginxList.NameServer.like('%%%s%%' % searchKey),NginxList.DomainName==searchKey,NginxList.DomainIp==searchKey))

            self.Result['total'] = totalquery.count()
            serverTask = ServerlistObj.order_by(desc(NginxList.CreateTime)).limit(pagesize).offset((page - 1) * pagesize).all()
            self.Result['rows'] = map(lambda obj: obj.toDict(), serverTask)
        self.finish(self.Result)


    @web.asynchronous
    def post(self,ident=0):
        data = json.loads(self.request.body)
        objTask = NginxList()
        objTask.ServerId = data['params'].get('ServerId', None)
        if objTask.ServerId:
            server_list = self.db.query(ServerList).filter(ServerList.ServerId==objTask.ServerId).first()
            objTask.NameServer= data['params'].get('NameServer', server_list.NameServer)
            objTask.DomainName = data['params'].get('DomainName', None)
            objTask.Document = data['params'].get('Document', None)
            objTask.Desc = data['params'].get('Desc', None)
            objTask.DomainIp = data['params'].get('DomainIp', None)
            objTask.ProxyIp = data['params'].get('ProxyIp', None)
            objTask.ProxyPort = data['params'].get('ProxyPort', None)
            objTask.CreateId = 1
            objTask.CreateTime = curDatetime()
            self.db.add(objTask)
            self.db.commit()
            self.Result['rows'] = 1
            self.Result['info'] = u'添加成功'
        else:
            self.Result['rows'] = 0
            self.Result['info'] = u'添加失败'
        self.finish(self.Result)


    @web.asynchronous
    def put(self, ident=0):
        data = json.loads(self.request.body)
        objTask = NginxList.query.get(ident)
        print ident
        if ident and objTask:
            objTask.NameServer= data['params'].get('NameServer', None)
            objTask.DomainName = data['params'].get('DomainName', None)
            objTask.Document = data['params'].get('Document', None)
            objTask.Desc = data['params'].get('Desc', None)
            objTask.DomainIp = data['params'].get('DomainIp', None)
            objTask.ProxyIp = data['params'].get('ProxyIp', None)
            objTask.ProxyPort = data['params'].get('ProxyPort', None)
            objTask.UpdateId = 2
            objTask.UpdateTime = curDatetime()
            self.db.add(objTask)
            self.db.commit()
            self.Result['rows'] = 1
            self.Result['info'] = u'修改成功'
        else:
            self.Result['rows'] = 0
            self.Result['info'] = u'修改失败'
        self.finish(self.Result)

    @web.asynchronous
    def delete(self, ident):
        self.db.query(NginxList).filter(NginxList.NginxId==ident).delete()
        self.db.commit()
        self.Result['info'] = u'删除成功'
        self.finish(self.Result)

@urlmap(r'/api/mysql\/?([0-9]*)')
class MysqlHandler(RESTfulHandler):
    @web.asynchronous
    def get(self, ident):
        if ident:
            try:
                objServer = MysqlList.query.get(ident)
                self.Result['rows'] = objServer.toDict()
                self.Result['total'] = 1
            except:
                self.Result['status'] = 404
                self.Result['info'] = 'No Row Found'
        else:
            page = int(self.get_argument('page', 1))
            searchKey = self.get_argument('searchKey', None)
            pagesize = int(self.get_argument('pagesize', self._PageSize))
            totalquery = self.db.query(MysqlList.MysqlId)
            ServerlistObj = self.db.query(MysqlList)
            if searchKey:
                totalquery = totalquery.filter(or_(MysqlList.NameServer.like('%%%s%%' % searchKey),MysqlList.AuthIp==searchKey,MysqlList.AuthName==searchKey))
                ServerlistObj = ServerlistObj.filter(or_(MysqlList.NameServer.like('%%%s%%' % searchKey),MysqlList.AuthIp==searchKey,MysqlList.AuthName==searchKey))

            self.Result['total'] = totalquery.count()
            serverTask = ServerlistObj.order_by(desc(MysqlList.CreateTime)).limit(pagesize).offset((page - 1) * pagesize).all()
            self.Result['rows'] = map(lambda obj: obj.toDict(), serverTask)
        self.finish(self.Result)

    @web.asynchronous
    def post(self,ident=0):
        data = json.loads(self.request.body)
        objTask = MysqlList()
        objTask.ServerId = data['params'].get('ServerId', None)
        if objTask.ServerId:
            server_list = self.db.query(ServerList).filter(ServerList.ServerId==objTask.ServerId).first()
            objTask.NameServer = data['params'].get('NameServer', server_list.NameServer)
            objTask.AuthCom = data['params'].get('AuthCom', None)
            com_list = str(objTask.AuthCom).split(' ')
            objTask.Permission = data['params'].get('Permission', com_list[1])
            objTask.DbName = data['params'].get('DbName', com_list[3].split('.')[0])
            objTask.AuthName = data['params'].get('AuthName', com_list[5].split('@')[0])
            objTask.AuthIp = data['params'].get('AuthIp', com_list[5].split('@')[1])
            objTask.AuthPasswd = data['params'].get('AuthPasswd', com_list[-1].strip('\'|\'\;'))
            objTask.CreateId = 1
            objTask.CreateTime = curDatetime()
            try:
                dbname = self.db.query(MysqlList).filter(MysqlList.DbName == objTask.DbName).first().DbName
                authname = self.db.query(MysqlList).filter(MysqlList.AuthName == objTask.AuthName).first().AuthName
                authip = self.db.query(MysqlList).filter(MysqlList.AuthIp == objTask.AuthIp).first().AuthIp
                authpasswd = self.db.query(MysqlList).filter(MysqlList.AuthPasswd == objTask.AuthPasswd).first().AuthPasswd
            except Exception,e:
                self.db.add(objTask)
                self.db.commit()
                self.Result['rows'] = 1
                self.Result['info'] = u'添加成功'
        else:
            self.Result['rows'] = 0
            self.Result['info'] = u'修改失败'
        self.finish(self.Result)

    @web.asynchronous
    def put(self, ident=0):
        data = json.loads(self.request.body)
        objTask = MysqlList.query.get(ident)
        if ident and objTask:
            objTask.NameServer= data['params'].get('NameServer', None)
            objTask.Permission = data['params'].get('Permission', None)
            objTask.DbName = data['params'].get('DbName', None)
            objTask.AuthName = data['params'].get('AuthName', None)
            objTask.AuthIp = data['params'].get('AuthIp', None)
            objTask.AuthPasswd = data['params'].get('AuthPasswd', None)
            objTask.UpdateId = 2
            objTask.UpdateTime = curDatetime()
            self.db.add(objTask)
            self.db.commit()
        self.Result['rows'] = 1
        self.Result['info'] = u'修改成功'
        self.finish(self.Result)

    @web.asynchronous
    def delete(self, ident):
        self.db.query(MysqlList).filter(MysqlList.MysqlId==ident).delete()
        self.db.commit()
        self.Result['info'] = u'删除成功'
        self.finish(self.Result)

@urlmap(r'/tpl/d3/')
class GraphHandler(RESTfulHandler):
    @web.asynchronous
    def get(self):
        self.render("graph.html")

@urlmap(r'/api/graph/')
class D3Handler(RESTfulHandler):
    @web.asynchronous
    def get(self):
        server_list = self.db.query(ServerList).all()
        d = {}
        d["data"] = {}
        for i in server_list:
            nameserver = i.NameServer
            allnginx = self.db.query(NginxList).filter(NginxList.NameServer==nameserver).first()
            allmysql = self.db.query(MysqlList).filter(MysqlList.NameServer==nameserver).first()
            ip0 = i.Ip0
            ip1 = i.Ip1
            d["data"].update({nameserver:{'name': "servername: {0}".format(nameserver), 'type': 'service', 'depends':[], 'dependedOnBy':[]}})
            #d["data"].update({ip0:{'name': "first_IP: {0}".format(ip0), 'type': 'service', 'depends':[nameserver], 'dependedOnBy':[]}})
            d["data"].update({ip1:{'name': "second_IP: {0}".format(ip1), 'type': 'service', 'depends':[nameserver], 'dependedOnBy':[]}})
            #if allnginx and allmysql:
            #    proxyip = "".join([allnginx.ProxyIp,"_",nameserver])
            #    authip = "".join([allmysql.AuthIp,"_",nameserver])
            #    p = self.db.query(NginxList).filter(NginxList.ProxyIp==ip0).first()
            #    p1 = self.db.query(MysqlList).filter(MysqlList.AuthIp==ip1).first()
            #    if not p1:
            #        p1 = self.db.query(MysqlList).filter(MysqlList.AuthIp=='127.0.0.1').first()
            #    if p and p1:
            #        n = self.db.query(ServerList).filter(ServerList.NameServer==p1.NameServer).first()
            #        if n:
            #            d["data"].update({proxyip:{'name': "代理IP: {0}".format(proxyip), 'type': 'nginx', 'depends':[nameserver,n.Ip0], 'dependedOnBy':[]}})
            #            d["data"].update({authip:{'name': "授权IP: {0}".format(authip), 'type': 'mysql', 'depends':[nameserver,n.Ip1], 'dependedOnBy':[]}})
            #elif allnginx:
            #    domainname = "".join([allnginx.DomainName,"_",nameserver])
            #    proxyip = "".join([allnginx.ProxyIp,"_",nameserver])
            #    try:
            #        p = self.db.query(NginxList).filter(NginxList.ProxyIp==ip0).first()
            #        n = self.db.query(ServerList).filter(ServerList.NameServer==p.NameServer).first()
            #    except Exception,e:
            #        pass
            #    else:
            #        d["data"].update({domainname:{'name': "解析域名: {0}".format(domainname), 'type': 'nginx', 'depends':[nameserver], 'dependedOnBy':[]}})
            #        d["data"].update({proxyip:{'name': "代理IP: {0}".format(proxyip), 'type': 'nginx', 'depends':[nameserver,n.Ip0], 'dependedOnBy':[]}})
            #elif allmysql:
            #    authip = "".join([allmysql.AuthIp,"_",nameserver])
            #    p = self.db.query(MysqlList).filter(MysqlList.AuthIp==ip1).first()
            #    if not p:
            #        p = self.db.query(MysqlList).filter(MysqlList.AuthIp=='127.0.0.1').first()
            #    n = self.db.query(ServerList).filter(ServerList.NameServer==p.NameServer).first()
            #    if n:
            #        d["data"].update({authip:{'name': "授权IP: {0}".format(authip), 'type': 'mysql', 'depends':[nameserver,n.Ip1], 'dependedOnBy':[]}})
        data = json.dumps(d)
        print d
        self.finish(data)
