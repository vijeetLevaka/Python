my_name = 'Reddy'

def print_name():
    global my_name
    my_name = "Vijeet"
    print('the name inside the function is', my_name)


print_name()
print("outside the function the name is", my_name)
