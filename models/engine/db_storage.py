#!/usr/bin/python3
"""This module defines a database storage class"""
import os
from sqlalchemy import MetaData
from sqlalchemy.orm import create_engine, Session

metadata = MetaData()


class DBStorage:
    """This class models a database mapped class"""
    __engine = None
    __session = None

    def __init__(self):

        dialect = 'mysql'
        dbapi = 'mysqldb'
        host = os.environ.get('HBNB_TYPE_STORAGE')
        username = os.environ.get('HBNB_TYPE_STORAGE')
        password = os.environ.get('HBNB_TYPE_STORAGE')
        db_name = os.environ.get('HBNB_TYPE_STORAGE')
        env = os.environ.get('HBNB_ENV')

        connection_string = (
            f"{dialect}+{dbapi}://"
            f"{username}:{password}@"
            f"{host}/"
            f"{db_name}"
        )

        self.__engine = create_engine(connection_string,
                       pool_pre_ping=True, echo=False)

        if env == 'test':
            metadata.drop_all(self.__engine)

    def all(self, cls=None):
        self.__session = Session(bind=self.__engine)
        dictionary = {}

    