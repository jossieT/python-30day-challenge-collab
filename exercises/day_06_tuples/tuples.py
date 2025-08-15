#Exercises: Day 6 
#Exercises: Level 1
#1. Create an empty tuple
my_empty_tuple = ()
my_empty_tuple_constr = tuple()

#2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ("lidu", "yenu", "jerry", "mita")
brothers = ("getu", "enu", "nathi")

#3. Join brothers and sisters tuples and assign it to siblings
sibilings = sisters + brothers
print(sibilings)

#4. How many siblings do you have?
sibiling_count = len(sibilings)
print(f"I have {sibiling_count} sibilings")

#5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
sibiling_list = list(sibilings)
sibiling_list.append("mom")
sibiling_list.append("dad")
print(sibiling_list)
family_members = tuple(sibiling_list)
print(family_members)

#Exercises: Level 2
#1. Unpack siblings and parents from family_members
sibilings = family_members[0:7]
parents = family_members[7:9]

#2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits =  ("apple", "banana", "orange")
veg = ("carrot", "orange", "potato")
anim_prod = ("milk", "egg", "meat")
food_stuff_tp = fruits + veg + anim_prod
print(food_stuff_tp)

#3. Change the about food_stuff_tp tuple to a
food_stuff_lt = list(food_stuff_tp)

#4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
tp_length = len(food_stuff_tp)
middle_index = tp_length // 2
middle_item = (food_stuff_tp[middle_index:middle_index+1])
print(f"middle item {middle_item}")

#5. Slice out the first three items and the last three items from food_staff_lt list
list_length = len(food_stuff_lt)
first_three_items = food_stuff_lt[0:3]
last_three_items = food_stuff_lt[list_length-3:list_length+1]
print(f"The first three items are {first_three_items}")
print(f"The last three items are {last_three_items}")

#6. Delete the food_staff_tp tuple completely
#del food_staff_tp #commented on purpose

#7. Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

#Check if 'Estonia' is a nordic country
print("Estonia" in nordic_countries) # False
#Check if 'Iceland' is a nordic country
print("Iceland" in nordic_countries) # True