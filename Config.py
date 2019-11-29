class BaseConfig(object):
    FLASK_PORT = 80
    FLASK_HOST = "0.0.0.0"


class DevConfig(BaseConfig):
    ENV = 'development'
    DEBUG = True


class ProdConfig(BaseConfig):
    # ENV = 'production'
    # DEBUG = True
    MYSQL_HOST = 'rm-bp17p167o6205qq10fo.mysql.rds.aliyuncs.com'
    MYSQL_USER_NAME = 'gitlab'
    MYSQL_PASSWORD = 'Qf@gitlab=123'
    MYSQL_DATABASE = 'gitlab'
