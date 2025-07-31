# Exercises: Level 1
#1. Write a function which count number of lines and number of words in a text. 
# All the files are in the data the folder: a) Read obama_speech.txt file and count number of lines and words b) 
# Read michelle_obama_speech.txt file and count number of lines and words c) Read donald_speech.txt file and 
# count number of lines and words d) Read melina_trump_speech.txt file and count number of lines and words
import re
import json
import os
import sys
def line_and_word_counter(file):
    try:
        with open(f'D:/python-30day-challenge-collab/exercises/day_19_file_handling/speech_files/{file}') as f:
            lines = f.readlines()
            line_count = len(lines)
            print(f"The number of lines in your file {file} are {line_count}")
        with open(f'D:/python-30day-challenge-collab/exercises/day_19_file_handling/speech_files/{file}') as f:
            words = re.findall(r'\b\w+\b', f.read().lower())
            print(f"The number of words in your file {file} are {len(words)}")

    except FileNotFoundError:
        print("File Not Found.")

    
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
        print("Most spoken languages:")
        for language, count in most_spoken:
            print(f"({language}: {count})")

    except FileNotFoundError:
        print("File Not Found.")
        return

#3. Read the countries_data.json data file in data directory, 
# create a function that creates a list of the ten most populated 
def most_populated_countries(file_name, number_of_countries):
    with open(f"D:/python-30day-challenge-collab/exercises/data/{file_name}", 'r', encoding='utf-8') as file:
        country_data = json.load(file)

#. Exercises: Level 2
#4. Extract all incoming email addresses as a list from the email_exchange_big.txt file.


#5. Find the most common words in the English language. 
# Call the name of your function find_most_common_words, it will take two parameters - a string or 
# a file and a positive integer, indicating the number of words. Your function will return an array of tuples 
# in descending order. Check the output


#6. Use the function, find_most_frequent_words to find: a) The ten most frequent words used in Obama's speech b) 
# The ten most frequent words used in Michelle's speech c) The ten most frequent words used in Trump's speech d) 
# The ten most frequent words used in Melina's speech


#7. Write a python application that checks similarity between two texts. It takes a file or a string as a parameter 
# and it will evaluate the similarity of the two texts. For instance check the similarity between the transcripts of 
# Michelle's and Melina's speech. You may need a couple of functions, function to clean the text(clean_text), 
# function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity).
# List of stop words are in the data 



#8. Find the 10 most repeated words in the romeo_and_juliet.txt


#9. Read the hacker news csv file and find out: a) Count the number of lines containing python or Python b) 
# Count the number lines containing JavaScript, javascript or Javascript c) Count the number lines containing 
# Java and not JavaScript



if __name__ == "__main__":

    file = input("Enter the file name you want to view:")
    line_and_word_counter(file=file)
    most_spoken_languages(file_name="countries_data.json", number_of_languages=10)