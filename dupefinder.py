import json
from collections import defaultdict

# Load the image data from image_data.json
with open('app/image_data.json') as f:
    image_data = json.load(f)

# Identify duplicates by title
duplicates = defaultdict(list)
for entry in image_data:
    duplicates[entry['title']].append(entry['url'])

# Write duplicates to duplicate.txt
with open('duplicate.txt', 'w') as f:
    for title, urls in duplicates.items():
        if len(urls) > 1:
            f.write(f"Title: {title}\n")
            for url in urls:
                f.write(f"    {url}\n")
            f.write("\n")

print("Duplicates have been written to duplicate.txt")
