import datetime
from math import pi
from random import seed, shuffle, randint
from math import sqrt

# variables and keywords
abool = True
anint = 10
afloat = 30.4
amn_scin = 1e6
pi_scin = 31472e-4
astring = 'whatever'
_underscore = 10
print(abool, anint, afloat, amn_scin, pi_scin, astring, _underscore)

# numeric operators
print(anint + 2)
print(anint - 2)
print(anint * 2)
print(anint / 2)
'''
/ represents division 
// represents result cast to int using the floor
anint // 3 = 3
anint // 4 = 2
'''
print(anint // 3)
print(anint // 4)

# c, jaya style assignment and shortcut operators are supported
anint += 10 # 20
print(anint)
anint -= 10 # 10
print(anint)
anint *= 10 # 100
print(anint)
anint /= 10 # 10.0
print(anint)

# String Operators * and +
astring * 3
# whateverwhateverwhatever
astring + astring
# 'whateverwhatever'
astring + 100
# error
astring + str(100)
# whatever100

# operators
# unary operators - + and - , - used to denote a negative number
# bitwise operators
a_for_bit = 2
print(bin(a_for_bit))
'0000 0010'
b_for_bit = 3
'0000 0011'
print(bin(b_for_bit))
'''
bitwise and 
0000 0010
0000 0011
----------
0000 0010 - 2

bitwise or
0000 0010
0000 0011
----------
0000 0011 - 3

>> right shift 1
0000 0010
0000 0001 - 1
<< left shift 1
0000 0100  - 4
'''
print(a_for_bit |  b_for_bit)
print(a_for_bit & b_for_bit)
print(a_for_bit  >> 1)
print(a_for_bit  << 1)

#  real world use cases for bitwise operators
# https://stackoverflow.com/questions/2096916/real-world-use-cases-of-bitwise-operators

# Built in functions
print('any built in ', any(x > 8 for x in range(10)))
print('all built in ', all(x > 8 for x in range(10)))
print('bin binary representatin ', bin(10))
print('chr unicode character for integer argument ', chr(97))

# delattr delete attribute from an object


class Person:
    def __init__(self, fname, lname, h, w):
        self.fname = fname
        self.lname = lname
        self.height = h
        self.weight = w


apers = Person('samar', 'kukreja', 175, 70)
print(apers.fname, apers.lname)
delattr(apers, 'lname')
# print(apers.fname, apers.lname)
print(apers.fname, apers.height, apers.weight)

# divmod
print(divmod(10, 3))

# enumerate
print(list(enumerate(range(10))))

# eval and exec
# eval executes a single python expression
# exec can take a code block that has statements
# eval returns value, exec always returns None and can be used for side effects
x = 1
print(eval('x + 1'))
print(exec('x=10'))
print(eval('x + 1'))

# filter
print(list(filter(lambda x: x % 2 == 0, range(10))))

# format
# see also Format Specification Mini-Language
# https://docs.python.org/3/library/string.html#formatspec
# value fromatted as per format specifier
# here width 6, fill 0  000010
print(format(10, '06d'))
# here + sign will be printed
print(format(10, '+6d')) #'   +10' +06d will lead to '+00010'
# left alignment
print(format(5,'0<10d'), 'see the alignment') #5000000000 if one leaves out 0 then '5        '
# right alignment and fill with 0s
print(format(10, '0>10d')) #'        10'
# format string syntax using curly braces
print("{1} then some literal stuff {0:010.4f}".format(94, 0037.4)) #94 then some literal stuff 00037.4000
print("{astr!r:>20s}".format(astr="test str"))
for align, text in zip('<^>', ['left', 'center', 'right']):
    print('{0:{fill}{align}16}'.format(text, fill=align, align=align))

# mote stuff on formatting
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two'))
# padding and aligning
print('%10s %10s' % ('one', 'two'))
print('{:<10s} {:>10s}'.format('one', 'two'))
print('{:->10}'.format('one'))

# numbers formatting
print('%d %d' % (23, 37))
print('{} {}'.format(23, 37))
print('%04d, %04d' % (23, 37))
print("{1:04d}, {0:04d}".format(23, 37))
print('%08.3f' % pi)
print('{:012.6f}'.format(pi))
# signed numbers
print('%+d' % 43)
print('{:+d}'.format(43))

# named placeholders
data = {'first': 'Hodor', 'last': 'Hodor!'}
print('%(first)s %(last)s' % data)
print('{first} {last}'.format(**data))
print('{first} {last}'.format(first='Hodor', last='Hodor!'))

# frozenset
alist = [1, 2, 1, 2, 2, 2, 3]
a_fr_set = frozenset(alist)
print(a_fr_set)

# getattr
print(getattr(apers, 'fname'))
# globals
globals()
# hasattr
print(hasattr(apers, 'weight'))
# hash
print(hash(apers))
# hex
print("hex example:", hex(255), format(255, "#x"))

# isinstance, issubclass
isinstance(apers, Person)
issubclass(Person, object)

# iter
with open('D:\\ufdata\\shakespeare.txt') as fp:
    idx_line = 0
    for line in iter(fp.readline, 1):
        print(line)
        idx_line += 1
        if idx_line == 10:
            break
# mao
print(list(map(lambda x: x ** 3, range(10))))

# next
riter = iter(range(10))
while True:
    try:
        print(next(riter))
    except StopIteration:
        print('we are here')
        break

# oct
print(oct(8))
print('%#o' % 10, '%o' % 10)
print(format(10, '#o'), format(10, 'o'))
print(f'{10:#o}', f'{10:o}')

# open


def print_line(some_file):
    print(some_file.readline())


shak_file = open('D:\\ufdata\\shakespeare.txt')
file_counter = 0
print_line(shak_file)
print_line(shak_file)
print('telling location ', shak_file.tell())
shak_file.seek(1000)
print_line(shak_file)
print(shak_file.tell())
for line in shak_file:
    file_counter += 1
    print(line)
    if file_counter == 10:
        break


# property
class C:
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x
    x = property(getx, setx, delx, "I'm the 'x' property.")


ac = C()
print(ac.x)
ac.x = 'aprop'
print(ac.x)
# del ac.x
print(ac.x)


class CPD:   # Class Property Demo
    def __init__(self):
        self._bcd = None

    @property
    def x(self):
        return self._bcd

    @x.setter
    def x(self, value):
        self._bcd = value

    @x.deleter
    def x(self):
        del self._bcd


acpd = CPD()
print(acpd.x)
acpd.x = 'aprop'
print(acpd.x)

# repr
print(repr(acpd))
today = datetime.datetime.now()
print(str(today))
print(repr(today))

# reversed
print(list(reversed(range(10))))
# round
print(round(pi, 2))

# set
print(set([1, 1, 2, 1, 1]))

# setattr
setattr(apers, 'lname', 'new last name')
setattr(apers, 'new_attr', 'new attribute')
print(apers.lname)
print(apers.new_attr)

# slicing
slice_obj = slice(2, 18, 3)
print(list(range(20))[slice_obj])
print(list(range(20))[2:18:3])

# sorted
items = list(range(20))
seed(100)
shuffle(items)
print(items)
items = sorted(items)
print(items)
print(sorted(items, reverse=True))

# sum
print(sum(range(10)))
print(sum(range(10), 200))


# static method class example
class SMCE:

    def __init__(self, x=10, y=10):
        self.length = x
        self.breadth = y

    @classmethod
    def area_class(cls, length, breadth):
        print('class method called')
        return length * breadth

    @staticmethod
    def area_static(length, breadth):
        print('static method called')
        return length * breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return (self.length + self.breadth) * 2


print(SMCE.area_static(10, 20))
print(SMCE.area_class(5, 5))
asmc = SMCE(10, 10)
print(asmc.area())
print(asmc.perimeter())

# tuple
atuple = 3, 4, 5
print(atuple)
print(atuple[0])
x, y, z = atuple
print(x, y, z)

# type
print(type(apers))
print(type(range(20)))

# vars
print(vars(apers))

# zip
print(list(zip(['Pele', 'BeckenBauer', 'Maradona'],
               [(1958, 1962, 1970), (1974, ), (1986,)])))

a_zip_list = list(zip(range(10), range(10, 20)))
print(a_zip_list)
print(list(zip(*a_zip_list)))

# for - python for works using the foreach logic
from random import Random
total_nos_looped = 0
# break execution
for x in range(10):
    print(x)
    decider = Random().randint(0, 100)
    total_nos_looped += 1
    if decider < 50:
        print('no {} less than 50  has been generated, therefore exiting after {} iterations'.format(decider, total_nos_looped))
        break

# continue
continue_loop_counter = 0
for x in range(10):
    print(x)
    decider = Random().randint(0, 100)
    continue_loop_counter += 1
    if decider < 50:
        if decider % 2 == 0:
            print('decider {} is even therefore continuing'.format(decider))
            continue
        else:
            print('odd no {} less than 50  has been generated, therefore exiting after {} iterations'.format(decider, continue_loop_counter))
            break

# pass - do nothing
for x in range(10):
    if x % 2 == 0:
        print('Number ', x)
    else:
        pass


# control structures
def is_prime(x):
    try:
        if(x <= 0):
            raise ValueError('positive integer needed')
        if(type(x) == float):
            raise ValueError(('As of now we are not stripping'
                              ' decimals to evaluate the '
                              'integer part.\nPlease provide'
                              ' a positive integer'))
        if(x == 1):
            return False
        if(x == 2):
            return True
        return all([x % n != 0 for n in range(2, int(sqrt(x)+1))])
    except ValueError as verr:
        print(verr)
    except Exception as error:
        print('Some problem occurred: ', error)


print(is_prime(3.4))

counter = 0
no_primes = 0
no_primes_within_prime = 0
while (counter < 10):
    rand_no = randint(0, 100)
    if (is_prime(rand_no)):
        no_primes += 1
        for x in range(2, rand_no+1):
            if(is_prime(x)):
                no_primes_within_prime += 1
        print(('random number generated {:d} '
               'and there were {:d} prime numbers'
               ' up till that number').
              format(rand_no, no_primes_within_prime))
        no_primes_within_prime = 0
    counter += 1
    if(counter == 10):
        print('we had {:d} prime numbers in this run'.format(no_primes))


def grad_from_percent(score):
    if(score >= 80):
        return 'A+'
    elif(score >= 65):
        return 'A'
    elif(score >= 55):
        return 'B'
    elif(score >= 45):
        return 'C'
    else:
        return 'D'


print(grad_from_percent(64))
