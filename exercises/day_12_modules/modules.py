from random import random, randint
import string

#Exercises: Day 12
#Exercises: Level 1
#1. Writ a function which generates a six digit/character random_user_id.
def random_user_id():
    chars = string.ascii_letters + string.digits
    random_id = ''
    for char in range(6):
        index = randint(0, len(chars) - 1)
        random_id += chars[index]
    return random_id
print(random_user_id())

#2. Modify the previous task. Declare a function named user_id_gen_by_user.
# It doesn’t take any parameters but it takes two inputs using input().
# One of the inputs is the number of characters and the second input is
# the number of IDs which are supposed to be generated.
def user_id_gen_by_user():
    chars = string.ascii_letters + string.digits
    id_list = []
    num_of_chars = int(input("Enter number of chars: "))
    num_of_ids = int(input("Enter number of ids: "))
    for i in range(num_of_ids):
        random_id = ''
        for char in range(num_of_chars):
            index = randint(0, len(chars) - 1)
            random_id += chars[index]
        id_list.append(random_id)
        print(random_id)
    return id_list
print(user_id_gen_by_user())

#3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
def rgb_color_gen():
    rgb_color = []
    for i in range(3):
        value = randint(0, 255)
        rgb_color.append(value)
    return f"rgb({rgb_color[0]},{rgb_color[1]},{rgb_color[2]})"
print(rgb_color_gen())
#Exercises: Level 2
#1. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array
# (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols,
# 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
def list_of_hexa_colors():
    hexa_chars = "0123456789abcdef"
    hex_vals = ''
    for i in range(6):
        index = randint(0, len(hexa_chars) - 1)
        hex_vals += hexa_chars[index]
    return f"#{hex_vals}"
print(list_of_hexa_colors())

#2. Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors(n):
    rgb_list = []
    for num in range(n):
        rgb_color = []
        for i in range(3):
            value = randint(0, 255)
            rgb_color.append(value)
        rgb_list.append(f"rgb({rgb_color[0]},{rgb_color[1]},{rgb_color[2]})")
    return rgb_list
print(list_of_rgb_colors(2))

#3. Write a function generate_colors which can generate any number of hexa or rgb colors.
def generate_colors(type_of_color, number):
    hexa_val_list = []
    rgb_list = []

    if type_of_color == 'rgb':
        for i in range(number):
            rgb_color = []
            for _ in range(3):
                value = randint(0, 255)
                rgb_color.append(value)
            rgb_list.append(f"rgb({rgb_color[0]},{rgb_color[1]},{rgb_color[2]})")
        return rgb_list

    elif type_of_color == 'hexa':
        hexa_chars = "0123456789abcdef"
        for i in range(number):
            hex_vals = ''
            for _ in range(6):
                index = randint(0, len(hexa_chars) - 1)
                hex_vals += hexa_chars[index]
            hexa_val_list.append(f"#{hex_vals}")
        return hexa_val_list

    else:
        return ["Invalid color type"]

print(generate_colors('hexa', 3))
print(generate_colors('hexa', 1))
print(generate_colors('rgb', 3))
print(generate_colors('rgb', 1))

#Exercises: Level 3
#1. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled
def shuffle_list(lst):
    for i in range(len(lst) - 1, 0, -1):
        j = randint(0, i)
        lst[i], lst[j] = lst[j], lst[i]
    return lst

#2. Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def unique_random():
    unique_list = []
    while len(unique_list) < 7:
        num = randint(0, 9)
        if num in unique_list:
            continue
        else: unique_list.append(num)
    return unique_list
print(unique_random())


