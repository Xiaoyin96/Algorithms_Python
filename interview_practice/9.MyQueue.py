#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''

'''
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
list: 先进后出，queue: 先进先出
'''
class MyQueue():
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        self.stack1.append(node)

    def pop(self):
        if len(self.stack2) == 0 and len(self.stack1) == 0:
            return
        elif len(self.stack2) == 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

q = MyQueue()
q.push(1)
q.push(2)
q.push(3)
#%%
print(q.pop())

#%%
q.push(4)
q.push(5)
#%%
print(q.pop())