#from flask import render_template, url_for, flash, redirect
from app import app
from flask import render_template
#from flaskblog.forms import RegistrationForm, LoginForm
#from flaskblog.models import User, Post





@app.route("/admin/dashboard")
def admin_dashboard():
    return render_template('admin/dashboard.html')


@app.route("/admin/profile")
def admin_profile():
    return 'admin profile'

