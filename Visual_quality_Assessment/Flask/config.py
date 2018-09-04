#配置文件
class Config(object):
    pass
class ProdConfig(Config):
    pass
class DevConfig(Config):
    DATABASE = 'laeval.db'
    SQLALCHEMY_DATABAsE_URI='sqlite:///{}'.format(DATABASE)

    DEBUG=True#在生产环境下，此值为False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

'''
SQLite数据URI为：sqlite:///database.db
MySQL数据库URI为: mysql+pymysql://user:password@ip:port/db_name
'''