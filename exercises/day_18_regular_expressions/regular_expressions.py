import re
#Exercises: Day 18
#Exercises: Level 1
#1. What is the most frequent word in the following paragraph?
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
reg_patter = r'\b\w+\b'
words = re.findall(reg_patter, paragraph, re.I)
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

list_of_tuples = []
for word in word_count:
    list_of_tuples.append((word_count[word], word))
print(sorted(list_of_tuples, reverse = True))

#2. The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction,
# 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance
# between the two furthest particles.
text = '''The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 
0 at origin, 4 and 8 in the positive direction.'''

matches = re.findall(r'-?\d+', text)
points = [int(num) for num in matches]
sorted_points = sorted(points)
distance = points[len(points) - 1] - points[0]
print(distance)

#Exercises: Level 2
#1. Write a pattern which identifies if a string is a valid python variable
def is_valid_variable(value):
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    return bool(re.match(pattern, value))

print(is_valid_variable('first_name')) # True
print(is_valid_variable('first-name')) # False
print(is_valid_variable('1first_name')) # False
print(is_valid_variable('firstname')) # True

#Exercises: Level 3
#1. Clean the following text. After cleaning, count three most frequent words in the string.
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as 
                educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs.
                %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

def clean_text(txt):
    pattern = r'[%$@&#;!]'
    return re.sub(pattern, '', txt)

cleaned_text = clean_text(sentence)

def most_frequent_words(text):
    words = re.findall(r'\b\w+\b', text, re.I)
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    result = []
    for word, count in freq.items():
        if count >= 2:
            result.append((count, word))

    result.sort(reverse=True)
    return result
print(most_frequent_words(cleaned_text))