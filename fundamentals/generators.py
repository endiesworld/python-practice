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
