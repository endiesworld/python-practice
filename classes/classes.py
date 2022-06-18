class Person():
    def __init__(self, firstname, surname) -> None:
        self.firstname = firstname
        self.surname = surname

    @property
    def firstname(self):
        return self.__firstname

    @firstname.setter
    def firstname(self, firstname):
        print('In the firstname setter ')
        self.__firstname = firstname

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        self.__surname = surname

    def say_hello(self):
        return f'Hi there!, I am {self.__firstname} {self.__surname}'


first_person = Person('Emmanuel', 'Okoro')

print(first_person.say_hello())

first_person.firstname = 'Ndubuisi'
print(first_person.say_hello())
