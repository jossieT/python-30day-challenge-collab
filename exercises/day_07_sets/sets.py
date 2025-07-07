#Exercises: Day 7
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Exercises: Level 1
#1. Find the length of the set it_companies
length_of_set = len(it_companies)
print(length_of_set)

#2. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

#3 Insert multiple IT companies at once to the set it_companies
local_it_companies_list = ['Addis Soft', 'SantiMpay', 'Telebirr']
it_companies.update(local_it_companies_list)
print(it_companies)

#4. Remove one of the companies from the set it_companies
it_companies.remove('Telebirr')
it_companies.discard('SantiMpay')
print(it_companies)

#5. What is the difference between remove and discard
#remove raises an error if the item is not found.
#discard does nothing if the item is not found

#Exercises: Level 2
#1. Join A and B
AB = A.union(B)
print(AB)

#2. Find A intersection B
A_int_B = A.intersection(B)
print(A_int_B)

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
#del it_companies

#Exercises: Level 3
#1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)
print(age_set)
#length of list is bigges as repeated values are dicarded in set

#2. Explain the difference between the following data types: string, list, tuple and set
#string (str)- Ordered, Immutable (can’t change characters), Stores text (characters)
#List Ordered, Mutable (can change items), Allows duplicates
#Tuple, Ordered, Immutable, Allows duplicates
#Set Unordered, Mutable, No duplicates

#3. I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence?
#Use the split methods and set to get the unique words.
txt = 'I am a teacher and I love to inspire and teach people'
text_set = set(txt.split())
print(text_set)
print(f"number of unique words used is {len(text_set)}")



