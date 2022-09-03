def caesarCipherEncryptor(string, key):
    encrypted_string = ""

    for c in string:
        new_c = ord(c) + key

        while new_c > 122:
            new_c = new_c - 122 + 96
            
        encrypted_string += chr(new_c)

    return encrypted_string
