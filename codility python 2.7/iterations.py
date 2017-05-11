#!/usr/bin/env python
# -*- coding: utf-8 -*- 

def exercise_1(n):
	for i in range(1, n+1):
		for j in range(i):
			print '*',
		print

# exercise_1(7)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def exercise_2(n):
	for i in range(n, 0, -1):
		for j in range(n - 1):
			print ' ',
		for j in range(2 * i - 1):
			print '*',
		print

# exercise_2(8)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

days = ['Monday', 'Tuesday', 'Wed']

for day in days:
	print day

