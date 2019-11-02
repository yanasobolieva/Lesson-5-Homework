# Returning unique ordered list
def unique_ordered(some_list: list):
    unique_ordered_list = []
    i = 0
    while i < len(some_list):
        if some_list[i] not in unique_ordered_list:
            unique_ordered_list.append(some_list[i])
        i += 1
    return unique_ordered_list


assert unique_ordered(["a", 5, 2, 5, (1, "a"), "a"]) == ["a", 5, 2, (1, "a")]
print(unique_ordered(["a", 5, 2, 5, (1, "a"), "a"]) == ["a", 5, 2, (1, "a")])


# Returning unique disordered list
def unique_disordered(some_list: list):
    temp_set = set(some_list)
    unique_list = list(temp_set)
    return unique_list


# uncomment the nest line to see what the function returns
# print(unique_disordered(["a", 5, 2, 5, (1, "a"), "a"]))

# such assert wouldn't work as the function returns disordered list each time:
# assert unique_disordered(["a", 5, 2, 5, (1, "a"), "a"]) == [2, "a", 5, (1, "a")]
# can assert that the list contains only unique elements in the following way:
assert \
    len(set(unique_disordered(["a", 5, 2, 5, (1, "a"), "a"]))) == len(unique_disordered(["a", 5, 2, 5, (1, "a"), "a"]))
print(
    len(set(unique_disordered(["a", 5, 2, 5, (1, "a"), "a"]))) == len(unique_disordered(["a", 5, 2, 5, (1, "a"), "a"])))
