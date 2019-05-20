import random

rand_value = random.randint(1, 1000)
chance = 1

while chance <= 10:
    try:
        prompt = 'Chance : {}\nenter the value :'.format(chance)
        user_value = int(input(prompt))
    except ValueError as err:
        print(err, '\n')
        continue

    if user_value == rand_value:
        print('you won')
        break
    elif user_value > rand_value:
        print(user_value, ': greater')
    else:
        print(user_value, ': lesser')

    chance += 1
    print()
else:
    print('you failed to guess')
