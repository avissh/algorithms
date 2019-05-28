#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 25 18:18:16 2019

@author: majdoor
"""

#!usr/bin/python3

n,k = [int(x) for x in (input().split(" "))]
a = [int(x) for x in input().split(" ")]
loc = a[k-1]
count = 0
for i in a:
    if(i>=loc and i>0):
        count = count+1
print(count)