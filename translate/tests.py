from django.test import TestCase
import time

def is_pangram(st):
    boo_retorno: bool = True
    dic_str: dict = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}

    return set(st.lower()) >= set("abcdefghijklmnopqrstuvwxyz")

    # for char in st.lower():
    #     dic_str[char] = 1

    # if 0 in dic_str.values():
    #         boo_retorno: bool = False

    # return boo_retorno


t1 = time.time()

print(is_pangram("The quick brown fox jumps over the lazy dog."), 1)
print(is_pangram("Cwm fjord bank glyphs vext quiz"), 2)
print(is_pangram("Pack my box with five dozen liquor jugs."), 3)
print(is_pangram("How quickly daft jumping zebras vex."), 4)
print(is_pangram("ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ"), 5)

print(is_pangram("This isn't a pangram!"), 6)
print(is_pangram("abcdefghijklm opqrstuvwxyz"), 7)
print(is_pangram("Aacdefghijklmnopqrstuvwxyz"), 8)

tempoExec = time.time() - t1

print("Tempo de execução: {} segundos".format(tempoExec))

