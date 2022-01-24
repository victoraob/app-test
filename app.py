from flask import Flask
from flask import render_template,request,redirect,url_for,flash

import numpy as np

app = Flask(__name__)
app.secret_key = "csrftoken"

from controllers.HomeController import *

if __name__ == '__main__':
    app.run(debug=True)