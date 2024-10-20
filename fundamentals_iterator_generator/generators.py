"""
    List comprehensions vs. generators
        Now the question on everybody's lips is, "What is this generator object?" Well, 
        a generator is like a list comprehension except it does not store the list in memory: it does not construct the list, 
        but is an object we can iterate over to produce elements of the list as required.

    Printing values from generators (2)
        like any other iterator, we can pass a generator to the function next in order to iterate through its elements. 
        For the geeks like me, this is an example of something called lazy evaluation, whereby the evaluation of the expression is 
        delayed until its value is needed. This can help a great deal when working with extremely large sequences as you don't want 
        to store the entire list in memory, which is what comprehensions would do; you want to generate elements of the sequence on the fly.

    Generators vs. list comprehensions
        Memory Usage:
            Lists: A list stores all its elements in memory at once. This means if you have a large dataset, storing it all in memory 
            can be very inefficient and possibly lead to memory errors.
            Generators: A generator doesn't store all of its values in memory. Instead, it generates each value on the fly and only 
            keeps one value at a time. This makes it highly memory-efficient, especially for large datasets or infinite sequences.
        Performance:
            Lists: Since lists store everything in memory, they are faster when it comes to random access. You can access any element 
            of the list in constant time, O(1). my_list = [1, 2, 3, 4, 5]
            print(my_list[3])  # Fast access: Output 4.
            Generators: Generators, on the other hand, don’t allow random access. You have to iterate over them to get to a specific value, 
            which can be slower. Generators are better suited for sequential access or when you process each value once and then discard it.

    

    Conditionals in generator expressions
        What's really cool is that anything we can do in a list comprehension such as filtering and applying conditionals, 
        we can also do in a generator expression, such as you see here. You'll get a whole bunch of practice with this in the upcoming exercises.

    Generator functions
        The last thing to discuss before you get coding is the ability to write generator functions. Generator functions are functions that, 
        when called, produce generator objects. Generator functions are written with the syntax of any other user-defined function, 
        however instead of returning values using the keyword return, they yield sequences of values using the keyword yield.

    Build a generator function
        Here I have defined a generator function that, when called with a number n, produces a generator object that generates 
        integers 0 though n. We can see within the function definition that i is initialized to 0 and that the first time the 
        generator object is called, it yields i equal to 0. It then adds one to i and will then yield one on the next iteration and so on. 
        The while loop is true until i equals equals n and then the generator ceases to yield values.

    Use a generator function
        This generator function can be called as you do any other function. Here I call the generator function with the argument, 
        We see that it produces a generator object and that we can iterate over this generator object with a for loop to print the 
        values it yields. Generator functions are a powerful and customizable way to create generators.
"""

first_10_evens = [number * 2 for number in range(10)]
print(f'The data type for firs_10_evens is {type(first_10_evens)}')

first_10_evens_generator = (number * 2 for number in range(10))
print(f'The data type for generator experession is {type(first_10_evens_generator)}')

"""
    Printing values from generators (1)
        Here we can see that looping over a generator expression produces the elements of the analogous list. 
        We can also pass a generator to the function list to create the list. Moreover,
"""
for element in first_10_evens_generator:
    print(element)


sequence = [2, 4, 6, 8, 10, 4, 12, 6, 14, 4, 16, 6, 4, 6, 18, 20]


def generator_fnc():
    global sequence
    for data in sequence:
        print(f'About to yield {data}')
        yield data


def take(count, sequence):
    counter = 0
    for data in sequence:
        if counter == count:
            return
        counter += 1
        print(f'The take function is called for the {counter} time')
        yield data


def distinct(iterable):
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        print(f' distinct function yiels {item}')
        yield item
        seen.add(item)


def run_pipeline():
    global sequence
    for item in take(3, list(distinct(sequence))):
        print(f'  run_pipeline function yields {item}')


# run_pipeline()

gen_expr = (data ** 2 for data in sequence)

print(f'The data type for generator experession is {type(gen_expr)}')
print(f'Generator object is a run once oject {list(gen_expr)}')
print(f'Check object for content: {sum(gen_expr)}')
