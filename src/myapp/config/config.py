#!/usr/bin/env python3
'''
Config file parser helper module.
'''

import configparser
import logging

def loadconf(conf_location=None):
    '''
    Initialization of configuration
    '''
    Config(conf_location)

class Config(object):
    '''
    ConfigParser wrapper class
    TODO make this more than a container for the config object.
    '''

    CONF = None

    def __init__(self, conf_location=None):
        import os
        import os.path
        try:
            fgetl_env = os.environ['FGETL_CFG']
        except:
            fgetl_env = None
        locations = [fgetl_env,
                     './fgetl/etc',
                     '/admin/etc/fgetl',
                     '/etc/fgetl',
                     '~/.config/fgetl']

        self.default_cfg = None
        self.settings_cfg = None
        for dd in locations:
            fle = "%s/%s" % (dd, 'default.cfg')
            if dd is not None and os.path.isfile(fle):
                self.default_cfg = fle
                break

        if conf_location is not None and not os.path.isdir(conf_location):
            import errno
            raise OSError(errno.ENOENT,
                          os.strerror(errno.ENOENT), conf_location)

        for dd in locations:
            fle = "%s/%s" % (dd, 'settings.cfg')
            if dd is not None and os.path.isfile(fle):
                self.settings_cfg = fle
                break

        self.config_location = conf_location

        if self.default_cfg is None and self.config_location is None:
            import errno
            raise OSError(errno.ENOENT,
                          os.strerror(errno.ENOENT), conf_location)

        Config.CONF = configparser.SafeConfigParser()

        if self.default_cfg:
            logging.info("Using default file %s" % self.default_cfg)
            Config.CONF.read(self.default_cfg)

        if self.settings_cfg:
            logging.info("Using settings file %s" % self.settings_cfg)
            Config.CONF.read(self.settings_cfg)
