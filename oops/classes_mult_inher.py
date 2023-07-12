class Person:
    def __init__(self, fn, ln, age):
        self.last_name = ln
        self.first_name = fn
        self._age = age

    def __str__(self):
        return self.first_name + " " + self.last_name + ', ' + str(self.age)

    @property
    def age(self):
        print('Gettnig Age')
        return self._age

    @age.setter
    def age(self, value):
        print('Setting Age')
        self._age = value


apers = Person('john', 'doe', 25)
print('A Person ', apers)


class Doctor(Person):
    def __init__(self, fn, ln, age, degree, mregno):
        Person.__init__(self, fn, ln, age)
        self.degree = degree
        self.registration_no = mregno

    def __str__(self):
        return super().__str__() + ' qualification: ' + \
            self.degree + ' registration_no: ' + str(self.registration_no)


a_doctor = Doctor('Arjun', 'Reddy', 33, 'MBBS', 234213)
print('A Doctor ', a_doctor)


class Administrator(Person):
    def __init__(self, fn, ln, age, district, **kw):
        Person.__init__(self, fn, ln, age)
        self.district = district

    def __str__(self):
        return super().__str__() + ' ' + self.district


an_admin = Administrator('Alfred', 'Beckenbauer', 45, 'Cologne')
print('An administrator ', an_admin)


'''
To inherit from multiple classes,
we can call mro method to see the order
in which parent classes are invoked.

And then we will have to explicitly invoke
parent class methods to initialize the
child class of multiple parents
'''


class MedicalAdmin(Administrator, Doctor):

    def __init__(self, fn, ln, age, degree, mregno, district, wards):
        Doctor.__init__(self, fn, ln, age, degree, mregno)
        Administrator.__init__(self, fn, ln, age, district)
        self.wards = wards

    def __str__(self):
        return Doctor.__str__(self) + ' district: ' + self.district +\
            ' wards: ' + str(self.wards)


print(MedicalAdmin.mro())

a_med_admin = MedicalAdmin('Jurgen', 'Rao', 47, 'MD', 43192, 'Munich', 22)
print('A Medical Admin, ', a_med_admin)


# Properties
class Celsius:
    def __init__(self, temperature=0):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32

    def get_temperature(self):
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value


a_celsius = Celsius(100)
print(a_celsius.to_fahrenheit())


class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    def get_temperature(self):
        print("Getting value")
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value

    temperature = property(get_temperature, set_temperature)


c = Celsius()
print(c.get_temperature())
print(c.temperature)


class Celsius:
    def __init__(self, temperature=0):
        # we cannot have temperature here as that will start an
        # nfinite recursive loop when we set the value
        # Any thing else than temperaure will work but to keep
        # code readable _teimperature is preferred
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self._temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value


c_new = Celsius()
print(c_new.temperature)
c_new.temperature = 45
print(c_new.temperature)

# classes and objects built in functoins
print(issubclass(MedicalAdmin, Doctor))
print(isinstance(a_med_admin, Doctor))
print(isinstance(a_med_admin, Administrator))
print(isinstance(a_celsius, Doctor))
print(hasattr(c_new, 'temperature'))
print(dir(c_new))
print(vars(a_med_admin))

# object oriented foundations and synctactic sugars
a_int = 3
print(a_int + 2)
print(a_int.__add__(2))
a_dict = {'a': 7}
a_dict.__setitem__('b', 8)
print(a_dict)
print(a_dict.__getitem__('b'))
