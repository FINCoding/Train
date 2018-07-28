# def shout(word='да'):
#     return word.capitalize()+"!"

def getTalk(type="shout"):
    def shout(word='да'):
        return word.capitalize()+"!"

    def whisper(word="нет"):
        return word.lower()+"..."

    if type == 'shout':
        return shout
    else:
        return whisper

# talk = getTalk()
# print(talk())

def my_shiny_new_decorator(a_function_to_decorate):
    def the_wrapper_around_the_original_function():
        print('Starts code')
        a_function_to_decorate()
        print("finish's code")
    return the_wrapper_around_the_original_function

@my_shiny_new_decorator
def a_stand_alone_function():
    print("i'm alone function")

# a_stand_alone_function()

# a_stand_alone_function_decorated = my_shiny_new_decorator(a_stand_alone_function)
# a_stand_alone_function_decorated()
a_stand_alone_function()
a_stand_alone_function()
