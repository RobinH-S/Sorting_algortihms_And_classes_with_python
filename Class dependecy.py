'''
Class dependency, a class uses object of other class
Dependency exists when one class relies on
another in some way, usually by invoking the
methods of the other.
'''
from random import  randint

class Die:
    def roll(self):
        self.value = randint(1,6)

class DicePlayer:
    def play(self):
        self.die = Die()
        self.die.roll()
        print('Die value: ', self.die.value)


""" Test objects 
player = DicePlayer()
player.play()
player.play()

"""

"""Composition
Composition: process of collecting several
objects to compose a new one. Composition is
usually a good choice when one object is part
of another object.
Example:
va Car class is composed of:
-Engine class
-BrakingSystem class
"""

class Student:
    def __init__(self, name, dept_name):
        self.name = name
        self.department = Department(dept_name)


    def print_info(self):
        print('Student name: ', self.name,
              ', Department', self.department.dept_name)

class Department:
    def __init__(self, dept_name):
        self.dept_name = dept_name

"""
#Test objekter for composition
student = Student('Roger' , 'UIB-Sv')
student.print_info()
"""


class Salary:
    def __init__(self, payment):
        self.payment = payment


class Engineer:

    def __init__(self, pay):
        self.pay = Salary(pay)

    def compute_salary(self):
        yearlywage = self.pay.payment * 12
        return yearlywage

    def print_salary(self):
        print(self.compute_salary())


"""Aggregation
-Similar relationship is Aggregation which is a
week form of composition

-Aggregation does not imply ownership

Engine BrakingSys
-The difference is that
aggregate objects can
exist independently. 
"""


"""Interface  - Relationship
Interface is a set of publicly accessible
methods on an object which can be used by
other parts of the program to interact with
that object.

-In general, interface provides a collection of
abstract methods and attributes that other
classes provide their implementation.

-Interface in Python can be defined with an
abstract class that has only abstract methods.
"""

from abc import ABC, abstractmethod
#Abstract Base Classes (ABCs).


class Animal (ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print('Dog barks!')


class Lion(Animal):
    def speak(self):
        print('Lion roars!')


class DvdPlayer(ABC):

    def play(self, dvd):
        pass

    def eject(self):
        pass


class ziDvdPlayer(DvdPlayer):

    def play(self, dvd):
        print(dvd, 'is playing')

    def eject(self):
        print('Dvd is ejecting')

player = ziDvdPlayer()
player.play('Xmen')