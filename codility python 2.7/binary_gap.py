#!/usr/bin/env python
# -*- coding: utf-8 -*- 

def solution(N):
    
    binary = str(bin(N)).strip("0b")
    binary_length = len(binary)
    temp = 0
    result = 0
        
    for n in range(binary_length):
        if binary[n] == '0':
            temp += 1
        elif binary[n] =='1':
            if result < temp:
                result = temp
            temp = 0
    return result

# print solution(5402)
# print solution(32)
# print solution(475)