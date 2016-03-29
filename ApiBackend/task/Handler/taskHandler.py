#coding:utf-8
__author__ = 'yang'


from lib.urlmap import urlmap
from lib.basehandler import RESTfulHandler
from tornado import web,gen
from task.Entity.TasklistModel import TaskList
import json
from Common.functions import curDatetime,getTypesAttr
from sqlalchemy import desc,or_



@urlmap(r'/api/task\/?([0-9]*)')
class TaskHandler(RESTfulHandler):
    @web.asynchronous
    def get(self, ident=0):
        if ident:
            try:
                objTask = TaskList.query.get(ident)
                self.Result['rows'] = objTask.toDict()
                self.Result['total'] = 1
            except:
                self.Result['status'] = 404
                self.Result['info'] = 'No Row Found'
        else:
            page = int(self.get_argument('page', 1))
            searchKey = self.get_argument('searchKey', None)
            pagesize = int(self.get_argument('pagesize', self._PageSize))
            totalquery = self.db.query(TaskList.TaskId)
            tasklistObj = self.db.query(TaskList)
            if searchKey:
                totalquery = totalquery.filter(or_(TaskList.Name.like('%%%s%%' % searchKey),TaskList.FromIp==searchKey,TaskList.FromPos.like('%%%s%%' % searchKey),TaskList.ToIp==searchKey,TaskList.ToPos.like('%%%s%%' % searchKey),TaskList.EName.like('%%%s%%' % searchKey)))
                tasklistObj   = tasklistObj.filter(or_(TaskList.Name.like('%%%s%%' % searchKey),TaskList.FromIp==searchKey,TaskList.FromPos.like('%%%s%%' % searchKey),TaskList.ToIp==searchKey,TaskList.ToPos.like('%%%s%%' % searchKey),TaskList.EName.like('%%%s%%' % searchKey)))

            self.Result['total'] = totalquery.count()
            listTask = tasklistObj.order_by(desc(TaskList.CreateTime)).limit(pagesize).offset((page - 1) * pagesize).all()
            self.Result['rows'] = map(lambda obj: obj.toDict(), listTask)
        self.finish(self.Result)


    @web.asynchronous
    def post(self, ident=0):
        data = json.loads(self.request.body)
        objTask = TaskList()

        objTask.Name = data['params'].get('Name', None)
        objTask.EName= data['params'].get('EName', None)
        objTask.Desc = data['params'].get('Desc', None)
        objTask.Type = data['params'].get('Type', None)
        objTask.FromIp = data['params'].get('FromIp', None)
        objTask.FromPos = data['params'].get('FromPos', None)
        objTask.ToIp = data['params'].get('ToIp', None)
        objTask.ToPos = data['params'].get('ToPos', None)
        objTask.Status = data['params'].get('Status', None)
        objTask.ToPos = data['params'].get('ToPos', None)
        objTask.Comand = data['params'].get('Comand', None)
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
        objTask = TaskList.query.get(ident)
        if ident and objTask:
            objTask.EName= data['params'].get('EName', None)
            objTask.Desc = data['params'].get('Desc', None)
            objTask.FromIp = data['params'].get('FromIp', None)
            objTask.FromPos = data['params'].get('FromPos', None)
            objTask.ToIp = data['params'].get('ToIp', None)
            objTask.ToPos = data['params'].get('ToPos', None)
            objTask.UpdateId = 2
            objTask.UpdateTime = curDatetime()
            self.db.add(objTask)
            self.db.commit()
        self.Result['rows'] = 1
        self.Result['info'] = u'修改成功'
        self.finish(self.Result)

# 任务其它项修改
@urlmap(r'/api/taskchange/(.*)')
class TaskHandler(RESTfulHandler):
    @web.asynchronous
    def get(self, ct):
        if ct:
            ctList = ct.split('.')
            if ctList[0] and ctList[1]:
                if ctList[0] == 'status':
                    StatusList = [7,8]
                    objTask = TaskList.query.get(ctList[1])
                    StatusList.remove(objTask.Status)
                    objTask.Status = StatusList[0]
                    self.db.add(objTask)
                    self.db.commit()
                self.Result['info'] = '状态修改成功'
                if ctList[0] == 'type':
                    from task.Entity.TypesModel import Types
                    StatusList = [0,1]
                    objTypes = Types.query.get(ctList[1])
                    StatusList.remove(objTypes.Status)
                    objTypes.Status = StatusList[0]
                    self.db.add(objTypes)
                    self.db.commit()
                self.Result['info'] = '状态修改成功'
            else:
                self.Result['status'] = 404
                self.Result['info'] = 'No change Found'
        else:
            self.Result['status'] = 404
            self.Result['info'] = 'No key Found'
        self.finish(self.Result)

# 任务日志统计报表
@urlmap(r'/api/taskstatics/(.*)')
class TaskstaticsHandler(RESTfulHandler):

    # @web.asynchronous
    def get(self, TaskId):
        from task.Entity.TasklogModel import TaskLog
        logList = self.db.query(TaskLog).filter(TaskLog.TaskId==TaskId).filter(TaskLog.Status==9).all()
        s = []
        import time
        for r in logList:
            if r.StartTime:
                t = time.mktime(time.strptime(r.StartTime.strftime('%Y-%m-%d %H:%M:%S'),'%Y-%m-%d %H:%M:%S'))
                tmp = '{x:%s,y:%s}' % (int(t)*1000, r.FileSize.replace('MB', '').replace('M', ''))
                s.append(tmp)
        self.Result['rows'] = ','.join(s)
        self.finish(self.Result)
