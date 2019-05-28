#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 25 18:39:57 2019

@author: majdoor
"""

n = int(input())
c1,c2,c3 = 0,0,0
count = 0
for i in range(0,n):
    a,b,c = [int(x) for x in (input().split(" "))]
    if a+b+c>1:
        count = count+1
print(count)
    