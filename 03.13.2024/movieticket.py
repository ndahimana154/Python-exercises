def movieTicketer(age):
    if(age<0):
        return("Invalid Age")
    if(age<12):
        return("Free Ticket")
    if(age<=18):
        return("500RWF Ticket")
    if(age>18):
        return("8000RWF Ticket")
    
personAge=int(input("Enter the age: "));

print(movieTicketer(personAge))