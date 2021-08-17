import nltk
import re

from nltk.corpus import words,names
nltk.download('words',quiet=True)
nltk.download('names',quiet=True)

word_list = words.words()
name_list = names.words()

alphabet='abcdefghijklmnopqrstuvwxyz'
def encrypt(text_phrase,numeric_shift):
    encrypted_text = ''
    # print(len(alphabet))
    for i in text_phrase:
        position = alphabet.find(i)
        shifter = (position+numeric_shift)%26
        encrypted_text+=alphabet[shifter]
    return encrypted_text    
    # print(encrypted_text)    
# encrypt('abc',27)

def decrypt(encry_text,numeric_shift):
    decrypted_text=''
    for i in encry_text:
        position = alphabet.find(i)
        shifter = (position-numeric_shift)%26
        decrypted_text+=alphabet[shifter]
    return decrypted_text
    # print(decrypted_text)
# decrypt('bcd',1)

def crack(encrypted_message):
    message_splitter = encrypted_message.split()
    counter = 0
    for i in message_splitter:
        word = re.sub(r'[^A-Za-z]+','', i)
        if word in word_list or word in name_list:
            counter += 1
        else:
            pass
    return counter