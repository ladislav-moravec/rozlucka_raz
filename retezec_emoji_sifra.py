# nahradi urcity znak nějakym emoji
def encrypt_string(string):
    encrypted_string = ""
    emoji_mapping = {
        'a': '😀',
        'b': '😃',
        'c': '😄',
        'd': '😁',
        'e': '😆',
        'f': '😅',
        'g': '🤣',
        'h': '😂',
        'i': '😊',
        'j': '😇',
        'k': '🙂',
        'l': '🙃',
        'm': '😉',
        'n': '😌',
        'o': '😍',
        'p': '😘',
        'q': '😗',
        'r': '😙',
        's': '😚',
        't': '😋',
        'u': '😛',
        'v': '😝',
        'w': '🤑',
        'x': '🤗',
        'y': '🤔',
        'z': '🤐'
    }

    for char in string.lower():
        if char.isalpha():
            encrypted_string += emoji_mapping.get(char, char)
        else:
            encrypted_string += char

    return encrypted_string


input_string = "ahoj razi nyni te ceka dalsi ukol a to stezka odvahy v zoologicka zahrade tak at se ti dari"
encrypted_string = encrypt_string(input_string)
print(encrypted_string)
