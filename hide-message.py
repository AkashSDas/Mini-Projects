import random
import string


def generate_random_characters():
    alphabets = string.ascii_letters
    numbers = string.digits
    special_characters = string.punctuation
    space_character = " "
    characters = f"{space_character}{alphabets}{numbers}{special_characters}"

    return characters[random.randint(0, len(characters)-1)]


def get_encrypt_message(message, separate):
    encrypt_message = ''
    count = 0
    for i in range(len(message)*separate+separate):
        if i % separate == 0 and i >= separate:
            encrypt_message += message[count]
            count += 1
        else:
            encrypt_message += generate_random_characters()

    return encrypt_message


def get_decrypt_message(encrypt_message, separate):
    decrypt_message = ''
    for i in range(len(encrypt_message)):
        if i % separate == 0 and i >= separate:
            decrypt_message += encrypt_message[i]

    return decrypt_message


message = 'I Love You'
separate = 1000

encrypt_message = get_encrypt_message(message, separate)
print(encrypt_message)

print()

decrypt_message = get_decrypt_message(encrypt_message, separate)
print(decrypt_message)
