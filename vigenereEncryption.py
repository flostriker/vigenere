#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 18:58:29 2020

@author: flo
"""


import secrets
from string import ascii_uppercase as l

def getMessage(x):
    whiteList = l
    return ''.join(filter(whiteList.__contains__, x.upper()))
    
def getKey(length):
    allowed = l
    return ''.join(secrets.choice(allowed) for i in range(length))
    





    

def getEncrypted(m, k):
    
    class CypherTable:
        def __init__(self):
          self.final_table = [l[i:]+l[:i] for i in range(len(l))]
        def get(self, b, a):
            val1 = self.final_table[0].index(a)
            new_letter = [i for i in self.final_table if i[0] == b][0][val1]
            return new_letter
    
    table = CypherTable()
        
    return ''.join([table.get(x,y) for x,y in zip(m,k)])
    
message = input("Input message: ")

message = getMessage(message)

key = getKey(len(message))

print("Message: ", message)
print("Key: ", key)
print("Encrypted message: ", getEncrypted(message, key))

