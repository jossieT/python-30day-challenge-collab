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


