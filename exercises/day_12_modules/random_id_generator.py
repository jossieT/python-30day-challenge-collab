import random
import string
#1. Writ a function which generates a six digit/character random_user_id

def random_user_id(length:int):
    characters = string.ascii_letters + string.digits  # A-Z, a-z, 0-9
    return ''.join(random.choices(characters, k=length))


