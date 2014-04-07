class Config(object):
    # Database config
    HOST = 'localhost'
    DATABASE='pyrcp'
    USERNAME='pyrcp'
    PASSWORD='pyrcp'
    CHARSET='utf8'
    #
    # App config
    DEBUG=True
    SECRET_KEY='development key'

    # Server info
    SERVERNAME='MyRO'
    USE_MD5_PASS=True

class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True


