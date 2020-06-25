from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('congif_file.ini')

from app import routes
from app import dbservices
