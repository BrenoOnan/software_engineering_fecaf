from funcoes import func_crud
import json
from time import sleep
arquivo = 'estoque.json'

if not func_crud.abrir_arquivo(arquivo):
    func_crud.criar_arquivo(arquivo)


while True:
    func_crud.cabecalho()
    print('[1] - Cliente')
    print('[2] - Administrador')
    user = str(input('Selecione as opçoes acima[Enter sair]: '))
    if user == '':
        print('Encerrando...')
        sleep(1)
        break
    elif user == '1':
        func_crud.cliente_compras(arquivo)
        print('Encerrando...')
        sleep(1)
        break
    elif user == '2':
        senha = int(input('Qual a senha: '))
        func_crud.senha_adm(senha, arquivo)
        print('Encerrando...')
        sleep(1)
        break
    else:
        print('Opção inválida')
        