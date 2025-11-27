
import time
import random
import threading

def timed_input(prompt, timeout):
    user_input = [None]

    def get_input():
        user_input[0] = input(prompt)

    thread = threading.Thread(target=get_input)
    thread.daemon = True
    thread.start()

    thread.join(timeout)
    return user_input[0]


# Game Ideas
def close_fume_hood():
    print('\n🚨QUICK type \'close\' to close the fume hood🚨')
    answer = timed_input('\ntype here: ', 10)
    
    if answer == 'close':
        print('you saved the lab!! 😅')
        return True
    else:
        print('everyone is unconscious...')
        return False
    
def learn_crash():
    print('\nLearn is crashing and the assignment is due!! 💻')
    print('\ntype \'submit\' as quick as you can!!')
    answer = timed_input('\ntype here: ', 10)
    
    if answer == 'submit':
        print('just in time, 55%!! 😅')
        return True
    else:
        print('another failed assignment...')
        return False

def meniscus_dilemma():
    print('\nthe meniscus in the beaker is too high, what do you do? 🧪')
    print('\na) add more \nb) use your mouth and blow it out \nc) remove a drop with a pipette')
    answer = timed_input('\ntype here: ', 10)
    
    if answer == 'c':
        print('perfect!')
        return True
    else:
        print('have you done your safety? 🤔')
        return False
    
def reactor_leak():
    print('\nQUICK type the code so the reactor is fixed! 🌋')
    print('\nA57JP')
    answer = timed_input('\ninput code: ', 10)
    
    if answer == 'A57JP':
        print('thank goodness you stopped the leak')
        return True
    else:
        print('\nWere those fish green before... 🐠')
        return False
    
#needed to run
MINIGAMES = [close_fume_hood, learn_crash, meniscus_dilemma, reactor_leak]

def main():
    score = 0
    lives = 3

    print("🎉 Welcome to Dumb Ways to Waterloo — Python Edition! 🎉")
    print("Survive as many minigames as possible.\n")

    while lives > 0:
        game = random.choice(MINIGAMES)
        result = game()

        if result:
            score += 1
            print(f"⭐ Score = {score}")
        else:
            lives -= 1
            print(f"💔 Lives left: {lives}")

        time.sleep(1)

    print("\n☠️ GAME OVER! Final score:", score)
