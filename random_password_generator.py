from random import randint, choice

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
    return password

if __name__ == "__main__":
    a = password_generator(False, 24)
    print(a)