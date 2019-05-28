#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 26 03:37:49 2019
@author: majdoor
"""

class Node:
   def __init__( self, data):
        self.data = data
        self.prv = None
        self.next = None

class DoublyLinkedList:
   def __init__(self):
        self.head = None
    
   def insertNode(self,data):
        loc = self.head
        prv = self.head
        while loc.next != None:
            loc = loc.next
        node = Node(data)
        node.prv = loc
        loc.next = node
        
   def deleteNode(self,data):
        loc = self.head
        while loc.next !=None:
            if(loc.data == data):
                loc.next.prv = loc.prv
                loc.prv.next = loc.next
                break
            loc = loc.next
    
   def printF2B(self):
        loc = self.head
        while loc.next != None:
            print(loc.data)
            loc = loc.next
            
   def printB2F(self):
       loc = self.head
       while loc.next != None:
           loc = loc.next
       while loc !=None:
           print(loc.data)
           loc = loc.prv
           
if __name__ == "__main__":
    dlist = DoublyLinkedList()
    node = Node(1)
    dlist.head = node
    for i in range(2,11):
        dlist.insertNode(i)
    dlist.deleteNode(6)
    print("-------------")
    dlist.printF2B()
    dlist.printB2F()
        
    
        