def findFibonnaci(num):
    fiblist = []
    a=0
    b=1
    i=0
    while(i<=num):
        fiblist.append(a)
        saver=a
        a=b
        b=b+a
        i+=1
    return fiblist


number=int(input("Enter the fibonnaci limit: "))
print(findFibonnaci(number))