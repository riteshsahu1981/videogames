from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '' #'root'
app.config['MYSQL_DB'] = 'videogame'
mysql = MySQL(app)
#api = Api(app)
from restapi import routes
