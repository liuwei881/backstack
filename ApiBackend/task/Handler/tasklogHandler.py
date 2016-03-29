#coding:utf-8
__author__ = 'yang'


from lib.urlmap import urlmap
from lib.basehandler import RESTfulHandler
from tornado import web
from task.Entity.TasklogModel import TaskLog
import json
from Common.functions import curDatetime
from sqlalchemy import desc



@urlmap(r'/api/tasklog')
class TasklogHandler(RESTfulHandler):
    @web.asynchronous
    def get(self):
        page = int(self.get_argument('page', 1))
        searchKey = self.get_argument('searchKey', None)
        pagesize = int(self.get_argument('pagesize', self._PageSize))
        totalquery = self.db.query(TaskLog.LogId)
        tasklogObj = self.db.query(TaskLog)
        if searchKey:
            totalquery = totalquery.filter(TaskLog.Name.like('%%%s%%' % searchKey))
            tasklogObj = tasklogObj.filter(TaskLog.Name.like('%%%s%%' % searchKey))
        self.Result['total'] = totalquery.count()
        logTask = tasklogObj.order_by(desc(TaskLog.LogId)).limit(pagesize).offset((page - 1) * pagesize).all()
        self.Result['rows'] = map(lambda obj: obj.toDict(), logTask)
        self.finish(self.Result)


    """
    日志数据接口  接受各个机器传送过来的日志信息
    post方式
        :param
        *   :Type       11:rsync_pull  12:rsync_push  13:mysqldump
        *   :Name       任务英文名称  与任务列表的英文名相同即可
            :Command    执行命令
            :StartTime  自动为当前时间
            :EndTime    执行结束时间(时间戳)
            :ExpireTime 文件过期时间
        *   :Status     执行结果    9:成功   10:失败
            :FileSize   文件大小
        :return
            {'Status':200/404,'Info':'receiveInfo'}

        :demo/example
            curl -d '{"Type":11,"Name":"testApi","Status":9}'  'http://l.bk/api/tasklog'
            "EndTime":'`date "+%s"`'  : 当前时间示例(时间戳)
    """
    @web.asynchronous
    def post(self):
        logObj = TaskLog()
        data = json.loads(self.request.body)
        logObj.TaskId = str(data.get('TaskId',11))
        logObj.Type = str(data.get('Type',11))
        logObj.Name = data.get('Name',None)
        logObj.Command = data.get('Command','')
        startTime = data.get('StartTime',None)
        endTime = data.get('EndTime',None)
        import time
        if startTime:
            logObj.StartTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(startTime))
            print logObj.StartTime
        if endTime:
            logObj.EndTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(endTime))
        logObj.ExpireTime = data.get('ExpireTime',None)
        logObj.Status = data.get('Status',None)
        logObj.CreateId = 0     #系统执行
        logObj.FileSize = data.get('FileSize',None)
        logObj.FromIp = self.request.remote_ip
        self.db.add(logObj)
        self.db.commit()
        self.Result['rows'] = 1
        self.Result['Info'] = 'ok'
        self.finish(self.Result)

    """
        更新日志接口
        根据logId 更新日志的结束时间 状态 文件大小 过期时间
    """
    @web.asynchronous
    def put(self):
        data = json.loads(self.request.body)
        LogId = str(data.get('LogId',11))
        if LogId:
            objLog = TaskLog.query.get(LogId)
            endTime = data.get('EndTime',None)
            import time
            if endTime:
                objLog.EndTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(endTime))
            if data.get('ExpireTime',None):
                objLog.ExpireTime = data.get('ExpireTime',None)
            if data.get('Status',None):
                objLog.Status = data.get('Status',None)
            if data.get('FileSize',None):
                objLog.FileSize = data.get('FileSize',None)
            objLog.FromIp = self.request.remote_ip
            self.db.add(objLog)
            self.db.commit()
            self.Result['rows'] = 1
            self.Result['Info'] = 'ok'
        else:
            self.Result['rows'] = 0
            self.Result['Info'] = 'no Log Id'
        self.finish(self.Result)