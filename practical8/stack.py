def createStack():
    stack = []
    return stack

def isEmpty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)
    print("pushed item is  " + item)

def pop(stack):
    if (isEmpty(stack)):
        return "stack is empty"
    return stack.pop()

stack = createStack()
push(stack, str(10))
push(stack, str(20))
push(stack, str(30))
push(stack, str(40))
print("popped item: " + pop(stack))
print("stack after popping an element: " + str(stack))