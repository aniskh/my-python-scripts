#!/usr/bin/env python3
#Python script to generate a random password with 12-16 characters

import string
import random

def random_passwd():
    #choose password lengh
    pwd_length = random.randint(12,16)
    #define possible alphanumeric to use
    alpha_list = "0123456789#$%&()*+,-./:;<=>?@[\]^_{|}~"
    # append alphabetic list
    characters_list = alpha_list + string.ascii_lowercase + string.ascii_uppercase
    #generate password
    password = ''
    for i in range (1, pwd_length):
        password = password + characters_list[random.randint(1,len(characters_list))]
    print (password)
def main():
    random_passwd()

if __name__ == "__main__":
    main()
