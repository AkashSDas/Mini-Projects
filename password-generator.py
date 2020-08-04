import random
import string


# Generating characters for password
def generate_password_characters():
    alphabets = string.ascii_letters
    alphabets = [alphabet for alphabet in alphabets]

    numbers = string.digits
    numbers = [number for number in numbers]

    special_characters = string.punctuation
    special_characters = [
        special_character for special_character in special_characters]

    return [alphabets, numbers, special_characters]


# Creating a 15 character random password
def password_generator():
    characters = generate_password_characters()

    password = []
    for _ in range(15):
        character_list = characters[random.randint(0, len(characters)-1)]
        password_character = character_list[random.randint(
            0, len(character_list)-1)]
        password.append(password_character)

    password = "".join(password)
    return password


print(password_generator())
