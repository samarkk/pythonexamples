class Stack:
    """Well known data structure"""
    def __init__(self):  # constructor
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        x = self.items[-1]
        del self.items[-1]
        return x

    def empty(self):
        return len(self.items) == 0


x = Stack()
print(x.empty())
print(x.push(1))
print(x.empty())
print(x.pop())
[x.push(y) for y in range(10)]
print(x.items)


class FancyStack(Stack):
    """stack with ability to inspect lower stack items"""
    def peek(self, n):
        """peek(0) returns topmost item peek(-1)
           the one below that and so on"""
        size = len(self.items)
        assert 0 <= n < size
        return self.items[size-1-n]


afs = FancyStack()
[afs.push(x) for x in range(10)]
print(afs.peek(7))


class LimitedStack(FancyStack):
    def __init__(self, limit):
        self.limit = limit
        super().__init__()
        super(LimitedStack, self).__init__()

    def push(self, x):
        assert(len(self.items) < self.limit)
        super().push(x)


als = LimitedStack(2)
als.push(1)
print(als.items)
als.push(2)
print(als.items)
# als.push(3)


class Connection:
    verbose = 0  # class variable

    def __init__(self, host):
        self.host = host

    def debug(self, v):
        self.verbose = v

    def connect(self):
        if self.verbose:
            print('connecting to host ', self.host)


ac = Connection('some host')
print(ac.verbose)
ac.connect()
ac.debug(1)
print(ac.verbose)
ac.connect()


class VarDemo:
    classlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def pop(self):
        del self.classlist[-1]

    def push(self, x):
        self.classlist.append(x)


avd = VarDemo()
avd.pop()
print(avd.classlist)

bvd = VarDemo()
print(bvd.classlist)
bvd.push(100)
print(avd.classlist)


class Person:
    def __init__(self, fn, ln, age):
        self.last_name = ln
        self.first_name = fn
        self.age = age

    def __str__(self):
        return self.first_name + " " + self.last_name + ', ' + str(self.age)


apers = Person('john', 'doe', 25)
print('A Person ', apers)


class Doctor(Person):
    def __init__(self, fn, ln, age, degree, mregno, **kw):
        # super().__init__(fn, ln, age)
        '''
        super() can also take two parameters: 
        the first is the subclass, 
        and the second parameter is an object 
        that is an instance of that subclass

        the method being called will be searched for
        one level above the subclass used in the 
        super call
        '''
        super(Doctor, self).__init__(fn, ln, age)
        self.degree = degree
        self.registration_no = mregno

    def __str__(self):
        return super().__str__() + ' qualification: ' + \
            self.degree + ' registration_no: ' + str(self.registration_no)


a_doctor = Doctor('Arjun', 'Reddy', 33, 'MBBS', 234213)
print('A Doctor ', a_doctor)


class Surgeon(Doctor):
    def __init__(self, fn, ln, age, deg, mregno, specialization):
        super().__init__(fn, ln, age, deg, mregno)
        self.specialization = specialization

    def __str__(self):
        return super().__str__() + ' specialization: ' + self.specialization


a_surgeon = Surgeon('Arjun', 'Reddy', 33, 'MBBS', 234213, 'Ortho')
print('A Surgeon ', a_surgeon)

print(Surgeon.mro())


class Administrator(Person):
    def __init__(self, fn, ln, age, district, **kw):
        super().__init__(fn, ln, age)
        self.district = district

    def __str__(self):
        return super().__str__() + ' ' + self.district


an_admin = Administrator('Alfred', 'Beckenbauer', 45, 'Cologne')
print('An administrator ', an_admin)
