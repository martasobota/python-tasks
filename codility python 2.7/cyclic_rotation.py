#!/usr/bin/env python
# -*- coding: utf-8 -*- 

def solution(A, K):
    if len(A) == 0:
        return 0
    elif K == 0:
        return A
    else:
        m = K % len(A)
        return A[-m:] + A[:-m]