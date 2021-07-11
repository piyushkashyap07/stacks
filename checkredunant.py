from sys import stdin

def checkRedundantBrackets(expression) :
    if expression[0]=='(' and expression[2]==')':
        return True
    st=[]
    for c in expression:
        if c!=')':
            st.append(c)
        else:
            if st[-1]=='(':
                return True
            while st[-1]!='(':
                st.pop()
            st.pop()

    return False        


#main
expression = stdin.readline().strip()

if checkRedundantBrackets(expression) :
	print("true")

else :
	print("false")