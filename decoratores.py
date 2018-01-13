def cough_dec(func):

    def func_wrapper():
        print('*cough*')
        func()
        print('*cough*')
    return func_wrapper

@cough_dec
def question():
    print('can you give me a discont on that?')

@cough_dec
def answer():
    print("it's only 50p you cheapstake")

question()
answer()
