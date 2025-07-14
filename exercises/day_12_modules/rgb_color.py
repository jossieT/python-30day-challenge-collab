import random
#3.Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
def rgb_color_gen():
    rgb_colors = []
    for _ in range(3):
        color_value = random.randint(0, 255)
        rgb_colors.append(color_value)
    return tuple(rgb_colors)


print(f"#rgb({rgb_color_gen()})")  # Example usage, will print a random RGB color

# Exercises: Level 2
#1. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).

def list_of_hexa_colors(num_colors):
    hex_colors = []
    for _ in range(num_colors):
        hex_color = f"#{random.randint(0, 0xFFFFFF):06x}"
        hex_colors.append(hex_color)
    return hex_colors
#2. Write a function list_of_rgb_colors which returns any number of RGB colors in an array.

def list_of_rgb_colors(num_colors):
    rgb_colors = []
    for _ in range(num_colors):
        rgb_color = rgb_color_gen()
        rgb_colors.append(rgb_color)
    return rgb_colors
#3. Write a function generate_colors which can generate any number of hexa or rgb colors.
def generate_colors(num_colors, color_type):
    if color_type == "hex":
        return list_of_hexa_colors(num_colors)
    elif color_type == "rgb":
        return list_of_rgb_colors(num_colors)
    else:
        raise ValueError("Invalid color type. Please choose 'hex' or 'rgb'.")



# Exercises: Level 3
#1. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
def shuffle_list(input_list):
    shuffled_list = input_list[:]
    random.shuffle(shuffled_list)
    return shuffled_list
#2. Write a function which returns an array of seven random numbers in a range of 0-9. 
# All the numbers must be unique.
def unique_random_numbers():
    return random.sample(range(10), 7)