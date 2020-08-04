import random
import string

import lxml.html
import requests
from bs4 import BeautifulSoup

URL = 'https://simple.wikipedia.org/wiki/Wikipedia:List_of_1000_basic_words'
response = requests.get(URL)
source = response.text
soup = BeautifulSoup(source, 'lxml')

words = soup.find_all('dd')
words_list = []
for word in words:
    words = word.text.replace('.', '').split(',')
    for word in words:
        words_list.append(word)


def get_secret_word(words_list):
    secret_word = random.choice(words_list)
    return secret_word


HANGMAN_PICS = ['''
     +---+
         |
         |
         |
        ===''', '''
     +---+
     O   |
         |
         |
        ===''', '''
     +---+
     O   |
     |   |
         |
        ===''', '''
     +---+
     O   |
    /|   |
         |
        ===''', '''
     +---+
     O   |
    /|\  |
         |
        ===''', '''
     +---+
     O   |
    /|\  |
    /    |
        ===''', '''
     +---+
     O   |
    /|\  |
    / \  |
        ===''']


def get_guess_word():
    print('All letters are in lowercase')
    while True:
        guess_word = input('Enter your guess word: ').lower()
        if guess_word in string.digits:
            print('Digits are not allowed, Please try again')
            continue
        if len(guess_word) != 1:
            print('You have to enter only one letter, Please try again')
            continue
        if guess_word not in string.ascii_lowercase:
            print('You have to enter a lowercase letter, Please try again')
            continue
        return guess_word


def display(tries, display_word, secret_word, HANGMAN_PICS):
    HANGMAN_PICS = [pic for pic in reversed(HANGMAN_PICS)]
    print(HANGMAN_PICS[tries])
    print()
    print(f'Remaining tries: {tries}')
    print(f'Your guess word: {"".join(display_word)}')

    if tries == 0:
        print('-*-*-GAMEOVER-*-*-')
    else:
        guess_word = get_guess_word()
        return guess_word


def valid(guess_word, dummy_secrect_word):
    dummy_secrect_word = [letter for letter in dummy_secrect_word]
    if guess_word in dummy_secrect_word:
        return True
    return False


def try_again():
    ask = input('Do you want to try agian(y/n): ').lower()
    return ask


def get_all_repeated_letters_with_indexes(word):
    word_dict = {}
    for letter in word:
        word_dict[letter] = []
        for index in range(len(word)):
            if word[index] == letter:
                word_dict[letter].append(index)
        word_dict[letter] = [index for index in reversed(word_dict[letter])]
    return word_dict


def play(words_list, HANGMAN_PICS):
    tries = 6
    secret_word = get_secret_word(words_list).strip().lower()
    dummy_secrect_word = [letter for letter in secret_word]
    display_word = '_'*len(secret_word)
    word_dict = get_all_repeated_letters_with_indexes(secret_word)
    print()
    print('-*-*-Welcome To The Hangman Game-*-*-')
    print(secret_word)
    while True:

        if tries > 0:
            if "".join(display_word) == "".join(secret_word):
                print('-*-*-Congratulations You Won-*-*-')
                ask = try_again()
                if ask == 'y':
                    play(words_list, HANGMAN_PICS)
                else:
                    break

        guess_word = display(tries, display_word, secret_word, HANGMAN_PICS)

        if tries == 0:
            ask = try_again()
            if ask == 'y':
                play(words_list, HANGMAN_PICS)
            else:
                break

        if valid(guess_word, dummy_secrect_word):
            display_word = [letter for letter in display_word]
            index = word_dict[guess_word][-1]
            word_dict[guess_word].pop(-1)
            display_word[index] = guess_word
            dummy_secrect_word.remove(guess_word)
        else:
            print('Wrong Guess')
            tries -= 1


play(words_list, HANGMAN_PICS)
