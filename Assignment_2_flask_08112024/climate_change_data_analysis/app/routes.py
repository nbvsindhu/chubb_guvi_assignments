# app/routes.py

from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user, current_user
from app import app, db
from app.models import User

# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:  # You should hash passwords in production
            login_user(user)
            return redirect(url_for('index'))  # Redirect to dashboard (index route)
        else:
            flash('Invalid username or password. Please try again.', 'danger')
            return redirect(url_for('login'))
    return render_template("login.html")

# Route for the dashboard (home page)
@app.route('/')
@login_required  # This ensures that the user is logged in before accessing the dashboard
def index():
    # Your logic to render the climate data dashboard goes here
    return render_template('index.html')
