from collections import deque
class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

s=Stack()
s.push(1)
s.push(2)
print(s.size())
s.push(3)
s.push(4)
print(s.peek())
s.pop()
print(s.peek())
print("************************")

def reverse_string(s):
    stack=Stack()
    for ch in s:
        stack.push(ch)
    rstr=''
    while (stack.size()!=0):
        rstr+=stack.pop()
    return rstr

if __name__ == '__main__':
    print(reverse_string("Parth Salke is great"))
    print(reverse_string("Racecar"))

print("************************")
def is_match(ch1, ch2):
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return match_dict[ch1] == ch2


def is_balanced(s):
    stack = Stack()
    for ch in s:
        if ch=='(' or ch=='{' or ch == '[':
            stack.push(ch)
        if ch==')' or ch=='}' or ch == ']':
            if stack.size()==0:
                return False
            if not is_match(ch,stack.pop()):
                return False

    return stack.size()==0


if __name__ == '__main__':
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("((a+g))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))

