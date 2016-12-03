# python3

import sys


# LIFO - Last In First Out
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False


text = sys.stdin.read()
# text = "[](()"

opening_brackets_stack = []
stack = Stack()
errorPosition = -1
for i, next in enumerate(text):
    if next == '(' or next == '[' or next == '{':
        stack.push(Bracket(bracket_type=next, position=i + 1))
        pass
    if next == ')' or next == ']' or next == '}':
        if stack.isEmpty():
            errorPosition = i + 1
            break
        popped = stack.pop()
        if not (popped.Match(next)):
            errorPosition = i + 1
            break
        pass

if errorPosition > -1:
    print(errorPosition)
elif stack.size() > 0:
    print(stack.pop().position)
else:
    print("Success")
