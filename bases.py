#!/usr/bin/env python
# -*- coding: utf-8 -*-

def toBase(num, base):
	list = []
	while num > 0:
		list.append(num % base)
		num//=base
	return int(''.join(map(str, list[::-1])))

#la ligne ci-dessus correspond à ceci en plus compact :
#(supposons que list contient [3, 2, 1])
#s = map(str, list[::-1])   # ['1','2','3']
#s = ''.join(s)          # '123'
#s = int(s)              # 123
#return s

def toDec(nStr, base):
	n, j = 0, 0
	for i in nStr:
		n += int(i)*base**(len(nStr)-j-1) #i * base^place du chiffre dans le nombre
		j += 1
	return n

print(toBase(256, 2))
print(toDec("100000000", 2))