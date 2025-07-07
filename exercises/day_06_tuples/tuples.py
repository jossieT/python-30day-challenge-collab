# Exercises: Level 1
#1. Create an empty tuple
empty_tuple = ()
#2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
my_sisters = ('Emebet', 'Banchayehu', 'Worknesh')
my_brothers = ('Asrat', 'Belayneh', 'Habtemariyam')
#3. Join brothers and sisters tuples and assign it to siblings
siblings = my_sisters + my_brothers
#4. How many siblings do you have?
print(len(siblings))
#5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
my_list = list(siblings)
family_members  = my_list + ["Azeneg", "Yazew"]
# Exercises: Level 2
#1. Unpack siblings and parents from family_members
siblings = family_members[:6]
parents = family_members[6:8]
#2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('lemon', 'orange', 'pinapple')
vegetables = ('cabbage', 'potato', 'tomato', 'banana')
animal_products = ('yogouhrt', 'milk', 'chease', 'meat')
food_stuff_tp = fruits + vegetables + animal_products
#3. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_list = list(food_stuff_tp)
#4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
if len(food_stuff_list) % 2 == 0:
    middle_item = food_stuff_list[len(food_stuff_list)/2-1: len(food_stuff_list)/2 +1]
else:
    middle_item = food_stuff_list[len(food_stuff_list)//2]

#5. Slice out the first three items and the last three items from food_staff_lt list
first_three_items = food_stuff_list[:3]
last_three_items = food_stuff_list[-3:]
#6. Delete the food_staff_tp tuple completely
del food_stuff_tp
#7. Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)

print('Iceland' in nordic_countries)