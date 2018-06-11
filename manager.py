import redis
from flask import Flask,session
from flask_session import Session  # 指定session存储位置
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate,MigrateCommand
from config import Config,ProductConfig
from flask_script import Manager


app = Flask(__name__)




# 加载配置信息到app
app.config.from_object(ProductConfig)

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

    # print(name)

    session['name'] = 'banzhang'

    return 'helloworld100'

if __name__ == '__main__':
    manger.run()