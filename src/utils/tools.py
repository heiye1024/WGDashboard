

from calendar import c
import os
import configparser


configuration_path = os.getenv('CONFIGURATION_PATH', '../')
DASHBOARD_CONF = os.path.join(configuration_path, 'wg-dashboard.ini')




def get_dashboard_conf():
    """
    Get dashboard configuration
    @return: configparser.ConfigParser
    """
    r_config = configparser.ConfigParser(strict=False)
    r_config.read(DASHBOARD_CONF)
    return r_config



class Config(object):
    """
    Flask configuration
    
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    """

    def __init__(self) -> None:
        super().__init__()    