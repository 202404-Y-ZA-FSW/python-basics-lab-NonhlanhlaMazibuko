import random

guess = float(input('Enter you guessed number between 1 and 100:'))

rand = random.randint(1, 100)
count = 0
while guess != rand:
    count += 1
    if guess < rand:
        print(f'guess is too low, you are on {count} attempts')
    
    elif guess > rand:
        print(f'guess is too high, you are on {count} attempts')  
    guess = float(input('Enter you guessed number between 1 and 100:'))

print('guess is correct')
print(f'guessed after {count} attempts')
    
