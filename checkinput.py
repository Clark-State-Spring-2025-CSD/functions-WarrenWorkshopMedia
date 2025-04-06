#Write a function that takes two parameters: a prompt message and an error message.
#The function will prompt the user with the passed in prompt to enter an integer
#If the text entered cannot be cast to an int, display the error message.
#The function will continue to prompt the user to enter an integer until a proper integer is entered.
#The most direct way of doing this would be using a try block, which has not been covered yet. You will need to research this.
#Write supporting code to call the function, and then display the number that was entered.


#The function to check the user's input is valid or not.
def CheckUserInput(Prompt, ErrorMessage):
    #While loop so they keep the program running until they enter a number!
    while True:
        UserInput = input(Prompt)
        #The try-block will return the input except if the user wants to try and type letters...
        try:
            return int(UserInput)
        except ValueError:
            print(ErrorMessage)

#Display either the number entered or the error message for the inputs.
Number = CheckUserInput("Enter a number: ", "Invalid input. Please enter a valid integer.")
print(f"You entered: {Number}")