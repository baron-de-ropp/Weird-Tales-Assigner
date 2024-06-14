from flask import render_template, request, redirect, url_for
from app import app
import random
from app.email_utils import send_email
from app.logic import get_random_images, check_existing_assignment, log_assignment
import os

@app.route('/')
def index():
    images = get_random_images(app.root_path)
    return render_template('index.html', images=images)

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        email = request.form['email']
        itch_username = request.form['itch_username']
        existing_assignment = check_existing_assignment(email)
        if existing_assignment:
            images = existing_assignment['images']
            message = "These were your assigned images!"
        else:
            images = get_random_images(app.root_path)
            log_assignment(email, itch_username, images)
            send_email(email, images)
            message = "Your inspiration challenge prompts are..."

        return render_template('assignment.html', images=images, email=email, itch_username=itch_username, message=message)
    return render_template('submit.html')
