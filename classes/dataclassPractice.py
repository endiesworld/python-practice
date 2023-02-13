from dataclasses import dataclass, field, asdict, astuple


# @dataclass
# class Person:
#     name: str
#     age: int
#     iq: int = 100
#     can_vote: bool = field(init=False)

#     def __post_init__(self):
#         print('called __post_init__ method')
#         self.can_vote = 18 <= self.age <= 70


# p = Person('Jane Doe', 25)
# print(p)


from dataclasses import dataclass, field


@dataclass(order=True)
class Person:
    sort_index: int = field(init=False, repr=False)

    name: str
    age: int
    gender: str = field(default='male', repr=False)
    iq: int = field(default=100)
    can_vote: bool = field(init=False)

    def __post_init__(self):
        self.can_vote = 18 <= self.age <= 70
        # sort by age
        self.sort_index = self.age


p = Person(name='John', age=25)

print("**************** VIEW object structure in str/repr ***************")
print(p)
print("**************** VIEW object as a dictionary ***************")
print(asdict(p))
print("**************** VIEW object as a tuple ***************")
print(astuple(p))

members = [
    Person(name='John', age=25),
    Person(name='Bob', age=35),
    Person(name='Alice', age=30)
]

sorted_members = sorted(members)
print("**************** VIEW sorted object ***************")
for member in sorted_members:
    print(f'{member.name}(age={member.age})')