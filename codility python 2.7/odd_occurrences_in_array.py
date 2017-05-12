#!/usr/bin/env python
# -*- coding: utf-8 -*- 

def solution(A):
	result = 0
	for number in A:
		result ^= number
	return result