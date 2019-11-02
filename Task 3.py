# First approach using slice
def thirds(some_tuple: tuple):
    return some_tuple[2::3]


assert thirds((1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c')) == (3, 6, 9, 'b')
print(thirds((1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c')) == (3, 6, 9, 'b'))


# Second approach using for and enumerate
def thirds_second_approach(some_tuple: tuple):
    return tuple([item for i, item in enumerate(some_tuple, 1) if i % 3 == 0])


assert thirds_second_approach((1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c')) == (3, 6, 9, 'b')
print(thirds_second_approach((1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c')) == (3, 6, 9, 'b'))
