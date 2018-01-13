#def greet(name = 'Reddy',time = 'afternoon'):
    #print(f'Good {time} {name}, hope you are well')

#name = input('enter your name:')
#time = input('enter the time of day:')

#greet(name='vijeet')

def area(radius):
    return 3.142 * radius * radius

def vol(area,length):
    print(area*length)

radius = int(input('enter a radius:'))
length = int(input('enter a length:'))

#area_calc = area(radius)

vol(area(radius), length)
