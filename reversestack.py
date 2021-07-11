from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)


def reverseStack(inputStack, extraStack) :
	#Your code goes here
    if len(inputStack) == 0:
        return ;
    lastElement = inputStack.pop()
    
    reverseStack(inputStack, extraStack);
        
    while not isEmpty(inputStack):
        top = inputStack.pop()
        
        extraStack.append(top)
    inputStack.append(lastElement)
    
    while not isEmpty(extraStack):
        top = extraStack.pop()
        inputStack.append(top)
        
    
    
        






























'''-------------- Utility Functions --------------'''

#Takes a list as a stack and returns whether the stack is empty or not
def isEmpty(stack) :
    return len(stack) == 0


#Taking input using fast I/o method
def takeInput() :
	size = int(stdin.readline().strip())
	inputStack = list()

	if size == 0 :
		return inputStack


	values = list(map(int, stdin.readline().strip().split(" ")))
	inputStack = values

	return inputStack


# Main
inputStack = takeInput()
emptyStack = list()

reverseStack(inputStack, emptyStack)

while not isEmpty(inputStack) :
	print(inputStack.pop(), end = " ")