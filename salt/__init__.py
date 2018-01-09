from flask import Flask,Blueprint
from .views import login
from flask_session import Session
import redis


app = Flask(__name__,template_folder='templates',static_url_path='static')
app.debug = True

print('app.root_path===',app.root_path)
print('app.static_url_path===',app.static_url_path)

app.secret_key('uaremyhero')

app.config['SESSION_TYPE'] = 'redis'  # session类型为redis
app.config['SESSION_REDIS'] = redis.Redis(host='127.0.0.1', port='6379', password='123123')  # 用于连接redis的配置
app.config['SESSION_KEY_PREFIX'] = 'session:'  # 保存到session中的值的前缀
app.config['SESSION_PERMANENT'] = False  # 如果设置为True，则关闭浏览器session就失效。
app.config['SESSION_USE_SIGNER'] = False  # 是否对发送到浏览器上 session:cookie值进行加密
Session(app)



app.register_blueprint(login.login)
app.register_blueprint()