"""
@author : majdoor
"""

#!usr/bin/python3

n = int(input())
if(n==2):
    print("NO")
else:
    print(("YES","NO")[n%2])