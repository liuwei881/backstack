# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, Text, DateTime
from lib.Route import BaseModel
from Common.functions import getStatusIdDesc

class ServerList(BaseModel):
    """
    服务器信息列表
    """
    __tablename__ = 'bk_server_list'

    ServerId = Column('fi_id', Integer, primary_key=True)
    NameServer = Column('fs_nameserver', String(50))
    Location = Column('fs_location',String(50))
    OsVersion = Column('fs_osversion',String(50))
    Memory = Column('fs_memory',String(20))
    Disk = Column('fs_disk',String(20))
    Cpu = Column('fs_cpu',String(20))
    Sorts = Column('fs_sorts',String(20))
    BandWidth = Column('fs_bandwidth',String(20))
    Ip0 = Column('fs_ip0', String(50))
    Ip1 = Column('fs_ip1', String(50))
    Ip2 = Column('fs_ip2', String(50))

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
            'ServerId': self.ServerId,
            'NameServer': self.NameServer,
            'Location':self.Location,
            'OsVersion':self.OsVersion,
            'Memory':self.Memory,
            'Disk':self.Disk,
            'Cpu':self.Cpu,
            'Sorts':self.Sorts,
            'BandWidth':self.BandWidth,
            'Ip0': self.Ip0,
            'Ip1': self.Ip1,
            'Ip2': self.Ip2,
            'CreateId': self.CreateId,
            'CreateTime': self.CreateTime.strftime('%Y-%m-%d %H:%M:%S') if self.CreateTime else '',
            'UpdateId': self.UpdateId,
            'UpdateTime': self.UpdateTime.strftime('%Y-%m-%d %H:%M:%S') if self.UpdateTime else ''
        }

class NginxList(BaseModel):
    """
    nginx域名解析列表
    """
    __tablename__ = 'bk_nginx_list'

    NginxId = Column('fi_id', Integer, primary_key=True)
    ServerId = Column('fi_sl_id',Integer)
    NameServer = Column('fs_nameserver', String(50))
    DomainName = Column('fs_domainname', String(50))
    Document = Column('fs_document', String(255))
    Desc = Column('fs_desc',String(255))
    DomainIp = Column('fs_domainip', String(50))
    ProxyIp = Column('fs_proxyip', String(50))
    ProxyPort = Column('fi_proxyport', Integer)

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
            'NginxId': self.NginxId,
            'ServerId': self.ServerId,
            'NameServer':self.NameServer,
            'DomainName': self.DomainName,
            'Document': self.Document,
            'Desc':self.Desc,
            'DomainIp': self.DomainIp,
            'ProxyIp': self.ProxyIp,
            'ProxyPort': self.ProxyPort,
            'CreateId': self.CreateId,
            'CreateTime': self.CreateTime.strftime('%Y-%m-%d %H:%M:%S') if self.CreateTime else '',
            'UpdateId': self.UpdateId,
            'UpdateTime': self.UpdateTime.strftime('%Y-%m-%d %H:%M:%S') if self.UpdateTime else ''
        }

class MysqlList(BaseModel):
    """
    mysql信息列表
    """
    __tablename__ = 'bk_mysql_list'

    MysqlId = Column('fi_id', Integer, primary_key=True)
    ServerId = Column('fi_sl_id',Integer)
    NameServer = Column('fs_nameserver', String(50))
    Permission = Column('fs_permission', String(50))
    DbName = Column('fs_dbname', String(50))
    AuthName = Column('fs_authname', String(50))
    AuthIp = Column('fs_authip', String(50))
    AuthPasswd = Column('fs_authpasswd', String(50))
    AuthCom = Column('fs_authcom', String(255))

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
            'MysqlId': self.MysqlId,
            'ServerId': self.ServerId,
            'NameServer':self.NameServer,
            'Permission':self.Permission,
            'DbName':self.DbName,
            'AuthName':self.AuthName,
            'AuthIp':self.AuthIp,
            'AuthPasswd':self.AuthPasswd,
            'AuthCom':self.AuthCom,
            'CreateId': self.CreateId,
            'CreateTime': self.CreateTime.strftime('%Y-%m-%d %H:%M:%S') if self.CreateTime else '',
            'UpdateId': self.UpdateId,
            'UpdateTime': self.UpdateTime.strftime('%Y-%m-%d %H:%M:%S') if self.UpdateTime else ''
        }