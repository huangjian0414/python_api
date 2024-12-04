

from flask import Flask, render_template
from flask.ext.mysql import MySQL

app = Flask(__name__)

# 配置 MySQL 数据库
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'flask_db'

# 初始化 MySQL 扩展
mysql = MySQL(app)


