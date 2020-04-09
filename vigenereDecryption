#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 19:58:37 2020

@author: flo
"""

from string import ascii_uppercase as l

def decrypt(encrypted, key):
    class CypherTable:
        def __init__(self):
          self.final_table = [l[i:]+l[:i] for i in range(len(l))]
        def get(self, b, a):
            val1 = self.final_table[0].index(a)
            val2 = self.final_table[val1].index(b)
            
            
            return self.final_table[val2][0]
    
    table = CypherTable()
    
    return ''.join([table.get(x,y) for x,y in zip(encrypted,key)])
    
    
    
    
encrypted = input("Input encrypted message: ")

key = input("Input key: ")

print(decrypt(encrypted, key))
