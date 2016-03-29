# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, Text, DateTime
from lib.Route import BaseModel


class Types(BaseModel):
    __tablename__ = 'bk_types'

    TypeId = Column('fi_id', Integer, primary_key=True)
    Name = Column('fs_name', Integer)
    Desc = Column('fs_desc', String(20))
    Status = Column('fi_status', Text)
    EName = Column('fs_ename', String(20))
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
            'TypeId': self.TypeId,
            'Name': self.Name,
            'Desc': self.Desc,
            'EName': self.EName,
            'Status': '启用' if self.Status else '禁用',
            'CreateId': self.CreateId,
            'CreateTime': self.CreateTime.strftime('%Y-%m-%d %H:%M:%S') if self.CreateTime else '',
            'UpdateId': self.UpdateId,
            'UpdateTime': self.UpdateTime.strftime('%Y-%m-%d %H:%M:%S') if self.UpdateTime else ''
        }

class Typesattr(BaseModel):
    __tablename__ = 'bk_types_attr'

    AttrId = Column('fi_attr_id', Integer, primary_key=True)
    TypeId = Column('fi_type_id', Integer)
    Name = Column('fs_name', Integer)
    Value = Column('fs_value', String(20))
    Status = Column('fi_status', Text)

    def toDict(self):
        return {
            'AttrId': self.AttrId,
            'Name': self.Name,
            'TypeId': self.TypeId,
            'Status': '启用' if self.Status else '禁用',
            'Value': self.Value,
        }

