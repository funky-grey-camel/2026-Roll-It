
# functions go here

def yes_no(question):

    #Checks user response to a question is yes / no (y/n), returns 'yes' or 'no'

    while True:

        response = input(question).lower()

        # check the user says yes / no / y / n
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes / no")


def instructions():
    print("""
    
*** Roll It 13 Instructions ***

- Roll the dice
- Try to beat the computer

Good luck
    
    """)

# Main routine

# testing loop...

want_instructions = yes_no("Do you want the instructions? ").lower()

if want_instructions == "yes":
    instructions()

