
def is_palindrono(num):
    n = 0
    f = len(num) - 1 
    while f > n and num[n] == num[f]:
        f = f - 1
        n = n + 1
    if num[n] == num[f]:
        return True
    else:
        return False
            
    


def invert_num(num):
    n_invert = ""
    pos = len(num)  -1

    for i in range(pos, -1, -1):

        n_invert += str(num[i])

    return n_invert



def is_primo(numero):
    contador = 0
    for n in range(1, int(numero) + 1):
        if int(numero) % n == 0:
            contador += 1
    if contador == 2:
        return True     # é primo
    else:
        return False    # nao é primo
    
  

def find_emirp(numero):
    n_qtd = 0
    n_maior = 0
    n_soma = 0
    n_ini = 3
    n_fim = numero
    for i in range(n_ini, n_fim):

        if is_primo(i):
            n_invert =  invert_num(i)
            if is_primo(n_invert):
                if i > 11 and not(is_palindrono(str(n_invert))):
                    n_qtd += 1
                    if n_invert > n_maior:
                        n_maior = n_invert
                    n_soma += n_invert
            
    return[n_qtd, n_maior, n_soma]

