from cs50 import get_float


def main():

    cash = 0

    while cash <= 0:
        # prompt the user for the amount of cash  give them in change
        cash = get_float("How much change are you owed? ")

    # print how my cash is going to be given back to the player
    print("Change owed: ", cash)
    cents = round(cash * 100)

    # figure out how many quaters are needed
    quartersCount = int(cents / 25)
    # figure out the remainder left to disperse
    cents = cents % 25

    # figure out how many dimes are needed
    dimesCount = int(cents / 10)
    # figure out the remainder left to disperse
    cents = cents % 10
    
    # figure out how many nickels are needed
    nickelCount = int(cents / 5)
    # figure out the remainder left to disperse
    cents = cents % 5
    
    # figure out how many pennies are needed
    pennyCount = int(cents / 1)
    # figure out the remainder left to disperse
    cents = cents % 1
    
    # printf("%i\n",cents);
    print(quartersCount + dimesCount + nickelCount + pennyCount)
    

if __name__ == "__main__":
    main()