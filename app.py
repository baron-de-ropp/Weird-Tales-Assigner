from flask import Flask, render_template, request, redirect, url_for
import random
from logic import get_random_images, check_existing_assignment, log_assignment
import os

app = Flask(__name__)

@app.route('/')
def index():
    images = get_random_images(app.root_path)
    return render_template('index.html', images=images)

# @app.route('/submit', methods=['GET', 'POST'])
# def submit():
#     if request.method == 'POST':
#         itch_username = request.form['itch_username']
#         existing_assignment = check_existing_assignment(itch_username)
#         if existing_assignment:
#             images = existing_assignment['images']
#             message = "These were your assigned images!"
#         else:
#             images = get_random_images(app.root_path)
#             log_assignment(itch_username, images)
#             message = "Your inspiration challenge prompts are..."

#         return render_template('assignment.html', images=images, itch_username=itch_username, message=message)
#     return render_template('submit.html')

if __name__ == "__main__":
    app.run(debug=True)

