def belt_count(dictionary):
    belts = list(dictionary.values())
    for belt in set(belts):
        num = belts.count(belt)
        print(f'There are {num} {belt} belts')


#def my_intro(dictionary):
#    for key, val in dictionary.items():
#        print(f'I am {key} and I am a {val} belt')

my_belts = {}

while True:
    my_name = input('enter a name:')
    my_belt = input('enter a belt colour:')
    my_belts[my_name] = my_belt
    another = input('add another? (Y/N)')
    if another=='Y':
        continue
    else:
        break

#my_intro(my_belts)
belt_count(my_belts)
