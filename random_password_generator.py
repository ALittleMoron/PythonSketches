from random import choice
import pyperclip
import sys

# if you need only letter+number password use selective_chars = all_chars[12:]
all_chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890' 

if len(sys.argv) == 3: 
    length = sys.argv[2]
    is_all_chars = sys.argv[3]
    if is_all_chars.lower() in ('strong', 'all') and is_all_chars.isalpha():
        password = ''
        for _ in range(length):
            password += choice(all_chars)
    elif is_all_chars.lower() in ('weak', 'low', 'no') and is_all_chars.isalpha():
        selective_chars = all_chars[12:]
        password = ''
        for _ in range(length):
            password += choice(selective_chars)
    pyperclip.copy(password)

elif len(sys.argv) == 2:
    selective_chars = all_chars[12:]
    password = ''
    for _ in range(length):
        password += choice(selective_chars)
    pyperclip.copy(password)

print(f"Your password: {password} was copied to the clipboard")
input("Press any key (not shutdown button) to exit... ")