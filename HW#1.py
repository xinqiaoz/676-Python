#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 16:14:10 2020

@author: Xinqiao Zhang
"""

###Python HW #1 

##Q1 

###(a)

list_1a = list(range(1,21))
print(list_1a)

###(b)

list_1b = list(range(20,0,-1))
print(list_1b)

###(c)


list_1c = list_1a + list_1b
del(list_1c[20])
print(list_1c)


###(d)

list_1d = 10 * [4,6,3]
print(list_1d)

###(e)

list_1e = list_1d + [4]
print(list_1e)



##Q2

import numpy as np

x = np.arange(3, 6.1, 0.1)
f = [np.exp(i) * np.cos(i) for i in x]
print(f)


##Q3 

x = []
x = list(range(1,26))
f = []
f = [2**i/i for i in x]
print(f)


##Q4 

###(a)

a = list_1a 
list_4a = [a[i-1]-a[20-i] for i in a]
print(list_4a)

###(b)

list_4b = [a[i-1] % 2 == 0 for i in a]
print(list_4b)


##Q5 

###(a)

with open('lorem.txt','r') as lorem_a:
    lines = lorem_a.readlines()
    lorem_a.close()

letter = ""
for line in lines:
    commasep = line.split(',')
    for c in commasep:
        periodsep = c.split('.')
        for x in periodsep:
            letter += x

lens = []
letter_list = letter.split(' ')
for x in letter_list:
    line = len(x)
    lens.append(line)
    
list_5a = [len([x for x in lens if 1 <= x <= 4])] + [len([x for x in lens if 5 <= x <= 7])] + [len([x for x in lens if x >= 8])]
print(list_5a)

###(b)

with open("lorem.txt") as lorem_b: 
    cap = lorem_b.read()

list_5b = list(filter(str.isupper, cap))
print(len(list_5b))

