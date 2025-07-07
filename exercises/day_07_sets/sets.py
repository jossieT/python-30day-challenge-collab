# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
# Exercise: Level 1
#1. Find the length of the set it_companies
print(len(it_companies))
#2. Add 'Twitter' to it_companies
it_companies.add('Twitter')
#3. Insert multiple IT companies at once to the set it_companies
it_companies.update(['Telegram', "Yahoo", 'Ericsson', 'Cisco'])
#4. Remove one of the companies from the set it_companies
it_companies.remove('Google') # remove function raises an error wen the inteded element is not found

#5. What is the difference between remove and discard
it_companies.discard('Google') # discard function does not raise error when the inteded element is not found
# Exercises: Level 2
#1. Join A and B
Union = A.union(B)
#2. Find A intersection B
Intersection = A.intersection(B)

#3. Is A subset of B
print(A.issubset(B))
#4. Are A and B disjoint sets
print(A.isdisjoint(B))
#5. Join A with B and B with A
print(A.union(B))
print(B.union(A))
#6. What is the symmetric difference between A and B
print(A.symmetric_difference(B))
#7. Delete the sets completely
del A, B, it_companies
#print(A), print(B), print(it_companies) # These lines raise an error as the sets are not difined because I have deleted them in the above line 
# Exercises: Level 3
#1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)
print(f'list with length {len(age)} is greater than set with length {len(age_set)} because set does not allow duplicate elements.')
#2. Explain the difference between the following data types: string, list, tuple and set
"""
strings are immutable sequences of characters, while lists are mutable sequences that can contain elements of different types.
Tuples are immutable sequences, similar to lists, but cannot be changed after creation. Sets are unordered collections of unique elements.
"""
#3. I am a teacher and I love to inspire and teach people. 
# How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = 'I am a teacher and I love to inspire and teach people'
print(f'In the above sentence, {len(set(sentence.split()))} unique words are used')