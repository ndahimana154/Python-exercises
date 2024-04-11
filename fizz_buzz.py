def fizz_buzz(number):
    if(number%3 == 0 and number%5==0):
        return "FizzBuzz"
    if(number %3 ==0):
        return "Fizz"
    if(number %5==0):
        return "Buzz"
    return"No Bizz"


print(fizz_buzz(5))