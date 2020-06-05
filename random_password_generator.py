from random import randint, choice
from pyperclip import copy as pypercopy

# if you need only letter+number password use selective_chars = all_chars[12:]
all_chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890' 

def password_generator(is_all_chars:bool, length:int):
    if not length:
        length = 0
    if type(is_all_chars) is not bool or type(length) is not int:
        raise Exception("is_all_chars is not bool type or length is not int type")

    if is_all_chars is True:
        password = ''
        for _ in range(length):
            password += choice(all_chars)
    else:
        selective_chars = all_chars[12:]
        password = ''
        for _ in range(length):
            password += choice(selective_chars)
    pypercopy(password)
    return password

if __name__ == "__main__":
    while(True):
        # choice_type = input("Do you want to get password with special chars(+-/*!$ etc.)? [Y/N]")
        # if choice_type == 'Y':
        #     choice_type = True
        # elif choice_type == 'N':
        #     choice_type = False
        # else:
        #     continue
        choice_length = int(input("length: "))
        a = password_generator(False, choice_length)
        print(a)
        if input() != '':
            continue
        else:
            break