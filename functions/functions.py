# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 10:22:56 2017

@author: Samar
"""
from functools import reduce
# import time


# a simple function to illustrate function syntax
def gcd(a, b):
    """
       find the greatest common divisor of two numbers
       triple quotes anywhere enable multiple line comments
       but as the first comment immediately following def or
       class they represent the docstring
    """
    while a != 0:
        a, b = b % a, a
    return b


print(gcd.__doc__)
print(gcd(2176, 3072))


# forward references not available
def foo():
    print('foo')
    bar()


foo()


def bar():
    print('bar')


# variable arguments
def add(*args):
    return reduce(lambda x, y: x + y, args)


print(add(1, 2, 3, 4, 5))


def add_varargs_kwargs(*args, **kwargs):
    sumOfNumbers = reduce(lambda x, y: x + y, args)
    for x, y in kwargs.items():
        if str(x) == 'mult':
            sumOfNumbers *= kwargs[x]
    return sumOfNumbers


print(add_varargs_kwargs(3, 4, 5, mult=5))


def add_varargs_kwargs_anyname(*blah, **tlah):
    sumOfNumbers = reduce(lambda x, y: x + y, blah)
    for x, y in tlah.items():
        if str(x) == 'mult':
            sumOfNumbers *= tlah[x]
    return sumOfNumbers


print(add_varargs_kwargs_anyname(3, 4, 5, mult=5))


# variable args have to follow regular args
def nadd(*args, a, b):
    return a + b


# order expected is default, regular, variable , then keyword args
# print(nadd(3, 4))
print(nadd(2, 3, 4))


def nadd_reg_var(a, b, *args):
    return (a + b) * reduce(lambda a, b: a + b, args)


print(nadd_reg_var(3, 4, 100, 200, 300, 400))
list4args = [100, 200, 300, 400]
print(nadd_reg_var(3, 4, *list4args))


def one_more_add(a, b, *args, **kwargs):
    return (a+b) * sum(args) * sum([kwargs[x] for x in kwargs])


print(one_more_add(2, 3, 1, 2, fn=2, sn=3, trdn=4, frthn=4))


def final_add_check_default(a, b=4, *args, **kwargs):
    print('a is', a, ' and b is ', b, ' and args is ', args)
    return (a+b) * sum(args) * sum([kwargs[x] for x in kwargs.keys()])


test_dict = {"fn": 3, "sn": 4}
ntest_dict = dict([('fn', 3), ('sn', 4)])
print('calling using keyword arguments')
print(final_add_check_default(2, 3, 5, fn=3, sn=4))
print('using a dictionary for keyword arguments')
print(final_add_check_default(2, 3, 5, **ntest_dict))


# decorators
def greet(name):
    return 'hello ' + name


def pdecorate(func):
    def func_wrapper(name):
        return '<p>{0}</p>'.format(func(name))
    return func_wrapper


greet_pdecorated = pdecorate(greet)
print(greet_pdecorated('whoever'))


@pdecorate
def greet_decorator(someone):
    return 'hello ' + someone


print(greet_decorator('someone'))


# using multiple decorators
def strong_decorate(func):
    def func_wrapper(name):
        return '<strong>{0}</strong>'.format(func(name))
    return func_wrapper


def div_decorate(func):
    def func_wrapper(name):
        return '<div>{0}</div>'.format(func(name))
    return func_wrapper


multi_decorated_greet = div_decorate(pdecorate(strong_decorate(greet)))
print(multi_decorated_greet('multi guy'))


@div_decorate
@pdecorate
@strong_decorate
def greet_multi_deocrators(someone):
    return 'hello ' + someone


print(greet_multi_deocrators('multi decorated guy'))


# generalizing the decorator so that it can be used inside classes also
def p_decorate_general(func):
    def func_wrapper(*args, **kwargs):
        return "<p>{0}</p>".format(func(*args, **kwargs))
    return func_wrapper


class Person():
    def __init__(self):
        self.name = "John"
        self.family = "Doe"

    @p_decorate_general
    def get_fullname(self):
        return self.name+" "+self.family


apers = Person()
print(apers.get_fullname())


@p_decorate_general
def greet_general(name):
    return 'hello genrally ' + name


print(greet_general('someone'))


# decorator with arguments
def tags(tag_name):
    def tags_decorator(func):
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        return func_wrapper
    return tags_decorator


@tags("p")
@tags('div')
@tags('strong')
def get_text(name):
    return "Hello "+name


print(get_text("John"))


# a decorator function to time execution of funcntions
def timing_function(some_function):
    """
    Outputs the time a function takes
    to execute.
    """
    import time

    def wrapper(*args):
        t1 = time.time()
        some_function(*args)
        t2 = time.time()
        return "Time it took to run the function: " + str((t2 - t1))
    return wrapper


@timing_function
def my_function():
    num_list = []
    for num in (range(0, 1000000)):
        num_list.append(num)
    print("\nSum of all the numbers: " + str((sum(num_list))))


print(my_function())


# decorators applied to a class to create curried functions
class curried():
    def __init__(self, func, *a):
        self.func = func
        self.args = a

    def __call__(self, *a):
        print('__call__ method called')
        args = self.args + a
        print(f'a was {a} and args now {args}')
        print('length of args ', len(args))
        if(len(args) < self.func.__code__.co_argcount):
            print('if block argcount ', self.func.__code__.co_argcount)
            print('if block args ', *args)
            return curried(self.func, *args)
        else:
            print('else block argcount ', self.func.__code__.co_argcount)
            print('else block args ', *args)
            return self.func(*args)


@curried
def add(a, b):
    return a + b


add1 = add(2)
print(add1(200))
print(add(2)(200))


@curried
def add_two_and_mult(a, b, c):
    return (a + b) * c


addtam = add_two_and_mult(3)
addtam_next = addtam(4)
addtam_final = addtam_next(5)
print(addtam_final)
print(add_two_and_mult(3)(4)(5))

class TestCC:   # Test Callable Class
    def __call__(self, *args):
        print('this func getting called')
        print(sum(args))


atcc = TestCC()
print(atcc(3, 4, 5))
print(atcc())
print(callable(atcc))


class NCC:    # Non Callable Class
    pass


ancc = NCC()
print(callable(ancc))
