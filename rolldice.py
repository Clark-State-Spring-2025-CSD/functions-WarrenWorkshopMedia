#Write a function that takes as input number of dice and number of sides. The function will then return a list
#of randomly generated numbers in the proper count and range. For example if the the function is asked to generate
#3D6 or three sixed sided dice, then a potential output would be [2,2,6]
#This function cannot have any input or print statements.
#Write supporting code that will as the user for number of dice and sides, call the function, then report the results.
#The function should not be called if number of dice is zero or less and instead should report bad input to the user
#The function should not be called if number of sides is 1 or less and instead should report bad input to the user
#Sample outputs (your text does not have to match exactly)

# How many dice to roll? 3
# How many sides? 6
# Here are the results: [6, 1, 6]

# How many dice to roll? 0
# How many sides? 5
# Error: Sides must be greater than 1 and dice count greater than 0.

# How many dice to roll? 20
# How many sides? 20
# Here are the results: [18, 19, 6, 8, 13, 6, 6, 6, 18, 12, 20, 10, 14, 8, 14, 17, 12, 15, 20, 17]

#Random Number Generator and seed for testing
import random

random.seed()

 #Check the User input and generate the list of random dice rolls.
def Roll_Dice(Num_Dice, Num_Sides):
    #Display error message in case the user wants to be funny attempting to roll 0 dice or a 1 sided coin.
    if Num_Dice <= 0 or Num_Sides <= 1:
        raise ValueError("Sides must be greater than 1 and dice count greater than 0.")
    return [random.randint(1, Num_Sides) for _ in range(Num_Dice)]

#Try block to prompt user for input of the number of dice and sides of the dice.
try:
    Num_Dice = int(input("How many dice to roll?: "))
    Num_Sides = int(input("How many sides?: "))
#Call the roll the dice function and display the results for the user's input
    Dice_Results = Roll_Dice(Num_Dice, Num_Sides)
    print(f"Here are the results: {Dice_Results}")
#Display the error message if user's input was invalid...
except ValueError as Error:
    print(f"Invalid Input: {Error}")


