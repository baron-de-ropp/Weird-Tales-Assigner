import json
import os
import csv
import random

def get_random_images(app_root):
    with open(os.path.join(app_root, 'image_data.json')) as f:
        image_list = json.load(f)
    return random.sample(image_list, 3)

def check_existing_assignment(email):
    if not os.path.exists('assignments.csv'):
        return None
    with open('assignments.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['email'] == email:
                return {
                    'email': row['email'],
                    'itch_username': row['itch_username'],
                    'images': json.loads(row['images'])
                }
    return None

def log_assignment(email, itch_username, images):
    with open('assignments.csv', 'a', newline='') as csvfile:
        fieldnames = ['email', 'itch_username', 'images']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if csvfile.tell() == 0:
            writer.writeheader()
        writer.writerow({'email': email, 'itch_username': itch_username, 'images': json.dumps(images)})
