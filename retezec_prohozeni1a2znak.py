# prohazuje 1.za 2. znak přes celý řetězec, následně 3. za 4. atd...
def swap_chars(string):
    char_list = list(string)
    for i in range(0, len(char_list)-1, 2):
        char_list[i], char_list[i+1] = char_list[i+1], char_list[i]
    swapped_string = ''.join(char_list)
    return swapped_string

input_string = "nyní musíš předvést, zda umíš rodině zaopatřit jídlo, chyť na náměstí holuba frajere"
swapped_string = swap_chars(input_string)
print(swapped_string)

