#1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
str1, str2, str3, str4  = "Thirty", "Days", "Of", "Pthon"
combined_string = str1 + str2 + str3 + str4
#2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
str5, str6, str7 = "Coding", "For", 'All'
concatenated_string = str5 + str6 + str7
#3. Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"
#4. Print the variable company using print().
print(company)
#5. Print the length of the company string using len() method and print().
print(len(company))
#6. Change all the characters to uppercase letters using upper() method.
upper = company.upper()
#7. Change all the characters to lowercase letters using lower() method.
lower = company.lower()
#8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
capital = company.capitalize()
title = company.title()
swap = company.swapcase()
#9. Cut(slice) out the first word of Coding For All string.
first_word = company[:6]
print(first_word)
#10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.find("Coding"))
#11. Replace the word coding in the string 'Coding For All' to Python.
print(company.replace("Coding", "Python"))
#12. Change Python for Everyone to Python for All using the replace method or other methods.
company2 = "Python for everone"
print(company2.replace("For Everyone", "For All"))
#13. Split the string 'Coding For All' using space as the separator (split()) .
print(company.split())
#14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(", "))
#15. What is the character at index 0 in the string Coding For All.
print(company[0])
#16. What is the last index of the string Coding For All.
print(len(company) - 1)
#17. What character is at index 10 in "Coding For All" string.
print(company[10])
#18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
print("Python For Everyone".split()[0][0] + "." + "Python For Everyone".split()[1][0] + "." + "Python For Everyone".split()[2][0])
#19. Create an acronym or an abbreviation for the name 'Coding For All'.
print("Coding For All".split()[0][0] + "." + "Coding For All".split()[1][0] + "." + "Coding For All".split()[2][0])
#20. Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index("C"))
#21. Use index to determine the position of the first occurrence of F in Coding For All.
print(company.index("F"))
#22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(company.rfind("l"))
#23. Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(company.rfind("l"))
#24. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
first_occurrence = sentence.find("because")
#25. Use rindex to find the position of the last occurrence of the word because in the following sentence: 
last_occurrence = sentence.rindex("because")
#26. Slice out the phrase 'because because because' in the following sentence: 
phrase = sentence[31:55]
#27. Find the position of the first occurrence of the word 'because' in the following sentence: 
print(first_occurrence)
#28. Slice out the phrase 'because because because' in the following sentence:
print(phrase)
#29. Does ''Coding For All' start with a substring Coding?
print("Coding For All".startswith("Coding"))
#30. Does 'Coding For All' end with a substring coding?
print("Coding For All".endswith("Coding"))
#31. '   Coding For All      '  , remove the left and right trailing spaces in the given string.
print('   Coding For All      '.strip())
#32. Which one of the following variables return True when we use the method isidentifier():
print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())
#33. The following list contains the names of some of python libraries: 
# ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
back_end_tech = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = '# '.join(back_end_tech)
print(result)
#34. Use the new line escape sequence to separate the following sentences.
print("I am enjoying this challenge.\nI just wonder what is next.")
#35. Use a tab escape sequence to write the following lines.
print("Name\t Age\tCountry\t City")
print("Asabeneh 250\tFinland\t Helsinki")
#36. Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")
#37. Make the following using string formatting methods:
print(f"8 + 6 = {8 + 6}")
print(f"8 - 6 = {8 - 6}")
print(f"8 * 6 = {8 * 6}")
print(f"8 / 6 = {8 / 6}")
print(f"8 % 6 = {8 % 6}")
print(f"8 // 6 = {8 // 6}")
print(f"8 ** 6 = {8 ** 6}")