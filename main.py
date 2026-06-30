from funcoes import func_crud
import json

arquivo = 'estoque.json'

if not func_crud.abrir_arquivo(arquivo):
    func_crud.criar_arquivo(arquivo)
    

    
    
func_crud.cabecalho('Eletronicos full')
print('[1] - Cliente')
print('[2] - Administrador')
user = int(input('Selecione as opçoes acima[Enter sair]: '))
if user == 1:
    func_crud.cliente_compras(arquivo, 'Eletronicos full')
elif user == 2:
    func_crud.menu_opcoes(arquivo, 'Eletronicos full')
