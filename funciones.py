def clean_string(text):
    return text.strip().capitalize()


total = int(input('How many guys you want me to say hello? '))
counter = 1
people = []

while counter <= total:
    name = input(f'Tell me the name number {counter}: ') # f-string
    people.append(name)
    counter = counter + 1

extras = ['    Galileo', 'Mari    ']
people.extend(extras)

people = list(map(clean_string, people))
print(people)
