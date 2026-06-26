from funcoes import func_crud
import json

arquivo = 'estoque.json'

if not func_crud.abrir_arquivo(arquivo):
    func_crud.criar_arquivo(arquivo)
    

    
    
    
func_crud.menu_opcoes(arquivo, 'Eletronicos full')