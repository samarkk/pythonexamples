from random import seed, randint
from math import sqrt

# A mapping object maps hashtable values to arbitrary objects
# class dict(**kwarg)¶
a = dict(one=1, two=2, three=3)
print(a)
b = {'one': 1, 'two': 2, 'three': 3}
print(b)
# class dict(iterable, **kwarg)
c = dict([('one', 1), ('two', 2), ('three', 3)])
c_with_kwargs = dict([('one', 1), ('two', 2), ('three', 3)], four=4)
print(c_with_kwargs)
d = dict({'two': 2, 'three': 3, 'one': 1})
print(d)
# mappings are unordered key value collections
print(a == b == c == d)

# dictionary operations
print(len(a))
print(a['one'])  # will raise a keyerror if key not in map
a['four'] = 4
print(a)
print('four' in a, 'five' in a)
print([x for x in iter(a)])
print(a.get('five', 0))
print(a.pop('four'))
print(a.pop('five', 0))
a_vals = a.values()
print(a_vals)

# values returns a dynamic dict view
# as the base changes so does the view
a['three'] = 33
print(a_vals)
a['four'] = 4
print(a_vals)

alist = []
seed(100)
for x in range(10):
    alist.append(randint(0, 100))
print(alist)

int_2_check = randint(0, 100)
print(int_2_check)
print(int_2_check in alist)
print(alist + list(range(5)))
# for two lists to be considered equal in value they 
# should have the same items in the same places
# [1, 2] == [1, 2] is True and [1, 2] == [2, 1] is False
print(alist * 2, alist * 2 == 2 * alist)

# indexing
print('position 0: ', alist[0])
print(alist[3:7])
# every second item between 3 and 7
print(alist[3:7:2])
print(alist[-7:])
print(alist[-9:-5])

# len, min and max
print(len(alist), min(alist), max(alist))

# index
print(alist.index(58))
print(alist.index(58, 2))

print([[x, alist.count(x)] for x in set(alist)])

alist[0] = 1000
print(alist)
# lists are modified in place and list variables hold references
blist = alist
blist[0] = 18
print(alist)

alist[3:5] = [37, 23]
print(alist)

del alist[3:5]
print(alist)

alist.append(37)
print(alist)
blist = alist.copy()
alist.clear()
print(alist)
print(blist)
alist = blist
alist *= 2
print(alist)
alist.pop()
print(alist)
alist.remove(58)
print(alist)
alist.reverse()
print('alist reversed ', alist)
alist.sort()
print('alist sorted ', alist)

empty_tuple = ()
print(type(empty_tuple))
singleton_tuple = ('whatever',)
print(singleton_tuple, len(singleton_tuple))
a_tuple = 23, 37, 41
a_tuple_par = (23, 37, 41)
print(len(a_tuple), a_tuple == a_tuple_par)

seed(10)
fset = set([randint(0, 10) for x in range(10)])
sset = set([randint(0, 10) for x in range(30)])
print(len(fset), fset)
print(len(sset), sset)
print(fset.union(sset))
print(fset.intersection(sset))
print(fset.difference(sset))
# difference between sset and fset will give
# {1, 2, 5, 8, 10}
print(sset.difference(fset))
# will retain only intersecting elements from fset
sset.intersection_update(fset)  # symbolically &=
print(sset)
sset.add(19)
print(sset)
a_frozen_set = frozenset(sset)
print(a_frozen_set)
a_frozen_set.issubset(sset)
a_frozen_set.isdisjoint(fset)
# sets support the update operation, frozensets do not
# will add on elements from sset that are not in fset
# to fset - fset will contain from 0 to 10
fset |= sset
fset.update(sset)
print('fset updated using sset ', fset)
# difference update
# simlar to seet.differenc(fset)
sset -= fset
print('sset after difference update ', sset)
# remove, discard, pop, clear are supported
# remove will raise a keyerror if element not present
# discard will not
fset.remove(30)
fset.discard(30)
fset.pop()
print(fset)

# comprehensions
# a simple comprehension filtering numbers from list and squaring them
a_list = [1, '4', 9, 'a', 0, 4]
squared_ints = [e**2 for e in a_list if type(e) == int]
print(squared_ints)
# the same manipulations using lambda functions map and filter
print(list(map(lambda x: x ** 2, filter(lambda x: type(x) == int, a_list))))
# [ 1, 81, 0, 16 ]
# Let us find the pythagorean triples i.e pairs of three
# numbers where the square of one is equal to the sum of the
# squares of the other two
p_triples = [(x, y, z) for x in range(1, 21)
             for y in range(1, 21)
             for z in range(1, 21)
             if x ** 2 + y ** 2 == z ** 2]
print(p_triples)


def remove_dup_tuples(tuple_list):
    tup_wo_dups = []
    tuple_list = [sorted(x) for x in tuple_list]
    print('sorted tuple list ', tuple_list)
    for x in tuple_list:
        if x not in tup_wo_dups:
            tup_wo_dups.append(x)
    return tup_wo_dups


p_triples_unique = remove_dup_tuples(p_triples)
print(p_triples_unique)

# use filter to get triples
el = []  # empty list
for x in range(1, 21):
    for y in range(1, 21):
        for z in range(1, 21):
            el.append((x, y, z))

triples_with_dups = list(sorted(x) for x in filter(
        lambda x: x[0] ** 2 + x[1] ** 2 == x[2] ** 2, el))
triples_without_dups = remove_dup_tuples(triples_with_dups)
print(triples_without_dups)

# set comprehensions
# use a set comprehension to find out the filter set for
# the sieve of erastothenes
target_number = 100
non_primes = set(y for x in range(2,
                 int(sqrt(target_number) + 1))
                 for y in range(2*x, target_number, x))
print(non_primes)
primes = [x for x in range(2, target_number) if x not in non_primes]
print(primes)

# generators
def generator_demo():
    alv = 273
    yield 1
    print('after 1')
    alv *= 2
    print('alv now is ', alv)
    yield 2
    print('after 2')
    alv *= 2
    print('alv now is ', alv)
    yield 3

agd = generator_demo()
print(next(agd))



# Fibonacci numbers using generator
def fib(n=10):
    counter = 0
    a, b = 0, 1
    while True:
        yield a
        # print(a)
        a, b = b, a + b
        counter += 1
        if(counter == n):
            break


afib = fib(50)
next(afib)
for fn in list(fib(300)):
    print('{:d}'.format(fn))

# a generator expressiona_gen_exp = (x for x in range(3))
a_gen_exp = (x for x in range(3))
print(next(a_gen_exp))
print(next(a_gen_exp))
print(next(a_gen_exp))
print(hasattr(a_gen_exp, '__iter__'))
print(next(a_gen_exp))
