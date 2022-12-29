def get_even_or_odd_numbers(n, is_even):
    return [i for i in range(0, n) if i % 2 != int(is_even)]


assert get_even_or_odd_numbers(3, True) == [0, 2]
assert get_even_or_odd_numbers(4, False) == [1, 3]

list1 = ['hello', 'orange', 'phenomenon']

def search_words(item, list1):
    return [s for s in list1 if s.count(item) == 1]


assert search_words('he', ['hello', 'orange', 'phenomenon']) == ['hello', 'phenomenon']
assert search_words('abc', ['hello', 'orange', 'phenomenon']) == []


def flatten(arr):
    for item in arr:
        yield from item

flatten([[1, 2], [], [3, 4, 5]])

generator = flatten([[1, 2], [], [3, 4, 5]])
assert next(generator) == 1
assert next(generator) == 2
assert next(generator) == 3
assert next(generator) == 4
assert next(generator) == 5





