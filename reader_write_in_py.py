import json
import webbrowser as wb

### Codigo exclusivo para as pastas de 1000 projetos.
### 
###

github = 'https://github.com/'

class js_manipul():

    def _openJson(self):
        with open(str(self), encoding='utf-8') as jsonInConverssing:
            jsonConverted = json.load(jsonInConverssing)
            return jsonConverted

    def _readJson(self):
        contador = 0
        for objeto in list(self):
            print(f'\033[33;1m{contador + 1}'
                  f'\033[32m[{str(objeto["repo_name"]).upper()}]\033[34m\n'
                  f'[{objeto["description"]}]\033[37m;\n')
            contador += 1
            acess = str(input("Deseja acessar a pagina deste projeto? ['s'|'n'|'sair']"))

            if acess == 's':
                link = github + objeto['full_name']
                wb.open(link)
                continue

            elif acess == 'sair':
                print('Saindo.')
                break

            elif acess == 'n':
                continue

            else:
                print('\033[31mERRO_DO_COMANDO!')
                return 0

# ____Local de execução_____
if __name__ == '__main__':
    endereço = str(input('Diga o caminho do arquivo json:\n'))
    abertura = js_manipul._openJson(endereço)
    js_manipul._readJson(abertura)
