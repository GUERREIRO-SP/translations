############################################################################################################
import os
import requests                     #.....   pip  install  requests
from requests import status_codes   

def down_file(url, file_name):
    resposta = requests.get(url)
    if resposta.status_code == requests.codes.OK:
        with open(file_name, "wb") as new_file:
            new_file.write(resposta.content)

        print("Download finalizado. Salvo em: {}".format(file_name))
    else:
        resposta.raise_for_status()


######  ..... Chamada da rotina .....
# base_url = "https://images.squarespace-cdn.com/content/v1/60c197ab5eb995242801216c/e0c69f02-5555-47a5-9aca-b8e1cb293405/WBG-Asset+3%407x.png?format=1500w"
# endereco = "\translations\export"
# file_name = os.path.join(endereco, os.path.basename())      # basename() - Cria o arquivo com o mesmo nome de origem...
# down_file(base_url, file_name)

############################################################################################################

import os
import wget                     #.....   pip  install  wget

link = "https://images.squarespace-cdn.com/content/v1/60c197ab5eb995242801216c/e0c69f02-5555-47a5-9aca-b8e1cb293405/WBG-Asset+3%407x.png?format=1500w"
endereco = "\translations\export"
file_name = os.path.join(endereco, os.path.basename())      # basename() - Cria o arquivo com o mesmo nome de origem...

wget.download(link, file_name)

############################################################################################################
