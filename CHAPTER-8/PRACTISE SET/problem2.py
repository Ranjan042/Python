celcius=int(input("Enter temperature in celcius"))

def converter(celcius):
    fahrenheit=(celcius*(9/5)) +32
    return fahrenheit

print("Degree in celicus: "+ str(converter(celcius)))