
def main():
    dicionario = {"nome": "Nivaldo"}

    print(dicionario)
    mudar(dicionario)
    print(dicionario)
    

def mudar(dict_1):
    dict_1["nome"] = "Rafael" 


if __name__ == '__main__':
    main()


