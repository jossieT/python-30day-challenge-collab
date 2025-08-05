import csv
from colorama import Style, Fore, init
init(autoreset=True)

def keyword_filteration():
    # Initialize Counters
    python_count = 0
    javascript_count = 0
    java_only_count = 0

    # Open CSV File
    with open('d:\python-30day-challenge-collab\exercises\data\hacker_news.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            # Join all columns into one line of text (in case keywords are in any column)
            line = ' '.join(row).lower()

            # a) Count lines containing "python" (case-insensitive)
            if 'python' in line:
                python_count += 1

            # b) Count lines containing "javascript" (all variants)
            if 'javascript' in line:
                javascript_count += 1

            # c) Count lines containing "java" but NOT "javascript"
            if 'java' in line and 'javascript' not in line:
                java_only_count += 1
            
    # Print Results
    print(f" {Fore.CYAN} Lines containing 'Python' or 'python': {Fore.MAGENTA } {python_count}")
    print(f"{Fore.CYAN} Lines containing 'JavaScript' (any case variation): {Fore.MAGENTA } {javascript_count}")
    print(f"{Fore.CYAN} Lines containing 'Java' but not 'JavaScript': {Fore.MAGENTA } {java_only_count}")


keyword_filteration()