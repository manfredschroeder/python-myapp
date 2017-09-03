#!/usr/bin/env python3
'''
A starting point for a program
'''

import sys
import logging
import time
import argparse

from sqlalchemy.orm.exc import NoResultFound
from myapp.util import session, dbinit, setuplogging
from myapp.config import loadconf, Config

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--conf_location", help="Location for configuration files")
    args = parser.parse_args()
    conf_location = './myapp/etc/'
    if args.conf_location:
        conf_location = args.conf_location

    loadconf(conf_location)
    setuplogging(conf_location)
    dbinit()

    import myapp.models as model
    logger = logging.getLogger('program')

    logger.info('Starting program.py')

    some_config = Config.CONF.get('something', 'some_config')

    while True:
        logger.debug('Get session')
        ses = session()

        try:
            logger.debug('Load something from the database')
            uploads = ses.query(model.Something).all()
        except NoResultFound:
            logger.error('Could not query somethings')
            sys.exit(1)

        logger.debug('Close session and sleep')
        ses.commit()
        ses.close()

        time.sleep(10)

