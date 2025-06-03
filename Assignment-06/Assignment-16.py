

def log_function_call(func):
    def wrapper():
        print("The function is being printing.")
        return func()
    return wrapper

@log_function_call
def say_hello():
    print("Hello, zain")

say_hello()