x = int(input("Enter a number of repetitions: "))

def repeat_hello(num_repetitions):
    def decorator(func):
        def wrapper():
            for _ in range(num_repetitions):
                func()
        return wrapper
    return decorator

@repeat_hello(x)
def hello():
    print('Hello')

hello()


