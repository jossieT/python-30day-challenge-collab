from mypackage import arithmetics
from mypackage import greet

print(arithmetics.add_numbers(1,2,3,4,5))

print(greet.greet_person('Yosef', 'Teshome'))

#Exercises: Day 20
#Read this url and find the 10 most frequent words. romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
import requests
import string
romeo_and_juliet = 'https://www.gutenberg.org/files/1112/1112-0.txt'

response = requests.get(romeo_and_juliet)

def most_frequent_words(file):
    content = file.text
    to_lower_case = content.lower()

    text = to_lower_case.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:10]

print(most_frequent_words(response))

#Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
'''
    the min, max, mean, median, standard deviation of cats' weight in metric units.
    the min, max, mean, median, standard deviation of cats' lifespan in years.
    Create a frequency table of country and breed of cats
'''

import numpy as np

cats_api = 'https://api.thecatapi.com/v1/breeds'

response = requests.get(cats_api)

if response.status_code == 200:
    cat_breeds_data = response.json()
else:
    print(f"Error: {response.status_code}")
    exit()


weights_metric = []
for breed in cat_breeds_data:
    if "weight" in breed and "metric" in breed["weight"]:
        parts = breed["weight"]["metric"].split("-")
        if len(parts) == 2:
            min_w, max_w = map(float, [p.strip() for p in parts])
            weights_metric.append((min_w + max_w) / 2)  # Midpoint

# Calculate stats
if weights_metric:
    print(f"Min: {np.min(weights_metric):.2f} kg")
    print(f"Max: {np.max(weights_metric):.2f} kg")
    print(f"Mean: {np.mean(weights_metric):.2f} kg")
    print(f"Median: {np.median(weights_metric):.2f} kg")
    print(f"Std Dev: {np.std(weights_metric):.2f} kg")
else:
    print("No weight data found.")

import requests
import numpy as np

# Fetch data
url = "https://api.thecatapi.com/v1/breeds"
response = requests.get(url)
cat_breeds_data = response.json()

# Parse lifespans
lifespans = []
for breed in cat_breeds_data:
    if "life_span" in breed:
        parts = breed["life_span"].split("-")
        if len(parts) == 2:
            min_yrs, max_yrs = map(float, [p.strip() for p in parts])
            lifespans.append((min_yrs + max_yrs) / 2)  # Midpoint

# Calculate stats
if lifespans:
    print(f"Min lifespan: {np.min(lifespans):.1f} years")
    print(f"Max lifespan: {np.max(lifespans):.1f} years")
    print(f"Mean lifespan: {np.mean(lifespans):.1f} years")
    print(f"Median lifespan: {np.median(lifespans):.1f} years")
    print(f"Standard deviation: {np.std(lifespans):.1f} years")
else:
    print("No lifespan data found.")

from collections import defaultdict

# Fetch data
url = "https://api.thecatapi.com/v1/breeds"
response = requests.get(url)
cat_breeds_data = response.json()

# Count breeds per country
country_breed_counts = defaultdict(int)
for breed in cat_breeds_data:
    country = breed.get("origin", "Unknown").strip()
    if country:
        country_breed_counts[country] += 1

# Print sorted table
print("Country\t\tNumber of Breeds")
print("-----------------------------")
for country, count in sorted(country_breed_counts.items(), key=lambda x: x[1], reverse=True):
    print(f"{country}\t\t{count}")


#UCI is one of the most common places to get data sets for data science and machine learning. Read the content of UCL
# (https://archive.ics.uci.edu/ml/datasets.php). Without additional libraries it will be difficult, so you may try it with
# BeautifulSoup4

import requests
from bs4 import BeautifulSoup
import csv
from time import sleep

# Constants
BASE_URL = "https://archive.ics.uci.edu"
DATASETS_URL = f"{BASE_URL}/datasets"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}


def get_soup(url):
    """Fetch and parse a webpage."""
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return BeautifulSoup(response.text, 'html.parser')
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None


def extract_dataset_info(card):
    """Extract dataset details from a card element."""
    name = card.find('h3').get_text(strip=True) if card.find('h3') else "No name"
    description = card.find('p').get_text(strip=True) if card.find('p') else "No description"
    link = card.find('a')['href'] if card.find('a') else None
    return {
        "name": name,
        "description": description,
        "link": f"{BASE_URL}{link}" if link else "No link"
    }


def scrape_uci_datasets():
    """Main scraping function."""
    all_datasets = []
    page = 1

    while True:
        url = f"{DATASETS_URL}?page={page}" if page > 1 else DATASETS_URL
        print(f"Scraping page {page}...")

        soup = get_soup(url)
        if not soup:
            break

        cards = soup.select('div.p-4.border.rounded-lg')
        if not cards:
            break

        for card in cards:
            all_datasets.append(extract_dataset_info(card))

        # Check for next page
        next_button = soup.select_one('a[aria-label="Next"]')
        if not next_button:
            break

        page += 1
        sleep(1)  # Be polite to the server

    return all_datasets


def save_to_csv(datasets, filename='uci_datasets.csv'):
    """Save datasets to CSV file."""
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['name', 'description', 'link'])
        writer.writeheader()
        writer.writerows(datasets)
    print(f"Saved {len(datasets)} datasets to {filename}")


# Main execution
if __name__ == "__main__":
    datasets = scrape_uci_datasets()

    if datasets:
        print("\nSample datasets:")
        for dataset in datasets[:3]:
            print(f"Name: {dataset['name']}")
            print(f"Description: {dataset['description']}")
            print(f"Link: {dataset['link']}\n")

        save_to_csv(datasets)
    else:
        print("No datasets found.")
