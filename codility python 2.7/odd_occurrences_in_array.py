#!/usr/bin/env python
# -*- coding: utf-8 -*- 

def solution(A):
    # write your code in Python 2.7
    for m in A:
        if A.count(m) < 2:
            return m