import re
from collections import Counter
# Exercises: Level 1
#1. What is the most frequent word in the following paragraph?
def word_extractor():
    paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

    # 1. Extract all words using regex, ignore punctuation
    words = re.findall(r'\b\w+\b', paragraph.lower())  # convert to lowercase to avoid case differences

    # 2. Count word frequencies
    word_counts = Counter(words)

    # 3. Sort by frequency (descending), then by word (optional)
    sorted_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))

    # 4. Convert to desired format (tuple with count first)
    formatted_output = [(count, word) for word, count in sorted_counts]

    # 5. Print result
    print(formatted_output)

#2. The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 
# 0 at origin, 4 and 8 in the positive direction. 
# Extract these numbers from this whole text and find the distance between the two furthest particles.
def particle_distance():
    points = ['-12', '-4', '-3', '-1', '0', '4', '8']
    regular_expressionn = r'^-\d+|\d+$'  # Matches negative and positive integers
    sorted_points = []
    for number in points:
        matches = re.findall(regular_expressionn, number)
        sorted_points.append(int(matches[0]) if matches else 0)

    distance = max(sorted_points) - min(sorted_points) # 20
    print(f"The distance between the two furthest particles is: {distance}")

# Exercises: Level 2
#1. Write a pattern which identifies if a string is a valid python variable
def is_valid_python_identifier(identifier):
    """
    Check if the given identifier is a valid Python identifier.
    A valid identifier starts with a letter or underscore, followed by letters, digits, or underscores.
    """
    regex = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    return bool(re.match(regex, identifier))

# Exercises: Level 3
#1. Clean the following text. After cleaning, count three most frequent words in the string.

def cleaning_and_counting():
    sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. 
    There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. 
    ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
    # Clean the text by removing unwanted characters
    cleaned_text = re.sub(r'[%$@&;#]', '', sentence)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()

    print(cleaned_text)

    print(most_frequent_words(cleaned_text)) # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]
def most_frequent_words(text):
    """    Count the three most frequent words in the given text.
    """
    words = re.findall(r'\b\w+\b', text)  # Extract words and convert to lowercase
    word_counts = Counter(words)  # Count word frequencies
    most_common = word_counts.most_common(3)  # Get the three most common words
    print(word_counts)  # Print all word counts for debugging
    return [(count, word) for word, count in most_common]  # Return as list of tuples

if __name__ == "__main__":

    word_extractor()
    particle_distance()
    # Test the identifier validation function
    test_identifiers = ['valid_identifier', 'invalid-identifier', '123invalid', '_valid123', 'invalid@char']
    for identifier in test_identifiers:
        print(f"'{identifier}' is a valid Python identifier: {is_valid_python_identifier(identifier)}")
    cleaning_and_counting()
    


