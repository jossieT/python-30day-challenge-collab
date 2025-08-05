# Exercises: Level 1
#1. Write a function which count number of lines and number of words in a text. 
# All the files are in the data the folder: a) Read obama_speech.txt file and count number of lines and words b) 
# Read michelle_obama_speech.txt file and count number of lines and words c) Read donald_speech.txt file and 
# count number of lines and words d) Read melina_trump_speech.txt file and count number of lines and words
import re
import json
import os
from colorama import Style, Fore, init
init(autoreset=True)
import similarity as st
import csv


def line_and_word_counter(file):
    try:
        with open(f'D:\python-30day-challenge-collab\exercises\data/{file}') as line_reader:
            lines = line_reader.readlines()
            line_count = len(lines)
            print(Fore.YELLOW + f"The number of lines in your file {file} are {Fore.RED} {line_count}")

        with open(f'D:\python-30day-challenge-collab\exercises\data/{file}') as word_reader:
            words = re.findall(r'\b\w+\b', word_reader.read().lower())
            print(Fore.CYAN + f"The number of words in your file {file} are {Fore.RED} {len(words)}")

    except FileNotFoundError:
        print(Fore.RED + "File Not Found.")

    
#2. Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages
def most_spoken_languages(file_name, number_of_languages):
    try:
        with open(f"D:/python-30day-challenge-collab/exercises/data/{file_name}", 'r', encoding='utf-8') as f:
            country_data = json.load(f)
        # Create a dictionary to count languages
        language_count = {}
        for country in country_data:
            languages = country.get('languages', [])
            for language in languages:
                if language in language_count:
                    language_count[language] += 1
                else:
                    language_count[language] = 1

        # Sort languages by count
        most_spoken = sorted(language_count.items(), key=lambda x: x[1], reverse=True)[:number_of_languages]
        print(Fore.GREEN + "Most spoken languages:")
        for language, count in most_spoken:
            print(f"({Fore.RED} + {language}: {Fore.GREEN} + {count})")

    except FileNotFoundError:
        print("File Not Found.")
        return

#3. Read the countries_data.json data file in data directory, 
# create a function that creates a list of the ten most populated 
def most_populated_countries(file_name, number_of_countries):
    with open(f"D:/python-30day-challenge-collab/exercises/data/{file_name}", 'r', encoding='utf-8') as file:
        country_data = json.load(file)
        country_data_list = []
        for country in country_data:
            name = country.get('name', 'Unknown')
            population = country.get('population', 0)
            country_data_list.append({"country": name, "population": population})

        # Sort countries by population
        most_populated = sorted(country_data_list, key=lambda x: x["population"], reverse=True)[:number_of_countries]
        print(Fore.BLUE + "Most populated countries:")
        print(most_populated)


            

#. Exercises: Level 2
#4. Extract all incoming email addresses as a list from the email_exchange_big.txt file.

def extract_email_addresses(file_name):
    try:
        with open(f"D:/python-30day-challenge-collab/exercises/data/{file_name}", 'r', encoding='utf-8') as file:
            content = file.read()
            # Use regex to find all email addresses
            email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
            emails = re.findall(email_pattern, content)
            email_collection = {}
            print(Fore.CYAN + "Extracted email addresses:")
            for i in range(len(emails)):
                if emails[i] in email_collection:
                    email_collection[emails[i]] += 1
                else:
                    email_collection[emails[i]] = 1
            
            print(email_collection)


    except FileNotFoundError:
        print(Fore.RED + "File Not Found.")
    except Exception as e:
        print(f"{Fore.RED} + An error occurred: {e}")


#5. Find the most common words in the English language. 
# Call the name of your function find_most_common_words, it will take two parameters - a string or 
# a file and a positive integer, indicating the number of words. Your function will return an array of tuples 
# in descending order. Check the output
def find_most_common_words(file_name, numbers_to_display):
    try:
        with open(f"D:\python-30day-challenge-collab\exercises\data/{file_name}", 'r', encoding='utf-8') as f:
            file = f.read()
            words = re.findall(r'\b\w+\b', file.lower())
            word_dictionary = {}
            word_list = []
            for i in range(len(words)):
                if words[i] in word_dictionary:
                    word_dictionary[words[i]] += 1
                else:
                    word_dictionary[words[i]] = 1
            most_common_words = sorted(word_dictionary, key=lambda x: x[1], reverse=True)[:numbers_to_display]
            for key, value in most_common_words:
                word_list.append((key, value))
            return word_list

    except FileNotFoundError as e:
        print(f"An error occurred: {e}")
    except TypeError as e:
        print(f"An error occurred: {e}")

#6. Use the function, find_most_frequent_words to find: a) The ten most frequent words used in Obama's speech b) 
# The ten most frequent words used in Michelle's speech c) The ten most frequent words used in Trump's speech d) 
# The ten most frequent words used in Melina's speech

def find_most_frequent_words(file_name):
    try:
        with open(f"D:\python-30day-challenge-collab\exercises\data/{file_name}", 'r', encoding='utf-8') as f:
            file = f.read()
        words = re.findall(r'\b\w+\b', file.lower())
        word_dictionary = {}
        frequent_words_list = []
        for i in range(len(words)):
            if words[i] in word_dictionary:
                    word_dictionary[words[i]] += 1
            else:
                word_dictionary[words[i]] = 1

        most_common_words = sorted(word_dictionary.items(), key=lambda x: x[1], reverse=True)

        # Find the maximum frequency
        if most_common_words:
            max_freq = most_common_words[0][1]

        # Print all words with the maximum frequency
            print(f"{Fore.GREEN} Most frequent words:")
            for word, freq in most_common_words:
                if freq == max_freq:
                    print(f"({Fore.MAGENTA}  {word}: {Fore.BLUE} {freq})")
                else:
                    break  # Stop when frequency decreases
        else:
            print("No words found.")
            
        return frequent_words_list

    except FileNotFoundError as e:
        print(f"An error occurred: {e}")
    except TypeError as e:
        print(f"An error occurred: {e}")    


#7. Write a python application that checks similarity between two texts. It takes a file or a string as a parameter 
# and it will evaluate the similarity of the two texts. For instance check the similarity between the transcripts of 
# Michelle's and Melina's speech. You may need a couple of functions, function to clean the text(clean_text), 
# function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity).
# List of stop words are in the data 
def clean_text(file_or_text):
   
    try:
        file_path = os.path.join("D:/python-30day-challenge-collab/exercises/data", file_or_text)
        with open(file_path, 'r', encoding='utf-8') as f:
            file_content = f.read()
        text = file_content.lower()
        cleaned_text = re.sub(r'[^a-zA-Z0-9.\s]', '', text)
    except FileNotFoundError as e:
            print(f"An error occurred with {file_or_text}: {e}")
    return cleaned_text


def remove_support_words(file_or_text):
    # ---- Define Stopwords ----
    stopwords = {
        'the', 'is', 'at', 'which', 'on', 'and', 'a', 'an', 'of', 'to', 'in',
        'that', 'it', 'for', 'with', 'as', 'by', 'from', 'this', 'are', 'was',
        'be', 'or', 'but', 'not', 'has', 'have', 'had', 'were', 'am', 'so', 'if', 'will'
    }
    file_name = clean_text(file_or_text)
    text = file_name.lower()
    words = re.findall(r'\b\w+\b', text)
    filtered_words = [word for word in words if word not in stopwords]
    return filtered_words  # Return as list of words

    
def check_text_similarity(file1, file2):
    text1 = remove_support_words(file1)
    text2 = remove_support_words(file2)
    jac_sim = st.jaccard_similarity(text1, text2)
    cos_sim = st.cosine_similarity(text1, text2)
    seq_sim = st.sequence_similarity(' '.join(text1), ' '.join(text2))
    print(f"\nJaccard Similarity: {jac_sim:.2f}")
    print(f"Cosine Similarity : {cos_sim:.2f}")
    print(f"Sequence Similarity: {seq_sim:.2f}")

#8. Find the 10 most repeated words in the romeo_and_juliet.txt
def most_repeated_words():
    try:
        with open ("D:/python-30day-challenge-collab/exercises/data/romeo_and_juliet.txt", 'r', encoding='utf-8') as f:
            file_content = f.read()
        repeated_words = {}
        words = re.findall(r'\b\w+\b', file_content.lower())
        for word in words:
            if word in repeated_words:
                repeated_words[word] += 1
            else:
                repeated_words[word] = 1
        repeated_words_sorted = sorted(repeated_words.items(), key=lambda x:x[1], reverse=True)[:10]
        return repeated_words_sorted

    except FileNotFoundError as e:
        print(f"An error occurred with romeo_and_juliet.txt: {e}")


#9. Read the hacker news csv file and find out: a) Count the number of lines containing python or Python b) 
# Count the number lines containing JavaScript, javascript or Javascript c) Count the number lines containing 
# Java and not JavaScript

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




if __name__ == "__main__":

    file = input("Enter the file name you want to view:")
    line_and_word_counter(file=file)
    most_spoken_languages(file_name="countries_data.json", number_of_languages=10)
    most_populated_countries(file_name="countries_data.json", number_of_countries=10)
    extract_email_addresses("email_exchanges.txt")
    find_most_frequent_words("donald_speect.txt")
    print(most_repeated_words())
    check_text_similarity('donald_speech.txt', 'obamas_speech.txt')
    keyword_filteration()
