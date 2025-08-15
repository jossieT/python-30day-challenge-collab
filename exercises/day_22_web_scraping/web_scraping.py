import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'


def scrape_uci_datasets():
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        print(f"Page Title: {soup.title.get_text()}")
        print(f"Status Code: {response.status_code}")

        # Try multiple ways to find the main table
        table = None

        # Method 1: Look for table with specific class
        table = soup.find('table', class_='table-normal')

        # Method 2: If not found, look for any table with dataset information
        if not table:
            tables = soup.find_all('table')
            for t in tables:
                if 'dataset' in str(t).lower():
                    table = t
                    break

        # Method 3: As last resort, take the first large table
        if not table and len(soup.find_all('table')) > 0:
            table = soup.find_all('table')[0]

        if not table:
            print("Could not identify the main data table")
            return

        print("\nFound table. Here are the first few rows:")

        # Process table rows with better error handling
        rows = table.find_all('tr')[:10]  # Just show first 10 rows for demo
        for row in rows:
            cells = row.find_all(['td', 'th'])
            row_data = [cell.get_text(' ', strip=True) for cell in cells]
            print(row_data)

    except Exception as e:
        print(f"Error: {e}")


scrape_uci_datasets()
