def ceasarCipher(s, k):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    solution = ''

    for char in s:
        if not char.isalpha():
            solution += char
        elif char.isupper():
            if ord(char) - 65 + k > len(alphabet)-1:
                solution += alphabet[(ord(char) - 65 + k) % len(alphabet)].upper()
            else:
                solution += alphabet[ord(char) - 65 + k].upper()
        else:
            if ord(char)-97 + k > len(alphabet)-1:
                solution += alphabet[(ord(char)-97 + k) % len(alphabet)]
            else:
                solution += alphabet[ord(char)-97 + k]

    print(solution)

if __name__ == '__main__':
    s0 = 'middle-Outz'
    k0 = 2
    s1 = 'Hello_World!'
    k1 = 4
    s2 = 'www.abc.xy'
    k2 = 87
    ceasarCipher(s2, k2)
