# RULES
# this was a coding challenge i had to do for a previous interview (in C++)
# it had a very bad "presentation of the rules" so hopefully the ones below are explained well enough

# input is an list of different types (integers and characters - as in string of length 1)
# go through the elements of the list from the beginning to end
# whenever you find a character (always the same, "E"), remove the LOWEST value in the list so far
# at the end, the output has to be all of the "removed" elements

# Additional rule, the program never gives you a "character" if you're lacking an integer to "remove"

def function_test(list_to_modify):
    input_list = []
    for elem in list_to_modify:
        input_list.append(elem)
    removed_elements = []
    i = 0
    while i < len(input_list):
        if type(input_list[i]) == str:
            lowest_value = min(input_list[0:i])
            removed_elements.append(lowest_value)
            removed_elem_index = input_list.index(lowest_value, 0, i)
            input_list.pop(removed_elem_index)
            input_list.pop(i-1)
            i -= 1
        else:
            i += 1

    return removed_elements
