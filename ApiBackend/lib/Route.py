# -*- coding: utf-8 -*-
__author__ = 'Hipeace86'
__datetime__ = '15-4-13'

import random, os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session, Session
from sqlalchemy import desc
from lib.Extension import DataUpdateExtension
from yaml import load

BaseModel = declarative_base()


class Basebase(object):
    __mapper_args__ = {
        'extension': DataUpdateExtension()
    }
    __table_args__ = {
        'mysql_engine': 'innodb',
        'mysql_charset': 'utf8'
    }

    @classmethod
    def get_by_id(cls, ident):
        entity = session.query(cls).get(ident)
        session.close_all()
        return entity

    @classmethod
    def get_page_list(cls, page, pagesize):
        if hasattr(cls, 'CreateTime'):
            entitys = session.query(cls).order_by(desc(cls.CreateTime)).offset((page - 1) * pagesize).limit(
                pagesize).all()
        else:
            entitys = session.query(cls).offset((page - 1) * pagesize).limit(pagesize).all()

        session.close_all()
        return entitys

    @classmethod
    def get_count(cls):
        count = session.query(cls).count()
        session.close_all()
        return count

    @classmethod
    def get_by_list_id(cls, list):
        print cls.__mapper__.primary_key


# return session.query(cls).filter(cls.pk.in_(list)).all()


yaml = load(file(os.path.join(os.path.abspath(os.path.join(__file__, '../../lib/')), 'config.yaml'), 'r'))

engine = create_engine(yaml['mysql'], convert_unicode=True, pool_recycle=120, echo=False)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
BaseModel.query = db_session.query_property()
