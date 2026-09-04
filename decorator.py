def decorator(func):
    def wrapper():
        print("runninf fuction: ", func.__name__)
        func()
    return wrapper
@decorator
def hello():
    print("Hello world")
hello()
    
@decorator
def ayush():
    print("Hello ayush")
ayush()