# String Exercises – Day 4

# 1. Concatenate 'Thirty', 'Days', 'Of', 'Python' to a single string
string1 = 'Thirty'
string2 = 'Days'
string3 = 'Of'
string4 = 'Python'
space = ' '
# Concatenating the strings with spaces
fullString = string1 + space + string2 + space + string3 + space + string4
print(fullString)

# 2. Concatenate 'Coding', 'For', 'All'
string12 = 'Coding'
string22 = 'For'
string32 = 'All'
space2 = ' '
fullString2 = string12 + space2 + string22 + space2 + string32
print(fullString2)
print('-' * 40)

# 3. Declare a variable named company and assign it to 'Coding For All'
company = 'Coding For All'

# 4. Print the variable company
print(company)
print('-' * 40)

# 5. Print the length of the company string
print('Length:', len(company))
print('-' * 40)

# 6. Change all the characters to uppercase
print(company.upper())
print('-' * 40)

# 7. Change all the characters to lowercase
print(company.lower())
print('-' * 40)

# 8. Use capitalize(), title(), swapcase()
print(company.capitalize())
print(company.title())
print(company.swapcase())
print('-' * 40)

# 9. Cut(slice) out the first word of Coding For All string
print(company[7:])
print('-' * 40)

# 10. Check if Coding For All contains 'Coding'
print('Coding' in company)
print(company.index('Coding'))
print(company.find('Coding'))
print('-' * 40)

# 11. Replace 'Coding' with 'Python'
print(company.replace('Coding', 'Python'))
print('-' * 40)

# 12. Change 'Python for Everyone' to 'Python for All'
phrase = 'Python for Everyone'
print(phrase.replace('Everyone', 'All'))
print('-' * 40)

# 13. Split 'Coding For All' by space
print(company.split())
print('-' * 40)

# 14. Split companies by comma
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(','))
print('-' * 40)

# 15. Character at index 0 in 'Coding For All'
print(company[0])
print('-' * 40)

# 16. Last index of 'Coding For All'
print(company[-1])
print('-' * 40)

# 17. Character at index 10
print(company[10])
print('-' * 40)

# 18. Acronym for 'Python For Everyone'
acronym1 = ''.join([w[0] for w in 'Python For Everyone'.split()])
print(acronym1)
print('-' * 40)

# 19. Acronym for 'Coding For All'
acronym2 = ''.join([w[0] for w in company.split()])
print(acronym2)
print('-' * 40)

# 20. Position of first 'C' in 'Coding For All'
print(company.index('C'))
print('-' * 40)

# 21. Position of first 'F' in 'Coding For All'
print(company.index('F'))
print('-' * 40)

# 22. rfind last 'l' in 'Coding For All People'
print('Coding For All People'.rfind('l'))
print('-' * 40)

# 23. First occurrence of 'because' in sentence
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))
print('-' * 40)

# 24. Last occurrence of 'because' in sentence
print(sentence.rindex('because'))
print('-' * 40)

# 25. Slice out 'because because because'
because_phrase = 'because because because'
start = sentence.find(because_phrase)
end = start + len(because_phrase)
print(sentence[start:end])
print('-' * 40)

# 26. Find position of first 'because'
print(sentence.find('because'))
print('-' * 40)

# 27. Slice out 'because because because' again
print(sentence[start:end])
print('-' * 40)

# 28. Does 'Coding For All' start with 'Coding'?
print(company.startswith('Coding'))
print('-' * 40)

# 29. Does 'Coding For All' end with 'coding'?
print(company.endswith('coding'))
print('-' * 40)

# 30. Remove trailing spaces
print('   Coding For All      '.strip())
print('-' * 40)

# 31. isidentifier()
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())
print('-' * 40)

# 32. Join libraries with hash and space
libs = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(libs))
print('-' * 40)

# 33. New line escape
print('I am enjoying this challenge.\nI just wonder what is next.')
print('-' * 40)

# 34. Tab escape
print('Name\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')
print('-' * 40)

# 35. String formatting: area of a circle
radius = 10
area = 3.14 * radius ** 2
print(f'The area of a circle with radius {radius} is {int(area)} meters square.')
print('-' * 40)

# 36. String formatting: math operations
x, y = 8, 6
print(f'{x} + {y} = {x + y}')
print(f'{x} - {y} = {x - y}')
print(f'{x} * {y} = {x * y}')
print(f'{x} / {y} = {x / y:.2f}')
print(f'{x} % {y} = {x % y}')
print(f'{x} // {y} = {x // y}')
print(f'{x} ** {y} = {x ** y}')
print('-' * 40)
