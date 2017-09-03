#!/usr/bin/env python3
'''
Base module for sqlalchemy table models
'''

from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import Column, Integer
import inflect

class Model(object):
    '''
    Base class for all sqlalchemy models in the project
    '''
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        """ Display object string representation in format:
                <Model(table=models), name=model.name)>'
        """

        return "<%s(table='%s', id='%s')>" % (
            self.__class__.__name__,
            self.__tablename__,
            self.id
        )

    @declared_attr
    def __tablename__(cls):
        """ Dynamically inflect tablename from class name """
        return inflect.engine().plural(cls.__name__.lower())
