# First approach with using while
def vowels(some_string: str):
    i = 0
    vowels_quantity = 0
    while i < len(some_string):
        if some_string[i].lower() in "aeiou":
            vowels_quantity += 1
        i += 1
    return vowels_quantity


assert (vowels("hApPyHalLOweEn!") == 5)
print(vowels("hApPyHalLOweEn!") == 5)


# Extended using while, if and elif
def count_vowels_in_string(some_string):
    temp_array = []
    i = 0
    while i < len(some_string):
        if some_string[i].lower() == 'a':
            temp_array.append(i)
        elif some_string[i].lower() == 'e':
            temp_array.append(i)
        elif some_string[i].lower() == 'i':
            temp_array.append(i)
        elif some_string[i].lower() == 'o':
            temp_array.append(i)
        elif some_string[i].lower() == 'a':
            temp_array.append(i)
        i += 1
    return len(temp_array)


assert (count_vowels_in_string("hApPyHalLOweEn!") == 5)
print(count_vowels_in_string("hApPyHalLOweEn!") == 5)


# Second approach without using while
def simple_count_vowels_in_string(some_string):
    found_a = some_string.lower().count('a')
    found_e = some_string.lower().count('e')
    found_i = some_string.lower().count('i')
    found_o = some_string.lower().count('o')
    found_u = some_string.lower().count('u')
    return found_a + found_e + found_i + found_o + found_u


assert (simple_count_vowels_in_string("hApPyHalLOweEn!") == 5)
print(simple_count_vowels_in_string("hApPyHalLOweEn!") == 5)
