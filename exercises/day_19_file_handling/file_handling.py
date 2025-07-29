import json
from collections import Counter
import re
import string

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






