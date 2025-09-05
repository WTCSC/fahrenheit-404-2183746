print("Welcome to Fahrenheit 404.")
print("Would you like to convert Celsius to Fahrenheit?")
Celcius=input("yes or no? ")
if Celcius=="yes": 
    c_degree = float(input("what is the Celcius degree? "))
    converted_c_degree = ((c_degree * 1.8) + 32)
    print(f"your converted Fahrenheit degree is: {converted_c_degree}°F.")
elif Celcius=="no": 
    print("Would you like to convert Fahrenheit to Celcius?")
    Fahrenheit=input("yes or no? ")
    if Fahrenheit=="yes":
        f_degree = float(input("what is the Fahrenheit value? "))
        converted_f_degree = ((f_degree - 32) * 0.5555)
        print(f"your converted Celcius value is: {converted_f_degree}°C.")
print("Thank you for using Fahrenheit 404.")
