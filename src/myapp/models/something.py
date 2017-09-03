#!/usr/bin/env python3
'''
Module containing the Something model
'''

from myapp.util.db import BASE
from myapp.models.model import Model

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

class Something(BASE, Model):
    '''
    Something table model
    '''

    id = Column(Integer, primary_key=True)
    fld1 = Column(String(255))
    fld2 = Column(String(255))
    fld3 = Column(String(255))
    fld4 = Column(Integer)

    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    #somethingelse = relationship('Somethingelse', backref='something', lazy='dynamic')

