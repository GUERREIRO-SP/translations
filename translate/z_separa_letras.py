from django.test import TestCase
import time

def solution(s):
    lst_retorno: list = []
    numero: int = 0
    result: str = ""
    for char in s:
        numero += 1
        result += char
        if numero == 2:
            lst_retorno.append(result)
            numero = 0
            result = ""

    if numero == 1:
        result = char + "_"
        lst_retorno.append(result)

    print(s, lst_retorno)

    return lst_retorno


t1 = time.time()

#    ['as', 'df', 'ad', 'sf']
print(solution("asdfadsf"))
#    ['as', 'df', 'ad', 's_']
print(solution("asdfads"))
print(solution(""))
print(solution("x"))


tempoExec = time.time() - t1

print("Tempo de execução: {} segundos".format(tempoExec))

