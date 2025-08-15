import requests
from bs4 import BeautifulSoup
import csv

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
