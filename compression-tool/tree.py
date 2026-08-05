from collections import Counter
import sys
import ast
import math
import argparse

class LeafNode:
    def __init__(self,el,wt):
        self.element = el
        self.weight = wt

    def node_value(self):
        return self.element
    
    def node_weight(self):
        return self.weight
    
    def is_leaf(self):
        return True
    
class InternalNode:
        def __init__(self,l,r,wt):
            self.left = l
            self.right = r
            self.weight = wt

        def left_node(self):
            return self.left
    
        def right_node(self):
            return self.right
    
        def node_weight(self):
            return self.weight
    
        def is_leaf(self):
            return False
    
class Tree:
    def __init__(self,wt,el=None,l=None,r=None):
        if(el!=None):
            self.root = LeafNode(el,wt)
        else:
            self.root = InternalNode(l,r,wt)

    def root_node(self):
        return self.root
    
    def node_weight(self):
        return self.root.weight
    
    def compare_to(self,t):
        if(self.root.node_weight()<t.node_weight()):
            return -1
        elif(self.root.node_weight()<t.node_weight()):
            return 0
        else:
            return 1

    def encode(self):
        codes = {}

        def traverse(node, current_code=""):
            if node is None:
                return

            if node.is_leaf():
                codes[node.node_value()] = current_code if current_code else "0"
                return

            traverse(node.left_node(), current_code + "0")
            traverse(node.right_node(), current_code + "1")

        traverse(self.root)
        return codes
    
    def decode(self,s):
        ans = ""
        curr = self.root
        n = len(s)
        for i in range(n):
            if s[i] == '0':
                curr = curr.left_node()
            else:
                curr = curr.right_node()

            # reached leaf node
            if curr.is_leaf():
                ans += curr.node_value()
                curr = self.root
        return ans + ' '
    

class Heap:
    def __init__(self,h,heap_size,max):
        self.heap = h
        self.n = heap_size
        self.max_size = max

    def heap_size(self):
        return self.n
    
    def is_leaf(self,pos):
        return ((self.n//2 <= pos) and (pos<self.n))
    
    def left_child(self,pos):
        return 2*pos+1
    
    def right_child(self,pos):
        return 2*pos+2
    
    def parent(self,pos):
        return (pos-1)//2
    
    def insert(self,key):
        if(self.n>self.max_size):
            print("Heap is full")
            return
        self.heap[self.n] = key
        self.n+=1
        self.shift_up(self.n-1)

    def remove_min(self):
        if(self.n<=0):
            print("Heap is empty")
            return
        if(self.n==1):
            self.n-=1
            return self.heap[self.n]
        self.n-=1
        self.swap(0,self.n)
        self.shift_down(0)
        return self.heap[self.n]


    def is_lesser_than(self,pos1,pos2):
        t1 = self.heap[pos1]
        t2 = self.heap[pos2]
        if(t1.node_weight()>t2.node_weight()):
            return False
        else:
            return True

    def shift_up(self,pos):
        if(pos<0 or pos>self.n):
            print("Invalid Heap position")
            return
        while(pos>0):
            parent = self.parent(pos)
            if(self.is_lesser_than(parent,pos)):
                return
            self.swap(pos,parent)
            pos = parent

    def swap(self,pos1,pos2):
        temp = self.heap[pos1]
        self.heap[pos1] = self.heap[pos2]
        self.heap[pos2] = temp

    def shift_down(self,pos):
        if(pos<0 or pos>self.n):
            print("Invalid Heap position")
            return
        while(not self.is_leaf(pos)):
            child = self.left_child(pos)
            if((child+1<self.n) and self.is_lesser_than(child+1,child)):
                child = child + 1
            if(not self.is_lesser_than(child,pos)):
                return
            self.swap(pos,child)
            pos = child

    def heapify(self):
        for i in range(self.parent((self.n)-1),-1,-1):
            self.shift_down(i)

    def traversal(self):
        for i in range(self.n):
            if(i==0 or int(math.floor(math.log(i+1)/math.log(2)))!=int(math.floor(math.log(i)/math.log(2)))):
                print()
            print(self.heap[i].node_weight(),end=" ")
        print()