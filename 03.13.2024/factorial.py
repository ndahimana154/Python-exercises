def findFactorial(num):
    factorial = 1;
    i=1;
    while(i<=num):
        factorial *=i
        i+=1
    return factorial

a=int(input("Enter the number: "))
print(findFactorial(a))