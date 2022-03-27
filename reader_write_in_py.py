import json
import requests as req
import webbrowser as wb


github = 'https://github.com/'

## O arquivo ser� lido at� o fim, com opç�o de ir e seguir o c�digo.
##

def archive_read_and_request(arquivo):

    with open(arquivo, encoding='utf-8') as DeepLearning:
        dados = json.load(DeepLearning)

    contador = 0
    for objeto in dados:
        print(f'\033[33;1;4m[{contador+1}]'
              f'\033[32;0m[{str(objeto["repo_name"]).upper()}]\033[34m\n'
              f'[{objeto["description"]}]\033[37m;\n')

        contador += 1
        acesso = str(input('\033[35mGostaria de acessar o link deste projeto?[s/n/sair]'))

        if acesso == 's':
            link = github + objeto['full_name']
            wb.open(link)
        elif acesso == 'sair':
            break
        elif acesso == 'n':
            continue
        else:
            print('\033[31mErro')
            return 0

# ____Local de execução_____
if __name__ == '__main__':
    endereço = str(input('Diga o caminho do arquivo json.'))
    archive_read_and_request(endereço)
