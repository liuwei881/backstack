# -*- coding: utf-8 -*-
"""
Users 
@version:1.0.20150908
@author: Hipeace86
"""
from sqlalchemy import Column, Integer, String, Float, DateTime
from lib.Route import BaseModel


class Users(BaseModel):
    """
    用户
    """
    __tablename__ = 'tzc_users'
    """
    数据库表名
    """

    UserId = Column('fi_user_id', Integer, primary_key=True)
    """:param UserId: 用户ID"""
    NickName = Column('fs_nick_name', String(50))
    """:param NickName: 用户昵称"""
    Account = Column('fs_account', String(50))
    """:param Account: 用户帐号"""
    Password = Column('fs_password', String(32))
    """:param Password: 密码"""
    Email = Column('fs_email', String(50))
    """:param Email: 邮箱"""
    IsAdmin = Column('fi_is_admin', Integer)
    """:param IsAdmin: 是否管理员"""
    IsDelete = Column('fi_is_delete', Integer)
    """:param IsDelete: 是否删除"""
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
            'UserId': self.UserId,
            'NickName': self.NickName,
            'Account': self.Account,
            'Password': self.Password,
            'Email': self.Email,
            'IsAdmin': self.IsAdmin,
            'IsDelete': self.IsDelete,
            'CreateId': self.CreateId,
            'CreateTime': self.CreateTime.strftime('%Y-%m-%d %H:%M:%S') if self.CreateTime else '',
            'UpdateId': self.UpdateId,
            'UpdateTime': self.UpdateTime.strftime('%Y-%m-%d %H:%M:%S') if self.UpdateTime else ''
        }
