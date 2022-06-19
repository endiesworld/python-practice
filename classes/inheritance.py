class Person:
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
        return f'Hi there my {self.__firstname} {self.__surname}'

    def __str__(self, value) -> str:
        return f'Hello I am {self.__firstname} {self.__surname}, and I am {value}'


class Student(Person):
    def __init__(self, firstname, surname, school_name) -> None:
        super().__init__(firstname, surname)
        self.school_name = school_name

    @property
    def school_name(self):
        return self.__school_name

    @school_name.setter
    def school_name(self, school_name):
        self.__school_name = school_name

    def __str__(self) -> str:
        return super().__str__('Student')


student = Student('Emmanuel', 'Okoro', 'UNN')

print(student.say_hello())
