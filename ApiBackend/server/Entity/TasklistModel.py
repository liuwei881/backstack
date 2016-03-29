# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, Text, DateTime
from lib.Route import BaseModel
from Common.functions import getStatusIdDesc

class TaskList(BaseModel):
    """
    任务列表
    """
    __tablename__ = 'bk_task_list'

    TaskId = Column('fi_id', Integer, primary_key=True)
    Name = Column('fs_name', String(50))
    EName = Column('fs_ename', String(20))
    Desc = Column('fs_desc', String(255))
    Type = Column('fi_type', Integer)
    FromIp = Column('fs_from_ip', String(20))
    FromPos = Column('fs_from_pos', String(255))
    ToIp = Column('fs_to_ip', String(20))
    ToPos = Column('fs_to_pos', String(255))
    Status = Column('fi_status', Integer)
    Comand = Column('fs_comand', Text)

    CreateId = Column('fi_create_id', Integer)
    """:param CreateId: 创建人"""
    CreateTime = Column('ft_create_time', DateTime)
    """:param CreateTime: 创建时间"""
    UpdateId = Column('fi_update_id', Integer)
    """:param UpdateId: 修改人"""
    UpdateTime = Column('ft_update_time', DateTime)
    """:param UpdateTime: 修改时间"""

    def toDict(self):
        return {
            'TaskId': self.TaskId,
            'Name': self.Name,
            'EName': self.EName,
            'Desc': self.Desc,
            'Type': getStatusIdDesc(self.Type),
            'TypeNum': self.Type,
            'FromIp': self.FromIp,
            'FromPos': self.FromPos,
            'ToIp': self.ToIp,
            'ToPos': self.ToPos,
            'Status': getStatusIdDesc(self.Status),
            'Comand': self.Comand,
            'CreateId': self.CreateId,
            'CreateTime': self.CreateTime.strftime('%Y-%m-%d %H:%M:%S') if self.CreateTime else '',
            'UpdateId': self.UpdateId,
            'UpdateTime': self.UpdateTime.strftime('%Y-%m-%d %H:%M:%S') if self.UpdateTime else ''
        }
