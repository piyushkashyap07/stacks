def stockSpan(price,n):
    s=[]
    s.append(1)

    for i in range(1,len(price)):
        k=1
        j=i-1
        while j>=0:
            if price[j]<price[i]:
                k=k+1
                j=j-1
            else:
                break
        s.append(k)
    return s
#### Implement Your Code Here

n=int(input())
p = [int(ele) for ele in input().split()]
if len(p)>0:
    price=p
    spans = stockSpan(price,n)
    for ele in spans:
        print(ele,end= ' ')