# 配置信息
import redis


class Config(object):

    SECRET_KEY = 'hdhjdhfk'
    DEBUG = True

    # 数据库配置
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:mysql@127.0.0.1:3306/information30'
    SQLALCHEMY_TRACK_MODIFCATIONS = False

    # redis的配置
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

    # 配置session信息
    SESSION_TYPE = 'redis'
    SESSION_USE_SIGNER = True  # 设置session签名
    SESSION_REDIS = redis.StrictRedis(REDIS_HOST,REDIS_PORT)  # 指定session储存位置
    PERMANENT_SESSION_LIFETIME = 3600 * 24 * 2  #设置session的有效期为两天


#开发模式配置信息
class DeveloperConfig(Config):
    pass



# 生产模式配置信息
class TestingCinfig(Config):
    DEBUG = False
    pass



# 测试模式配置信息
class ProductConfig(Config):
    TESTING = True
    pass


# 提供一个统一的入口欧管理不同模式
config_dict = {
    'develop':DeveloperConfig,
    'product':TestingCinfig,
    'testing':ProductConfig
}