# o jedno písmeno v abeceně vpřed
def shift_char(char):
    if char.isalpha():
        if char.islower():
            shifted_char = chr((ord(char) - ord('a') + 1) % 26 + ord('a'))
        else:
            shifted_char = chr((ord(char) - ord('A') + 1) % 26 + ord('A'))
    else:
        shifted_char = char
    return shifted_char

def shift_string(string):
    shifted_string = ""
    for char in string:
        shifted_string += shift_char(char)
    return shifted_string

input_string = "musis ukazat, ze umis ctit stanovena pravidla a pri objednavce/koupi alkoholu ukazat automaticky obcanku"
shifted_string = shift_string(input_string)
print(shifted_string)
