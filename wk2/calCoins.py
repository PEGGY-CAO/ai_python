# This program is used to ask the user to enter a number of quarters, dimes, nickels and pennies
# Then outputs the monetary value

def askFor(coinUnit):
    coinCounts = int(input("How many " + coinUnit + " do you have?"))
    if coinUnit == "quarters":
        return 25 * coinCounts
    elif coinUnit == "dimes":
        return 10 * coinCounts
    elif coinUnit == "nickels":
        return 5 * coinCounts
    else:
        return coinCounts


sum = 0
sum += askFor("quarters")
sum += askFor("dimes")
sum += askFor("nickels")
sum += askFor("pennies")
print("Total monetary value is: $" + str(sum / 100))
