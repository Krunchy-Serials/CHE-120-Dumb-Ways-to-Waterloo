import random 
#KK This minigame randomizes answers to a question. Each time the user plays the minigame, 2 wrong answers and 1 correct answer will be displayed.

#KK list of wrong choices that can be displayed
wrong_choices = ['scream as loud as you can', 'climb out of the emergency trap door', 'cry', 'call your mom','summon a goose to help you','jump', 'pry open the door','use mass balances', 'make a titration out of your tears', 'wipe your tears with your 102 midterm', 'meditate', 'write a lab report on your experimental findings']

#KK list of right choices
right_choices = ['study for your linear algebra exam! Theres no time to lose!', 'press the emergency button', 'Apply Le Chatelier’s Principle to reduce stress', 'wait for help to arrive', 'hack into the elevator mainframe (launch jupyter notebook)']


def getrandomword(choiceList):
    Index = random.randint(0, len(choiceList) - 1)
    return choiceList[Index]

def escape_dana_porter_elevator(time_limit=None):
    
    print('quick! You are stuck in the Dana Porter Elevator! Choose your escape wisely \n')
    
    #KK Randomizes one string from list of right choices
    correct = random.choice(right_choices)
    #KK Randomizes 2 strings from list of wrong choices
    incorrect = random.sample(wrong_choices, 2)

    #KK Creates a list from the 2 incorrect choices and one correct and shuffles the order
    options = [correct] + incorrect
    random.shuffle(options)

    #KK Numbers the options 1-3
    for i, choice in enumerate(options, start=1):
        print( str(i) + ". " + str(choice))

    #KK Prompts user to add input
    while True:  
        answer = input('\n please pick your answer (1-3):')

        #KK Validates that players input was valid and prompts them to answer again until its valid.
        if not answer.isdigit() or int(answer) not in [1,2,3]:
            print('looks like this will take a while! Choose a valid input to escape the elevator!')
            continue
        
        break

    #KK changes input string to integer
    validated_input = int(answer)
    selected = options[validated_input - 1]

    #KK checks if the players answer was in the list of right choices
    if selected in right_choices:
        print('Congrats! You have escaped the Dana Porter Elevator')
        return True
    else:
        print('FAIL! You are forever stuck in the elevator')
        return False
    

if __name__ == "__main__":
    escape_dana_porter_elevator()

