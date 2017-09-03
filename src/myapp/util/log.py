'''
Python logging configuration
'''

import logging
import logging.handlers
import logging.config

def setuplogging(config_location):
    '''
    set up application logging
    '''
    import os
    import os.path
    try:
        fgetl_env = os.environ['FGETL_CFG']
    except:
        fgetl_env = None
    locations = [config_location,
                 fgetl_env,
                 './fgetl/etc/logging.cfg',
                 '/admin/etc/fgetl/logging.cfg',
                 '/etc/fgetl/logging.cfg',
                 '~/.config/fgetl/logging.cfg']
    setup = False
    for dd in locations:
        fle = '%s/logging.cfg' % dd
        if dd is not None and os.path.isfile(fle):
            logging.config.fileConfig(fle)
            setup = True
            break

    if not setup:
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler = logging.StreamHandler()
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(formatter)

        root = logging.getLogger()
        root.setLevel(logging.DEBUG)
        root.addHandler(handler)
        logging.info("Using default logging settings")
