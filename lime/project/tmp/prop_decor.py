# -*- coding: UTF-8 -*-

class Person():

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        print('GET')
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

d = Person('wery')
# d.name = 'ok'

# Превращаем метод в свойство и разделяем логику на GET, SET или DEL
print(d.name)


def bold(fun_hello):
    def inner(*args):
        print ("<b>")
        fun_hello(*args)
        print ("</b>")
    return inner



@bold
def hello(who):
    print ("Hello", who)

hello('world')