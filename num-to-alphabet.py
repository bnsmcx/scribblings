#!/usr/bin/env python3

import sys

# get input from stdin
coded_message = [n.split() for n in sys.stdin][0] 
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for i in range(26):
    decoded_message = []

    for j in range(len(coded_message)):
        code_word = coded_message[j].split('-')
        decoded_word = ''

        for char in code_word:
            if char == ' ':
                decoded_word.append(char)
            else:
                index = int(char) + i
                index = index - 25 if index > 25 else index
                char = alphabet[index]
                decoded_word += char
        decoded_message.append(decoded_word)

    for word in decoded_message:
        print(word, end=" ") 
    
    print()


