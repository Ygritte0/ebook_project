from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_pagedown import PageDown
from config import config

bootstrap = Bootstrap()
# mail = Mail()
# moment = Moment()
db = SQLAlchemy()
pagedown = PageDown()




def create_app(config_name):
    app = Flask(__name__)

    # 这一行是应用配置的，from_object是让app从传入的对象中读取配置。
    # 如果你自定义了配置类，就把你的类传进来，也就是你的 config['default']。
    # app是Flask的实例，它有一个default_config属性，代表了默认的配置
    app.config.from_object(config['default'])

    # 这个地方发起了一个KeyError异常，KeyError一般在直接获取dict值时报错
    # 举例，a是一个字典，当直接过去里面b的值的时候就会报错：
    # a = {'a': 1}
    # print(a['b'])
    # 所以你这里是因为 config 变量不存在值为 config_name的键
    # 如何调试呢？首先打印config，看config里都有什么。然后打印config_name，看在不在config里
    print('config is: ', config)
    print('config_name is： ', config_name)
    # config 是个字典类型，如果config中存在config_name这个键，那么config_name in config会是True
    print('config_name in config ', config_name in config)

    # 这一行不是应用配置，而是执行配置内的init_app函数，进行其他一些处理。
    # 你 config 中自定义的init_app函数，代码块是pass，什么都没做。所以这一行可以注释掉
    config[config_name].init_app(app)
    print(app.config)

    bootstrap.init_app(app)
    # mail.init_app(app)
    # moment.init_app(app)
    db.init_app(app)
    # pagedown.init_app(app)
    #
    # if app.config['SSL_REDIRECT']:
    #     from flask_sslify import SSLify
    #     sslify = SSLify(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # from .auth import auth as auth_blueprint
    # app.register_blueprint(auth_blueprint, url_prefix='/auth')
    #
    # from .api import api as api_blueprint
    # app.register_blueprint(api_blueprint, url_prefix='/api/v1')

    return app