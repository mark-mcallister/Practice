
while True:

    print("Welcome to the temperature converter!")

    unit = input("Is the temperature you have in farenheit or celsius? (F or C): ")

    if unit == "F":
        temperature_f = float(input("What is the temperature? (e.g. '45'): "))
        final_celsius = (temperature_f - 32) * 5 / 9
        print("Your temperature of",temperature_f,"farenheit is",final_celsius,"celsius")

    elif unit == "C":
        temperature_c = float(input("What is the temperature? (e.g. '20'): "))
        final_farenheit = (temperature_c * 9/5) + 32
        print("Your temperature of",temperature_c,"celsius is",final_farenheit,"farenheit")

    else:
        print("Sorry, I didn't understand that.")

    play_again = input ("Would you like to play again? (Y/N): ")

    if play_again == "N":
        exit()

    if play_again != "Y":
        break












