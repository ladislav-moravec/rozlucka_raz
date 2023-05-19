def swap_chars(string):
    char_list = list(string)
    for i in range(0, len(char_list)-1, 2):
        char_list[i], char_list[i+1] = char_list[i+1], char_list[i]
    swapped_string = ''.join(char_list)
    return swapped_string

def reverse_string(string):
    reversed_string = string[::-1]
    return reversed_string

input_string = "prokaž, že se zvládneš dorozumět v každé situaci a objednej si na baru drink bez jediného slova"
swapped_string = swap_chars(input_string)
reversed_string = reverse_string(swapped_string)
print(reversed_string)
