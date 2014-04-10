'''
    Initial config. Your config should extend this one.
'''
class Config(object):
    # Database config
    HOST = 'localhost'
    DATABASE='database_name'
    USERNAME='username'
    PASSWORD='userpass'
    CHARSET='utf8'

    # App config
    DEBUG=True
    SECRET_KEY='development key'

    # Server info
    SERVERNAME='PyRCP'
    USE_MD5_PASS=True

'''
    Custom config. Extends Config class.
'''
class MyRoConfig(Config):
    HOST = 'localhost'
    DATABASE='pyrcp'
    USERNAME='pyrcp'
    PASSWORD='pyrcp'
    SERVERNAME='MyRO'
    DEBUG = True
