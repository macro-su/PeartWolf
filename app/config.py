import os


class Config(object):
    # 秘钥
    SECRET_KEY = os.environ.get('SECRET_KEY') or '123456'
    FLASK_PORT = 80
    FLASK_HOST = "0.0.0.0"
    # 额外的初始化操作
    @staticmethod
    def init_app(app):
        pass


class DevConfig(Config):
    ENV = 'development'
    DEBUG = True


class ProdConfig(Config):
    # ENV = 'production'
    # DEBUG = True
    MYSQL_HOST = 'rm-bp17p167o6205qq10fo.mysql.rds.aliyuncs.com'
    MYSQL_USER_NAME = 'gitlab'
    MYSQL_PASSWORD = 'Qf@gitlab=123'
    MYSQL_DATABASE = 'gitlab'


config = {
    'dev': DevConfig,
    'prod': ProdConfig,
    'default': DevConfig
}
