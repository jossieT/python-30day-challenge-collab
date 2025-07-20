# Exercises: Day 17
names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia'] 
#1. Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, 
# and ru respectively.
*nordic_countries, es, ru = names
print(f"nordic_countries = {nordic_countries}\nEstonia = {es}\nRussia = {ru}")