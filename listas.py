
def multiplicar(numero):
    return numero * 2

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
new_numbers = []

for n in numbers:
    new_numbers.append(multiplicar(n))

print(new_numbers)
