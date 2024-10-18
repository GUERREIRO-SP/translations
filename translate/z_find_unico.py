from django.test import TestCase
import time

def find_uniq(arr):
    n: int = 0
    set_num: set = set(arr)

    for i in set_num:
        if arr.count(i)==1:
            n = i

    return n   # n: unique number in the array





t1 = time.time()

print(find_uniq([ 1, 1, 1, 2, 1, 1 ]), 2)
print(find_uniq([ 0, 0, 0.55, 0, 0 ]), 0.55)
print(find_uniq([ 3, 10, 3, 3, 3 ]), 10)

tempoExec = time.time() - t1

print("Tempo de execução: {} segundos".format(tempoExec))

