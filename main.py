from rich import print
from funcoes import func_crud
import json
from time import sleep

arquivo = 'estoque.json'

if not func_crud.abrir_arquivo(arquivo): #se não existir o arquivo
    func_crud.criar_arquivo(arquivo) #criar arquivo


while True:
    func_crud.cabecalho() #chama o cabeçalho
    print('[1] - Cliente') #sessão cliente
    print('[2] - Administrador')#sessão administrador
    user = str(input('Selecione as opçoes acima[Enter sair]: '))
    if user == '':
        print('Encerrando...'), sleep(1)
        break
    elif user == '1':
        func_crud.cliente_compras(arquivo) #abrindo sessão cliente
        print('Encerrando...'), sleep(1)
        break
    elif user == '2':
        senha = int(input('Qual a senha: '))
        func_crud.senha_adm(senha, arquivo) #abrindo sessão administrador
        print('Encerrando...'), sleep(1)
        break
    else:
        print('Opção inválida')
        