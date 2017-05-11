#!/usr/bin/env python
# -*- coding: utf-8 -*- 

def solution(A):
    for m in A:
        if A.count(m) < 2:
            return m