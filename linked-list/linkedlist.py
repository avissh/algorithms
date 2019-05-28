#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 25 19:20:57 2019
@author: majdoor
"""

class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None
    
    def get_data(self):
        return self.data
    
    def set_next(self,next):
        self.next = next
    
    def get_next(self):
        return self.next
    
    def has_next(self):
        return self.next != None
    
class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
            
    def lengthOfList(self):
        count = 0
        loc = self.head
        while loc.next != None:
            loc = loc.next
            count+=1
            
    def insertElementAtEnd(self,data):
        loc = self.head
        while loc.next != None:
            loc = loc.next
        loc.next = Node(data)
    
    def deleteElement(self,data):
        loc = self.head
        prv = None
        while loc.next !=None:
            if(loc.data == data):
                prv.next = loc.next
                return
            else:
                prv = loc
                loc = loc.next

    def elementAtMiddleOfList(self):
        loc = self.head
        half = self.head
        while loc.next:
            loc = loc.next.next
            if(loc == None):
                break
            half = half.next
        print(half.data)
    
    def insertElementAtMiddle(self,data):
        print("here")
        loc = self.head
        half = self.head
        while loc:
            if(loc.next == None or loc.next.next == None):
                node = Node(data)
                local = half.next
                half.next = node
                half.next.next = local
                print("here")
                break
            loc = loc.next.next
            half = half.next
    
if __name__ == "__main__":
    llist = LinkedList()
    l = 4
    llist.head = Node(1)
    for i in range(2,l+2):
        llist.insertElementAtEnd(i)
    llist.lengthOfList()
    llist.printList()
    llist.insertElementAtMiddle(1111)
    llist.insertElementAtMiddle(11112)
    llist.insertElementAtMiddle(11113)
    llist.insertElementAtMiddle(11113)
    llist.printList()
    
    
    