"""
Description:
Author:qxy
Date: 2019-06-15 13:05
File: 00225_implement_stack_using_queues 
"""

"""
使用队列实现栈的下列操作：

push(x) -- 元素 x 入栈
pop() -- 移除栈顶元素
top() -- 获取栈顶元素
empty() -- 返回栈是否为空
注意:

你只能使用队列的基本操作-- 也就是 push to back, peek/pop from front, size, 和 is empty 这些操作是合法的。
你所使用的语言也许不支持队列。 你可以使用 list 或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
你可以假设所有操作都是有效的（例如, 对一个空的栈不会调用 pop 或者 top 操作）。

"""


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.stack.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.stack.pop(-1)

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.stack[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not len(self.stack)


"""
执行用时 :40 ms, 在所有Python3提交中击败了97.47%的用户
内存消耗 :13 MB, 在所有Python3提交中击败了95.59%的用户
"""