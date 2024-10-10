# import math
import time

# def is_palindromo(num):
#     n1 = 0
#     f = len(str(num)) - 1 
#     while f > n and num[n1] == num[f]:
#         f -= 1
#         n1 += 1
#     if num[n1] == num[f]:
#         return True
#     else:
#         return False


def invert_num(num) -> int:
    return int(str(num)[::-1])

def insert_list(numero, list_primo):
    for pos in range(len(list_primo)-1, 0, -1):
        num_in_list = list_primo[pos] 
        if num_in_list < numero:
            list_primo.insert(pos+1, numero)
            return 
        elif num_in_list == numero:
            return
        


def is_primo(numero, list_primo):
    
    # raiz4 = int(math.sqrt(numero)) 
    raiz4 = int(numero**(1/2)) 
    for num in list_primo:
        if num > raiz4:
            break
        if numero % num == 0:
            return False
    
    insert_list(numero, list_primo)
    return True     # é primo


def find_emirp(n):
    list_primo = [2, 3, 5, 7, 11, 13,]  
    n_invert = 0
    n_qtd = 0
    n_maior = 0
    n_soma = 0
    n_ini = 13
    n_fim = n
    for i in range(n_ini, n_fim, 2):

        if is_primo(i, list_primo):
            n_invert =  invert_num(i)
            if n_invert==i  or n_invert % 2 == 0:
                continue
            if is_primo(n_invert, list_primo):
                n_qtd += 1
                n_maior = i
                n_soma += i
            
#     print(list_primo)            
    return[n_qtd, n_maior, n_soma] #[amount of emirps in the range(13, n + 1), largest emirp smaller than n, sum of all the emirps of this range.



t1 = time.time()

print(find_emirp(666430))

tempoExec = time.time() - t1
print("Tempo de execução: {} segundos".format(tempoExec))
