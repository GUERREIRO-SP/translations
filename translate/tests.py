from django.test import TestCase

# Create your tests here.

def count_element(n, str):
    qtd = 0

    for num in range(0, str):
        if n == num:
            qtd += 1

    return qtd


def busca_in_lista(idx, lista):
    qtd = 0

    for num in lista:
        qtd = count_element(idx, num)

    return qtd


def count_spec_digits(integers_list, digits_list):
    
    for e in digits_list:
        # for i in digits_list:
            lst_retorno = (e, 0)

            print(f"E: {e}")
            print(f"Lista: {digits_list}")

            qtd = busca_in_lista(e, integers_list)

            lst_retorno[1]= qtd
    
    return [lst_retorno]


integers_list =  [1, 1, 2 ,3 ,1 ,2 ,3 ,4]
digits_list = [1, 3]

print(count_spec_digits(integers_list, digits_list))

