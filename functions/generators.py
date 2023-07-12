def csv_reader(file_name):
    file = open(file_name)
    result = file.read().split('\n')
    return result

def infinite_sequence():
    i = 0
    while True:
        yield i
        i += 1
for i in infinite_sequence():
    print(i)

def isprime(n):
    if n == 0 or n == 1:
        return False
    if n == 2:
        return True
    return not any(n % x == 0 for x in range(2, int(n ** 0.5) + 1))

def prime_generator(n):
    i = 2
    counter = 0
    while(counter < n):
        if isprime(i):
            counter += 1
            yield i
        i += 1

for i in prime_generator(200):
    print(i)


import sys
nums_squared_lc = [i ** 2 for i in range(10000)]
sys.getsizeof(nums_squared_lc)

nums_squared_gc = (i ** 2 for i in range(10000))
print(sys.getsizeof(nums_squared_gc))

def is_palindrome(num):
    if num < 10:
        return False
    return str(num) == ''.join(i for i in reversed(str(num)))

def infinite_palindromes():
    num = 0
    while True:
        if is_palindrome(num):
            print('Found palindrome {}'.format(num))
            i = (yield num)
            if i is not None:
                num = i
        num += 1

pal_gen = infinite_palindromes()
for i in pal_gen:
    digits = len(str(i))
    pal_gen.send(5 ** digits)

pal_gen = infinite_palindromes()
for i in pal_gen:
    print(i)
    digits = len(str(i))
    if digits == 5:
        pal_gen.throw(ValueError("We don't like large palindromes"))
    pal_gen.send(10 ** (digits))

pal_gen = infinite_palindromes()
for i in pal_gen:
    print(i)
    digits = len(str(i))
    if digits == 5:
        pal_gen.close()
    pal_gen.send(10 ** (digits))

file_name = 'D:/dloads/techcrunch.csv'
lines = (line for line in open(file_name))
# get the columns from the first line
list_line = (s.rstrip().split(',') for s in lines)
cols = next(list_line)
# zip the columns with every line and convert the zipped structure into a dictionary
company_dicts = (dict( zip(cols, data))for data in list_line)
# a new generator expression
# if  its series a funding cast the raised amount to int
funding = ( int(company_dict['raisedAmt']) for company_dict in company_dicts if company_dict['round'] == 'a')
# sum it
total_series_a = sum(funding)
print(f'Total series A fundraising ${total_series_a}')
