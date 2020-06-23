from flask import Flask,config,redirect,render_template
from dbservices import dbservice

from app import app

'''set = setconf
set.conf()
class create_app():
    application = Flask(__name__)
    with application.app_context():
        set.conf()



apps = create_app()
app = apps.application
'''
db = dbservice()
app.config['USERNAME'] = '1cbc267c-dff3-417f-97d7-44bb40ad570d-bluemix'
app.config['PASSWORD'] = 'a3eb3e22cddda14a068eef718f2921048e550f059a6c6e3230e42c51c08a5249'
app.config['URL'] = 'https://1cbc267c-dff3-417f-97d7-44bb40ad570d-bluemix:a3eb3e22cddda14a068eef718f2921048e550f059a6c6e3230e42c51c08a5249@1cbc267c-dff3-417f-97d7-44bb40ad570d-bluemix.cloudantnosqldb.appdomain.cloud'


@app.route('/')
def index():
    db.connection()
    return("Hello")
