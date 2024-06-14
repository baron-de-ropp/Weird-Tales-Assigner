from flask import render_template
from app import app
import random
import json
import os

@app.route('/')
def index():
    images = get_random_images()
    return render_template('index.html', images=images)

def get_random_images():
    # Load the image data from image_data.json
    with open(os.path.join(app.root_path, 'image_data.json')) as f:
        image_list = json.load(f)
    return random.sample(image_list, 3)
