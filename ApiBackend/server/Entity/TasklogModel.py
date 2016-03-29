# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, Text, DateTime
from lib.Route import BaseModel
from Common.functions import getStatusIdDesc

class TaskLog(BaseModel):
    """
    任务列表
    """
    __tablename__ = 'bk_task_log'

    LogId = Column('fi_id', Integer, primary_key=True)
    TaskId = Column('fi_task_id', Integer)
    Type = Column('fi_type', Integer)
    Name = Column('fs_name', String(50))
    FileSize = Column('fs_file_size', String(20))
    Comand = Column('fs_comand', Text)
    Status = Column('fi_status', Integer)
    CreateId = Column('fi_create_id', Integer)
    ExpireTime = Column('ft_expire_time', DateTime)
    StartTime = Column('ft_start_time', DateTime)
    EndTime = Column('ft_end_time', DateTime)
    FromIp = Column('fs_from_ip', String(15))


    def toDict(self):
        return {
            'LogId': self.LogId,
            'TaskId': self.TaskId,
            'Type': getStatusIdDesc(self.Type),
            'Name': self.Name,
            'FileSize': self.FileSize,
            'Comand': self.Comand,
            'Status': getStatusIdDesc(self.Status),
            'CreateId': self.CreateId,
            'FromIp': self.FromIp,
            'ExpireTime': self.ExpireTime,
            'StartTime': self.StartTime.strftime('%Y-%m-%d %H:%M:%S') if self.StartTime else '',
            'EndTime': self.EndTime.strftime('%Y-%m-%d %H:%M:%S') if self.EndTime else ''
        }
