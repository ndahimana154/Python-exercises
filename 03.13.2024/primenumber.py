def findPrime(num):
    i=2
    isPrime = True
    while(i<num):
        if(num%i==0):
            isPrime = False
            break;
        i+=1
    if(isPrime== True):
        return (f"{num} is Prime number: ")
    return(f"{num} is not Prime number: ")

number = int(input("Enter the number: "))
print(findPrime(number))