import json
from collections import Counter
import re
import string
import csv

#Exercises: Day 19
#Write a function which count number of lines and number of words in a text.
# All the files are in the data the folder: a) Read obama_speech.txt file and count
# number of lines and words b) Read michelle_obama_speech.txt file and count number
# of lines and words c) Read donald_speech.txt file and count number of lines and words d)
# Read melina_trump_speech.txt file and count number of lines and words

def number_of_words_lines(filepath):
    with open(filepath) as f:
        lines = f.read().splitlines()
        total_words = sum(len(line.split()) for line in lines)
        print("Number of lines:", len(lines))
        print("Total words:", total_words)

don_filepath = "./data/donald_speech.txt"
number_of_words_lines(don_filepath)

#Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages
def most_spoken_languages(filename, top_n):
    with open(filename, 'r', encoding='utf-8') as f:
        countries = json.load(f)

    language_counter = Counter()

    for country in countries:
        languages = country.get('languages', [])
        language_counter.update(languages)


    most_common = language_counter.most_common(top_n)
    return [(count, language) for language, count in most_common]


print(most_spoken_languages(filename='./data/countries_data.json', top_n=10))

#Read the countries_data.json data file in data directory, create a function that creates a
# list of the ten most populated countries
def most_populated_countries(filepath, top_num):
    with open(filepath, 'r', encoding='utf-8') as f:
        countries = json.load(f)
    population_list = [{'country': country['name'], 'population': country['population']} for country in countries]
    sorted_list = sorted(population_list, key=lambda x: x['population'], reverse=True)
    print(sorted_list)
    return sorted_list[:top_num]

print(most_populated_countries('./data/countries_data.json', 5))

#Exercises: Level 2
#Extract all incoming email addresses as a list from the email_exchange_big.txt file.

def extract_emails_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regular expression pattern for email
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

    emails = re.findall(email_pattern, content)
    unique_emails = list(set(emails))
    return unique_emails


print(extract_emails_from_file("./data/email_exchanges_big.txt"))

#Find the most common words in the English language. Call the name of your
# function find_most_common_words, it will take two parameters - a string or a file and a positive integer,
# indicating the number of words. Your function will return an array of tuples in descending order. Check the output
def find_most_common_words(filename, num):
    with open(filename, 'r', encoding='utf-8') as f:

        file_content = f.read()
    to_lower_case = file_content.lower()
    text = to_lower_case.translate(str.maketrans('', '', string.punctuation))
    words = text.split()

    word_counts = {}

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    return sorted_words[:num]


print(find_most_common_words("./data/sample.txt", 5))

#Use the function, find_most_frequent_words to find: a) The ten most frequent words used in Obama's speech b)
# The ten most frequent words used in Michelle's speech c) The ten most frequent words used in Trump's speech d)
# The ten most frequent words used in Melina's speech

print(find_most_common_words("./data/donald_speech.txt", 5))
print(find_most_common_words("./data/melina_trump_speech.txt", 5))
print(find_most_common_words("./data/michelle_obama_speech.txt", 5))
print(find_most_common_words("./data/obama_speech.txt", 5))

#Find the 10 most repeated words in the romeo_and_juliet.txt
def word_count_most_repeated(filename, num):
    with open(filename) as f:
        content = f.read()
    to_lower_case = content.lower()

    text = to_lower_case.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    word_counts = {}

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    return sorted_words[:num]

print(word_count_most_repeated("./data./romeo_and_juliet.txt", 10))


#Read the hacker news csv file and find out: a) Count the number of lines containing python or Python
# b) Count the number lines containing JavaScript, javascript or Javascript c) Count the number lines containing Java and not JavaScript
def analyze_hacker_news_csv(file_path):
    python_count = 0
    js_count = 0
    java_only_count = 0

    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            line = ' '.join(row).lower()

            # a) Contains "python"
            if 'python' in line:
                python_count += 1

            # b) Contains any variant of JavaScript
            if 'javascript' in line:
                js_count += 1

            # c) Contains "java" but not "javascript"
            if 'java' in line and 'javascript' not in line:
                java_only_count += 1

    print("a) Lines containing 'python' or 'Python':", python_count)
    print("b) Lines containing 'JavaScript', 'javascript', or 'Javascript':", js_count)
    print("c) Lines containing 'Java' but not any 'JavaScript' variant:", java_only_count)


file_path = './data/hacker_news.csv'
analyze_hacker_news_csv(file_path)







