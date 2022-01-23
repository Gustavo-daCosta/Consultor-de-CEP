import json
from requests import get
from os import system

def ConsultaCEP():
    requestExists = False
    while True:
        try:
            system('cls')
            print('         CONSULTAR CEP\n')
            print('OBS: Não precisa digitar pontuações, somente os números. Lembre-se que todo CEP tem 8 dígitos')
            CEP = str(input('Digite seu CEP: ')).strip()
            request = get(f'https://cep.awesomeapi.com.br/json/{CEP}').json()
            requestExists = True
        except:
            print('ERRO! Digite um CEP')
        finally:
            if requestExists is True:
                if 'status' in request:
                    print(request['message'])
                else:
                    print(f'''\nCEP: {request['cep']}
Endereço: {request['address']}
Bairro: {request['district']}
Município e Estado: {request['city']} - {request['state']}
DDD do endereço: {request['ddd']}
Código de cidade do IBGE: {request['city_ibge']}\n''')
                input('Pressione ENTER para continuar...')
                break
                system('cls')

while True:
    system('cls')
    print('''        CONSULTA DE CEP\n
[ 1 ] Consultar CEP
[ 2 ] Sair''')
    while True:
        try:
            opcao = int(input('Selecione uma opção: '))
        except:
            print('ERRO! Digite o número 1 ou 2.')
        finally:
            if opcao != 1 and opcao != 2:
                print('ERRO! Digite o número 1 ou 2.')
            else:
                break
    if opcao == 1:
        ConsultaCEP()
    elif opcao == 2:
        print('Saindo...')
        exit()