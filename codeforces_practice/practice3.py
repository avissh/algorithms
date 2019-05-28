#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 25 19:12:54 2019

@author: gk
"""

t = int(input()[2:]);s=input()
while t:s = s.replace('BG','GB');t-=1
print(s)