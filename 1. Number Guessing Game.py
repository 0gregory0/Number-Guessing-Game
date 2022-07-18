import random as ran

#Defining the Function
def guessing_game():
    #Generating a random number
    random_number = ran.randint(0, 100)

    #While Loop
    while True:
        #Error handling
        try:
            #Prompt User for Input
            guess = int(input('I\'m thinking of a number between 0 and 100. Can you guess it? '))

            if guess == random_number:
                print('Just right. I was thinking of {} and you guessed {}.'.format(random_number, guess))
                break

            elif guess > random_number:
                print('Your guess of {} is too high'.format(guess))

            elif guess < random_number:
                print('Tour guess of {} is too low'.format(guess))
        
        except:
            print('Invalid input. Enter a positive integer in figures.')
guessing_game()
