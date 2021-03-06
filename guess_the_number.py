import random

correct = 'you guessed correctly!'
too_low = 'too low'
too_high = 'too high'


def configure_range():
    '''Set the high and low values for the random number'''
    return 1, 10


def generate_secret(low, high):
    '''Generate a secret number for the user to guess'''
    return random.randint(low, high)

 # count the number of guesses

def get_guess():
    '''get user's guess'''
    bad = True
    while bad:
        try:
            guess = int(input('Guess the secret number? '))
            bad = False
            return guess
        except ValueError:
            print('Must input an integer. Please try again.')


def check_guess(guess, secret):
    '''compare guess and secret, return string describing result of comparison'''
    if guess == secret:
        return correct
    if guess < secret:
        return too_low
    if guess > secret:
        return too_high


def main():
    counter = 0
    (low, high) = configure_range()
    secret = generate_secret(low, high)
    
    while True:
        counter = counter + 1
        guess = get_guess()
        result = check_guess(guess, secret)
        print(result)
        print(f'You have guessed: {counter}')
        if result == correct:
            break


if __name__ == '__main__':
    main()
