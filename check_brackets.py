from stack import *
def check_brackets(statement):
    stack = Stack()
    for ch in statement:
        if ch in ('{', '[', '('):
            stack.push(ch)
        if ch in ('}', ']', ')'):
            last = stack.pop()
            if last is '{' and ch is '}':
                continue
            elif last is '[' and ch is ']':
                continue
            elif last is '(' and ch is ')':
                continue
            else:
                return False
    if stack.size > 0:
        return False
    else:
        return True

if __name__ == '__main__':
    sl = (
        "{(foo)(bar)}[hello](((this)is)a)test",
        "{(foo)(bar)}[hello](((this)is)atest",
        "{(foo)(bar)}[hello](((this)is)a)test))"
         )
    for s in sl:
        m = check_brackets(s)
        print("{}: {}".format(s,m)) 
