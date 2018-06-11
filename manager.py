import redis
from flask import Flask,session
from flask_session import Session  # 指定session存储位置
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager

app = Flask(__name__)

# 配置信息
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



# 加载配置信息到app
app.config.from_object(Config)

# 创建db对象
db = SQLAlchemy(app)

# 创建redis对象
redis_store = redis.StrictRedis(host=Config.REDIS_HOST,port=Config.REDIS_PORT,decode_responses=True)

# 指定session存储位置
Session(app)

# 将应用程序使用csrf保护
CSRFProtect(app)

# 配置数据库迁移
manger = Manager(app)
Migrate(app,db)
manger.add_command('db', MigrateCommand)

@app.route('/')
def hello_world():

    # redis_store.set('name','zhangsan')
    #
    # name = redis_store.get('name')
    #
    # print(name)

    session['name'] = 'banzhang'

    return 'helloworld100'

if __name__ == '__main__':
    manger.run()