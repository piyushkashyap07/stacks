from sys import stdin


def isBalanced(expression) :
	#Your code goes here
    list=[]
    for i in expression:
        if i == ")":
            if len(list) > 0:
            	ele = list.pop()
            else:
                return False
            if ele == ")":
                return False
        else:
            if i == "(":
                list.append(i)
    if len(list) == 0:
    	return True
    else:
        return False
            
        
    
























	




#main
expression = stdin.readline().strip()

if isBalanced(expression) :
	print("true")

else :
	print("false")
