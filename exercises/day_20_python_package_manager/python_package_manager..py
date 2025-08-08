import requests # importing the request module
import math
import requests
from bs4 import BeautifulSoup

def url_reader(url):

    response = requests.get(url) # opening a network and fetching a data
    print(response)
    print(response.status_code) # status code, success:200
    print(response.headers)     # headers information
    print(response.text) # gives all the text from the page


#2. Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
"""
    i. The min, max, mean, median, standard deviation of cats' weight in metric units.
    ii. The min, max, mean, median, standard deviation of cats' lifespan in years.
    iii. Create a frequency table of country and breed of cats
"""
def read_cats_api():

    url = 'https://api.thecatapi.com/v1/breeds'
    response = requests.get(url)
    cat_data = response.json()
    return cat_data
            
def get_statistics(numbers):
    n = len(numbers)
    total = sum(numbers)
    sorted_numbers = sorted(numbers)
    
    # Mean
    mean = total / n
    
    # Median
    if n % 2 == 0:
        median = (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
    else:
        median = sorted_numbers[n//2]
    
    # Standard Deviation
    variance = sum((x - mean) ** 2 for x in numbers) / (n - 1)
    std_dev = math.sqrt(variance)
    
    return {
        "min": min(numbers),
        "max": max(numbers),
        "mean": mean,
        "median": median,
        "std_dev": std_dev
    }


def get_weights(cat_data):
    weights = []

    for cat in cat_data:
        try:
            min_w, max_w = map(float, cat["weight"]["metric"].split(" - "))
            avg = (min_w + max_w) / 2
            weights.append(avg)
        except:
            pass
    return get_statistics(weights)

def get_life_span(cat_data):
    
    life_span = []
    for cat in cat_data:
        try:
            min_life, max_life = map(float, cat["life_span"].split("-"))
            avg_life = (min_life + max_life)/2
            life_span.append(avg_life)

        except:
            pass

    
    return get_statistics(life_span)

def frequency_table(cat_data):
    country_counts = {}

    for cat in cat_data:
        country = cat.get("origin", "Unknown")
        if country in country_counts:
            country_counts[country] += 1
        else:
            country_counts[country] = 1

    # Sort by count descending
    sorted_country_counts = sorted(country_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_country_counts

#3. Read the countries API and find
"""
the 10 largest countries
the 10 most spoken languages
the total number of languages in the countries API
"""

def read_countries_api():
    url = "https://restcountries.com/v3.1/region/europe"
    response = requests.get(url)
    country_data = response.json()
    surface_area = {}
    languages = {}
    for country in country_data:
        surface_area[country["name"]["common"]] = country["area"]
    

    sorted_area = sorted(surface_area.items(), key=lambda x: x[1], reverse=True)[:10]
    print(sorted_area) 

    for country in country_data:
        if "languages" in country:
            for language in country["languages"].values():
                if language in languages:
                    languages[language] += 1
                else:
                    languages[language] = 1
    print(languages)




#4. UCI is one of the most common places to get data sets for data science and machine learning. 
# Read the content of UCL (https://archive.ics.uci.edu/ml/datasets.php). 
# Without additional libraries it will be difficult, so you may try it with BeautifulSoup4

def read_ucl_content():
    url = "https://archive.ics.uci.edu/datasets"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, "html.parser")

    # This page uses expandable sections for each dataset
    datasets = []
    for section in soup.find_all("div", class_="dataset-item"):
        title = section.find("p", class_="dataset-heading").get_text(strip=True)
        info = section.find("p", class_="dataset-description").get_text(strip=True)
        datasets.append({"name": title, "description": info})

    # Display some examples
    for ds in datasets[:5]:
        print(ds)
    






if __name__ == "__main__":

    cat_data = read_cats_api()
    print(get_weights(cat_data))
    print(get_life_span(cat_data))
    print(frequency_table(cat_data))
    read_countries_api()
