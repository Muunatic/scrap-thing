import random
from database import database
import string

def get_valid_word(database):
    word = random.choice(database)
    while '-' in word or ' ' in word:
        word = random.choice(database)

        return word

def engine():
    word = get_valid_word(database)
    word_letters = set(database)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    user_letter = input('Bruhh:').upper()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)
    
    elif user_letter in used_letters:
        print('Kamu sudah menebaknya silahkan cari yang lain')
    
    else:
        print('Kamu salah')


user_input = input('Ketik untuk mengisi:')
print(user_input)