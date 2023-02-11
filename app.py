from requests import get
from os import system

consultarCepTitulo = "         CONSULTAR CEP\nOBS: Digite somente os números do CEP. Lembre-se que todo CEP tem 8 dígitos"
consultarCepMsgErro = "ERRO! Digite um CEP válido"

def ConsultarCEP():
    while True:
        system('cls')
        print(consultarCepTitulo)
        CEP = str(input('Digite seu CEP: ')).strip()

        try:
            request = get(f'https://cep.awesomeapi.com.br/json/{CEP}').json()
        except:
            print(consultarCepMsgErro)
            input("Pressione ENTER para continuar...")
        finally:
            if 'status' in request:
                print(request['message'])
                input("Pressione ENTER para continuar...")
            else:
                return request
                

def mostrarDadosCEP(request: list):
    print(f'''\nCEP: {request['cep']}
Endereço: {request['address']}
Bairro: {request['district']}
Município e Estado: {request['city']} - {request['state']}
DDD do endereço: {request['ddd']}
Código de cidade do IBGE: {request['city_ibge']}\n''')


msgOpcaoInvalida = "ERRO! A opção digitada é inválida, tente novamente."

while True:
    system('cls')
    print('''        CONSULTA DE CEP\n
[ 1 ] Consultar CEP
[ 2 ] Sair''')
    while True:
        try:
            opcao = int(input('Selecione uma opção: '))
        except:
            print(msgOpcaoInvalida)
        finally:
            if opcao not in [1, 2]:
                print(msgOpcaoInvalida)
            else:
                break
    if opcao == 1:
        while True:
            cep = ConsultarCEP()
            mostrarDadosCEP(cep)
            desejaContinuar = str(input("Deseja consultar outro CEP? [S/N] ")).strip().lower()
            if desejaContinuar in "naonão":
                break

    else:
        print('Saindo...')
        exit()
