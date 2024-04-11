def greetings(country):
    if(country == "Rwanda"):
        return (f"Mwaramutse {country}")
    if(country == "France"):
        return(f"Bonjour {country}")
    return (f"Invalid Country")

countryName = input("Enter the Country name: ")

print(greetings(countryName))