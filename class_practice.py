
temp = float(input("What is the temperature in Fahrenheit? "))

comfort_level = "cold"

if temp > 70:
    if temp > 90:
        comfort_level = "hot"
    else:
        comfort_level = "comfortable"

print(comfort_level)