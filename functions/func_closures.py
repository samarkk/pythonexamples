# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 14:49:05 2017

@author: Samar
"""


import time

'''
In Python, a closure is a function that "closes over" variables from its enclosing scop
preserving those variables even after the enclosing scope has finished executing
A closure can access and manipulate variables that are not in its local scope
Closures are commonly used to encapsulate behavior and state within functions, creating self-contained units of code
'''

def closure_example(start_at=0):
    # count defined outside the inside function is a free variable
    count = [start_at]

    # if references are made from an inner function to an
    # object defined in any outer scope, but not in the global scope
    # the inner function is known as a closure
    def incr():
        #  A closure combines its own scope with that of an outer one
        #  the lexical environment within which it was created
        count[0] += 1
        return count
    return incr


counter = closure_example(10)
for x in range(20):
    print(counter())


# closures as decorators to extend or modify the behaviour of functions without altering the code directly
def add_logging(func):
    def wrapper(*args, **kwargs):


        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned: {result}")
        return result
    return wrapper

@add_logging
def multiply(x, y):
    return x * y

result = multiply(3, 4)
print("Result:", result)


def logged(when):
    def log(f, *args, **kwargs):
        print('''Called:
            function: {}
            args:  {}
            kwargs: {}
            '''.format(f, args, kwargs)
              )

# both pre_logged and post_logged wrapper functions
# form closures over the free variable - in this case function
# log defined outside their scope

    def pre_logged(f):
        def wrapper(*args, **kwargs):
            print('pre wrapper')
            log(f, *args, **kwargs)
            return f(*args, **kwargs)
        return wrapper

    def post_logged(f):
        def wrapper(*args, **kwargs):
            print('post wrapper')
            now = time.time()
            time.sleep(1)
            try:
                return f(*args, **kwargs)
            finally:
                print("time delta {}".format((time.time()-now)))
                log(f, *args, **kwargs)
        return wrapper

    try:
        print('now inside try block')
        return {"pre": pre_logged, "post": post_logged}[when]
    except KeyError as e:
        raise ValueError(e, 'must be "pre" or "post"')


@logged("pre")
@logged("post")
def hello(name):
    print("Hello ,", name)


# q - what is the function getting decorated
# ans - hello
# q - does the decorator take arguments
# a - yes, it takes when for which two choices are provided - pre, post
#     as arguments
# q - which methods are the function decorators
# a - pre_logged and post_logged, they wrap the function and
#     return the wrapper
# q - which methods are the closures inside logged decorator
# a - pre_logged and post_logged are the two closures
# q - what is the common utility function in the decorator
# a - it is the inside function log which is used by both
#     pre and post logged


hello("whoever")
