import requests
from bs4 import BeautifulSoup
import csv

# Exercises: Day 22
#Scrape the following website and store the data as json file(url = 'http://www.bu.edu/president/boston-university-facts-stats/').
import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.bu.edu/president/boston-university-facts-stats/'


def scrape_bu_facts():
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        # Initialize dictionary to store all facts
        bu_facts = {
            "university_name": "Boston University",
            "source_url": url,
            "facts": []
        }

        # Find all fact sections - they're in divs with class 'facts-wrapper'
        sections = soup.find_all('div', class_='facts-wrapper')

        for section in sections:
            # Extract the category title
            category = section.find('h3')
            if not category:
                continue

            category_title = category.get_text(strip=True)

            # Initialize category dictionary
            category_data = {
                "category": category_title,
                "items": []
            }

            # Find all fact items in this section
            fact_items = section.find_all('div', class_='fact')

            for item in fact_items:
                # Extract number and description
                number = item.find('div', class_='number').get_text(strip=True) if item.find('div',
                                                                                             class_='number') else "N/A"
                description = item.find('div', class_='description').get_text(strip=True) if item.find('div',
                                                                                                       class_='description') else "N/A"

                category_data["items"].append({
                    "statistic": number,
                    "description": description
                })

            bu_facts["facts"].append(category_data)

        # Save to JSON file
        with open('bu_facts_stats.json', 'w', encoding='utf-8') as f:
            json.dump(bu_facts, f, indent=2, ensure_ascii=False)

        print("Successfully saved data to bu_facts_stats.json")
        return bu_facts

    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
    except Exception as e:
        print(f"Error: {e}")


# Run the scraper
scrape_bu_facts()

url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'


def scrape_presidents():
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        print(f"Page Title: {soup.title.get_text()}")
        print(f"Status Code: {response.status_code}")

        # Find the correct table - Wikipedia's presidential tables are usually class 'wikitable'
        table = soup.find('table', {'class': 'wikitable'})

        if not table:
            print("Presidents table not found")
            return

        print("\nFound presidents table. Saving to CSV...")

        # Prepare CSV file
        with open('us_presidents.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)

            # Process all rows
            for row in table.find_all('tr'):
                # Extract regular cells and header cells
                cells = row.find_all(['th', 'td'])

                # Clean each cell's text
                row_data = []
                for cell in cells:
                    # Remove references [1][2] etc.
                    text = cell.get_text(' ', strip=True)
                    text = ' '.join([word for word in text.split() if not word.startswith('[')])
                    row_data.append(text)

                # Write row to CSV
                if row_data:  # Only write if we have data
                    writer.writerow(row_data)

        print("Successfully saved to us_presidents.csv")

    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
    except Exception as e:
        print(f"Error: {e}")


scrape_presidents()
