#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 26 14:47:26 2019
@author: majdoor
"""



class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prv = None

class CLL:
    
   def __init__(self):
        self.head = None
    
   def insertNode(self,data):
        head = self.head
        while(head.next!=self.head):
            head = head.next
        loc = Node(data)
        loc.next = self.head
        loc.prv = self.head.prv
        head.next = loc
        self.head.prv = loc
    
   def printNode(self):
        head= self.head
        while(head.next != self.head):
            print(head.data)
            head = head.next
   
   def printRvNode(self):
        head = self.head
        while(head.prv != self.head):
            print(head.data)
            head = head.prv
   
   def deleteNode(self,data):
        head = self.head
        if(head.data == data):
            self.head = head.next
            self.prv = head.prv
        else:
            while(head.next != self.head):
                if(head.data == data):
                    head.prv.next = head.next
                    head.next.prv = head.prv
                    break
                head = head.next
    
    
if __name__ == "__main__":
    node = Node(1)
    cll = CLL()
    node.next = node
    node.prv = node
    cll.head = node
    for i in range(0,10):
        cll.insertNode(i)
    cll.deleteNode(2)
    cll.printNode()
    
        
        