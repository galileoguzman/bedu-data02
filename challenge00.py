import random


number = input('Give me a number: ') # 100


counter = 1
list_random = []

while counter <= int(number):
    choice = random.randint(1, 2) # Return 1 or 2

    index = random.randint(1, int(number)) # Return between 1 y number - 100

    value = str(choice * index)

    list_random.append(value)
    counter = counter + 1


print(list_random)
