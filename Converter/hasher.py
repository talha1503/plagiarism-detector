import os,hashlib

def hash1(text_array):
    hashed_list = []
    for groups in text_array:
        hash_func = hashlib.md5(groups.encode())
        hashed_list.append(hash_func.digest())

    return hashed_list

#driver
strr = []
n = int(input())

for i in range(0,n):
    x = input()
    strr.append(x)

hashed_list = hash1(strr)
for hash_words in hashed_list:
    print(hash_words)

