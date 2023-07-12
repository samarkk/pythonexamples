# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 17:17:59 2017

@author: Samar
"""
import sys
import logging
import traceback


def safe_float(obj):
    try:
        retval = float(obj)
    except ValueError:
        retval = 'could not convert non-number to float'
    return retval


print(safe_float('23.344'))
print(safe_float('23.3.44'))


# multiple exception blocks
def safe_float(obj):
    try:
        retval = float(obj)
    except ValueError:
        retval = 'could not convert non-number to float'
    except TypeError:
        retval = 'object type cannot be converted to float'
    return retval


print(safe_float(3.14234))
print(safe_float('why not onlnie numeric conversion'))


# except statement with multiple exceptions
def safe_float(obj):
    try:
        retval = float(obj)
    except (ValueError, TypeError) as e:
        # one can also issue except(ValueError, TypeError) as e:
        # and prnt e, e.args to see the error that was caught and the args
        print(e, e.args)
        retval = 'argument must be a number or numeric string'
    return retval


print(safe_float('23.344'))
print(safe_float('23.3.44'))


# try, except, finally
def foo(x):
    return 1 / x


def bar(x):
    try:
        return foo(x)
    # except ZeroDivisionError, message and ZeroDivisionError as message
    # the first one will work only with python2
    # 2nd one with both python 2 and 3
    except ZeroDivisionError as message:
        print('can\'t divide by zero ', message)

    finally:
        print('this will always get printed')


# print( bar(3))
print(bar(0))


# we have a try except else finally structure also available
# where the else block represents the no exceptions raised suite
# we can place additional functionalities there
try:
    safe_float(3.12)
except Exception as e:
    # we could define multiple exception statements
    print(e)
else:
    print('we did good')
finally:
    print('wow')


# creating user defined exceptions
class InvalidWithdrawal(Exception):
    def __init__(self, balance, amount):
        super().__init__("account doesn't have ${}".format(amount))
        self.amount = amount
        self.balance = balance

    def overage(self):
        return self.amount - self.balance


def withdraw(balance, amount):
    try:
        if balance >= amount:
            print('New balance is {}'.format(balance - amount))
        if balance < amount:
            raise InvalidWithdrawal(balance, amount)
    except InvalidWithdrawal as e:
        # print('exc info \n', sys.exc_info())
        # sys.exc_info() returns a 3 tuple - exception class,
        # exception value and a traceback object
        print('Your balance is {} you cannot withdraw {}'
              ''.format(e.balance, e.amount))


print(withdraw(100, 200))
print(withdraw(200, 300))


# exception chaining - exceptions inside exception blocks
try:
    v = {}['a']
except Exception as e:
    print(e, type(e), e.args)
    raise ValueError('failed') from e


# using logging ans sys.exc_info to get more info about exceptions
def get_number():
    return int('non_number')


try:
    get_number()
except Exception as e:
    print(sys.exc_info())
    logging.exception('we have some error here')

x = 300
errs_tb = []
errs_rec = []
for sm_nmbr in [3, 0, 'err', 23.7]:
    try:
        print(x / sm_nmbr)
    except ValueError as ve:
        print('we are here in the value error block')
        print(ve)
    except(TypeError, ZeroDivisionError) as generic_err:
        print('we are here in the type error and zde block')
        errs_rec.append(generic_err)
        errs_tb.append(sys.exc_info()[2])

print(errs_tb)
print(errs_rec)
print(traceback.format_tb(errs_tb[0]))
print(traceback.format_tb(errs_tb[1]))
