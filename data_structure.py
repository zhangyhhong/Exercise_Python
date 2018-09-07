# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 13:43:45 2018

@author: zyh
用Python实现基本的数据结构：栈，队列，链表
"""
#栈
class Stack:
    def __init__(self):
        self.items = []
        
    def push(self,item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
        
    def clear(self):
        del self.items[:]
    
    def size(self):
        return len(self.items)
    
    def isempty(self):
        return self.size() == 0
    
def testStack():
    print('test Stack')
    s = Stack()
    print('Empty? %s, Size: %s' %(s.isempty(),s.size()))
    s.push(1)
    s.push(2)
    print('Empty? %s, Size: %s' %(s.isempty(),s.size()))  
    print('pop one element:',s.pop())
    print( 'size:',s.size())
    

#队列
class Queue:
    def __init__(self):
        self.items = []
        
    def enqueue(self,item):
        self.items.append(item)
        
    def dequeue(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)
    
    def isempty(self):
        return self.size() == 0

def testQueue():
    print('\ntest Queue')
    s = Queue()
    print('Empty? %s, Size: %s' %(s.isempty(),s.size()))
    s.enqueue(1)
    s.enqueue(2)
    print('Empty? %s, Size: %s' %(s.isempty(),s.size()))  
    print('one element dequeue:',s.dequeue())
    print( 'size:',s.size())    

#单链表
class Node:
    def __init__(self,initdata):
        self._data = initdata
        self._next = None
        
    def getData(self):
        return self._data
    
    def getNext(self):
        return self._next
    
    def setData(self,newdata):
        self._data = newdata
        
    def setNext(self,newnext):
        self._next = newnext
        
class SinCycLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.head.setNext(self.head) #初始化指向自己的头结点
        
    def add(self,item):
        tmp = Node(item)
        tmp.setNext(self.head.getNext())
        self.head.setNext(tmp)
        
    def remove(self,item):   #移除值为item的节点
        pre = self.head
        while pre.getNext() != self.head:   #是否到头
            cur = pre.getNext()
            if cur.getData() == item:
                pre.setNext(cur.getNext())
            pre = pre.getNext()
            
    def search(self,item):
        cur = self.head.getNext()
        while cur != self.head:
            if cur.getData() == item:
                return True
            cur = cur.getNext()
        return False
    
    def isempty(self):
        return self.head.getNext() == self.head
    
    def size(self):
        count = 0
        cur = self.head.getNext()
        while cur != self.head:
            count += 1
            cur = cur.getNext()
        return count

def testLinkedList():
    print('\ntest LinkedList')
    s = SinCycLinkedList()
    print('Empty? %s, Size: %s' %(s.isempty(),s.size()))
    s.add(1)
    s.add(2)
    print('Empty? %s, Size: %s' %(s.isempty(),s.size()))  
    print('1 is in LinkedList?',s.search(1))
    s.remove(1)
    print('After remove 1,1 is in LinkedList?',s.search(1))
    print( 'size:',s.size())
    
if __name__ =='__main__':
    testStack()
    testLinkedList()
    testQueue()
    
            
            
            
            
         
