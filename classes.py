class Person:

    def __init__(self, name):
        print('__init__')
        self.name = name
    def greeting(self):
        print('hi {}'.format(self.name))
    def __del__(self):
        print('del')


person = Person('mo')
person.greeting()

person = ''