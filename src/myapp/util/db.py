#!/usr/bin/env python3
'''
Global database and SQLAlchemy functions/objects
Import module
Run "dbinit()"
access module variables: db.SESSION db.ENGINE etc
'''

import myapp.config as config

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import configure_mappers

#conf = config.Config('~/.config/myapp/config.cfg')
BASE = None
SESSION_FACTORY = None
ENGINE = None

def dbinit():
    '''
    Initialise the database connections from the config
    '''
    global ENGINE, SESSION, SESSION_FACTORY, BASE

    #config.Config.CONF

    db_uri = config.Config.CONF.get('database', 'URI')
    db_opts = dict()
    for option in config.Config.CONF.options('database'):
        if option.startswith('option.'):
            oopt = option.split('.', 1)[1]
            db_opts[oopt] = config.Config.CONF.get('database', option)

    session_autocommit = config.Config.CONF.getboolean('session', 'autocommit')

    ENGINE = create_engine(db_uri, **db_opts)
    SESSION_FACTORY = sessionmaker(bind=ENGINE, autocommit=session_autocommit)

    BASE = declarative_base()
    configure_mappers()

def session():
    '''
    Get a new session
    '''
    return scoped_session(SESSION_FACTORY)
