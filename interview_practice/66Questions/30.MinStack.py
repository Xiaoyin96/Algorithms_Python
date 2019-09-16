#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
'''
定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。在该栈中，调用min、push、pop的时间复杂度都是O(1)
利用辅助栈, stack: 先进后出
'''
class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = [] # 辅助栈

    def push(self,num):
        self.stack.append(num)
        if not self.minstack or num < self.min():
            self.minstack.append(num)
        else:
            self.minstack.append(self.minstack[-1])

    def pop(self):
        if not self.stack or not self.minstack:
            return None
        self.minstack.pop() # minstack updated
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def min(self):
        if self.minstack:
            return self.minstack[-1]

s = MinStack()
s.push(1)
s.push(2)
s.push(3)
s.push(-1)
s.push(-2)
s.push(-4)

s.pop()
s.min() # -2

s.pop()
s.min() # -1



