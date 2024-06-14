import requests
from bs4 import BeautifulSoup
import json

def get_image_page_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    image_page_links = []

    # Find all the links to the individual image pages
    for link in soup.find_all('a', class_='mw-file-description'):
        image_page_links.append("https://commons.wikimedia.org" + link['href'])

    return image_page_links

def get_image_data(image_page_url):
    response = requests.get(image_page_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the title from the description div
    description_div = soup.find('div', class_='description mw-content-ltr en')
    if description_div:
        description_text = description_div.get_text(strip=True)
        # Extract the text between "featuring" and "by"
        if "featuring" in description_text and "by" in description_text:
            title = description_text.split("featuring")[1].split("by")[0].strip()
        else:
            title = "Unknown Title"
    else:
        # Fallback to the h1 title if the description div is not found
        title_tag = soup.find('h1', class_='firstHeading')
        title = title_tag.text.strip()

    # Find the preview image URL
    full_image_link = soup.find('div', class_='fullImageLink')
    if full_image_link:
        img_tag = full_image_link.find('a')
        img_url = img_tag['href']
    else:
        raise ValueError("Full image link not found")

    return {"url": img_url, "title": title}

# URLs to scrape
urls = [
    "https://commons.wikimedia.org/wiki/Category:Weird_Tales_covers",
    "https://commons.wikimedia.org/w/index.php?title=Category:Weird_Tales_covers&filefrom=1953-05%0AWeird+Tales+May+1953.jpg#mw-category-media"
]

all_image_data = []
for url in urls:
    image_page_links = get_image_page_links(url)
    for link in image_page_links:
        try:
            image_data = get_image_data(link)
            all_image_data.append(image_data)
        except Exception as e:
            print(f"Failed to scrape {link}: {e}")

# Save the data to a file
with open('image_data.json', 'w') as f:
    json.dump(all_image_data, f, indent=4)

print(f"Scraped {len(all_image_data)} images.")

def main():
    all_image_data = []
    for url in urls:
        image_page_links = get_image_page_links(url)
        for link in image_page_links:
            try:
                image_data = get_image_data(link)
                all_image_data.append(image_data)
            except Exception as e:
                print(f"Failed to scrape {link}: {e}")

    # Save the data to a file
    with open('image_data.json', 'w') as f:
        json.dump(all_image_data, f, indent=4)

    print(f"Scraped {len(all_image_data)} images.")


if __name__ == "__main__":
    # main()
    print("done")


