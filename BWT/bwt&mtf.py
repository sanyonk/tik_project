from typing import List, Tuple, Union
from string import ascii_lowercase
import re

with open('bwt.txt', 'r') as f:
        a = f.readline().strip()
        a = re.sub(r'\s+', '', a)
        

#a = input("Enter a string:")

words = list(a)
list = []
for i in range(len(words)):
    word = a[-1] + a[:-1]
    new = ''.join(word)
    a = new
    list.append(new)
    i += 1

#print(list)
sort = sorted(list)
#print(sort)

check_word = []
for i in range(len(words)):
	element = sort[i]
	last = element[- 1]
	i = i + 1
	check_word.append(last)

code_word = ''.join(check_word)
#print(f'{code_word}, {sort.index(a)}')


'''
SYMBOLTABLE = list(ascii_lowercase)

def move2front_encode(strng, symboltable):
    sequence, pad = [], symboltable[::]
    for char in strng:
        indx = pad.index(char)
        sequence.append(indx)
        pad = [pad.pop(indx)] + pad
    return sequence

def move2front_decode(sequence, symboltable):
    chars, pad = [], symboltable[::]
    for indx in sequence:
        char = pad[indx]
        chars.append(char)
        pad = [pad.pop(indx)] + pad
    return ''.join(chars)


for s in ['bananaaa']:
	encode = move2front_encode(s, SYMBOLTABLE)
	print('%14r encodes to %r' % (s, encode), end=', ')
	decode = move2front_decode(encode, SYMBOLTABLE)
	print('which decodes back to %r' % decode)
	assert s == decode, 'Whoops!'
'''

del list

def m2f_e(s, st):
    return [[st.index(ch), st.insert(0, st.pop(st.index(ch)))][0] for ch in s]

def m2f_d(sq, st):
    return ''.join([st[i], st.insert(0, st.pop(i))][0] for i in sq)

ST = list('abcdefghijklmnopqrstuvwxyz')
for s in [code_word]:
    encode = m2f_e(s, ST[::])
    print('%14r encodes to %r' % (s, encode), end=', ')
    decode = m2f_d(encode, ST[::])
    #print('decodes back to %r' % decode)

print(sort.index(a))