from rich import print
import json

def abrir_arquivo(estoque): #verifica se existe o arquivo e tenta abrir 
    try:
        a = open(estoque, 'r')
    except:
        return False
    else:
        return True
    
def criar_arquivo(estoque): #cria o arquivo caso não haja arquivo
    try:
        with open(estoque, 'w', encoding="utf-8") as arq:
            pass
        
    except Exception as error:
        print(f'{error} ❌')
    else:
        print('Arquivo gerado com sucesso')
        

def cabecalho(): #cabeçalho da loja#
    print("--"*19)
    print('[blue]Eletronicos full[/]'.center(45))
    print("--"*19)
    

def validar_senha_adm(password): # função de validação da senha#
    return password == 123

def senha_adm(password, estoque): # verfica a senha 
    
    if validar_senha_adm(password):
        menu_opcoes(estoque)
    else:
        print('Senha inválida!')

def menu_opcoes(estoque): #função para abrir o menu de opçoes
    try:
        while True:
            from time import sleep
            cabecalho(), sleep(1)
            print("1 - Ver estoque"), sleep(1)
            print("2 - Atualizar produto"), sleep(1)
            print("3 - Adicionar produto"), sleep(1)
            print("4 - Deletar produto"), sleep(1)
            print('--'*16)
            opcao = str(input('Qual das opçoes[Enter para sair]:')).strip()
            if opcao == '':
                break
            elif opcao == '1':
                ver_estoque(estoque)
            elif opcao == '2':
                atualizar_produto(estoque)
            elif opcao == '3':
                adicionar_produto(estoque)
            elif opcao == '4':
                deletar_produto(estoque)
            else:
                print('Opção invalida!')  
                
    except Exception as error:
        print(f'{error} ❌')
        

def ver_estoque(estoque): #função para printar o estoque de forma tabular 
    try:
        from time import sleep
        with open(estoque, 'r', encoding="utf-8")  as arq:
           estoque_produtos = json.load(arq) 
           print('-'*49)
           print(f'{"ID":<5} {"Produto":<15} {"Quantidade":<14} {"Preço":<10}')
           print('-'*49)
           
           for id, keys in estoque_produtos.items():
               sleep(1)
               print(f"{id:<5} {keys['nome']:<15} {keys['quantidade']:<13} R$:{keys['preço']:<10.2f}")
               
    except Exception as error:
        print(f'{error} ❌')
    
    
def atualizar_produto(estoque): #função para atualizar o produto do estoque
    try:
        from time import sleep
        with open (estoque, 'r', encoding= 'utf=8') as arq:
            estoque_produtos = json.load(arq)

            user = (str(input('Digite o produto para atualizar[ID:]:'))).strip()
            print('Proucurando...'), sleep(1)
            
            if user in estoque_produtos:
                print(f'Produto selecionado: [blue]{estoque_produtos[user]['nome']}[/]')
                
                nova_quantidade= input('Qual a nova quantidade: ').strip()
                novo_preco = input('Qual o novo preço do item R$: ').strip()
                
                if nova_quantidade != '': #converte para int
                    estoque_produtos[user]['quantidade'] += int(nova_quantidade)
                    
                if novo_preco != '': #converte para int
                    estoque_produtos[user]['preço'] = int(novo_preco)

                with open (estoque,'w', encoding='utf= 8') as arq:
                    json.dump(estoque_produtos, arq, indent= 4, ensure_ascii= False)
                
                print('Atualiazando...'), sleep(1)
                print(f'[blue]{estoque_produtos[user]['nome']}[/] atualizado com sucesso')
            else:
                print('Produto não encontrado!')    
                
    except Exception as error:
        print(f'{error} ❌')


def adicionar_produto(estoque): #função para adicionar novo produto
    try:
        from time import sleep
        with open(estoque, 'r', encoding="utf-8") as arq:
            estoque_produto = json.load(arq)
            
            user = str(input('Deseja adicionar qual produto:')).strip().capitalize()
            if user == '':
                print("Invalido!")
                return
            
            for linha in estoque_produto.values(): #verifica se existe o produto no estoque
                    if linha["nome"] == user:
                        print(f'[blue]{user}[/] ja existe!')
                        return
            else:
                add_quantidade = int(input("Qual a quantidade a entrar em estoque:"))
                add_preco = int(input('Qual o valor do item R$: '))
                novo_id = str(len(estoque_produto)+ 1)
                
                estoque_produto[novo_id] = { 
                                            "nome": user,
                                            "quantidade": add_quantidade,
                                            "preço": add_preco
            }
                with open(estoque, 'w', encoding= "utf=8") as arq:
                    json.dump(estoque_produto, arq, indent= 4, ensure_ascii= False)
                print(f'[blue]{user}[/] adicionado com sucesso!')

    except Exception as error:
        print(f'{error} ❌')


def deletar_produto(estoque): #função para encontrar deletar produto do estoque 
    try:
        from time import sleep
        with open(estoque, 'r', encoding="utf=8") as arq:
            estoque_produto = json.load(arq)
            id_user = str(input('Qual produto deseja excluir do estoque[ID]:')).strip()
            if id_user in estoque_produto:
                print(f'Produto encontrado: [blue]{estoque_produto[id_user]["nome"]}[/]')
                print("Excluindo o produto...")
                del estoque_produto[id_user]
                sleep(2)
                print(f"Excluido com sucesso ✅")
                with open(estoque, 'w', encoding="utf=8") as arq:
                    json.dump(estoque_produto, arq, indent= 4, ensure_ascii=False)
                
            else:
                print("Produto não encontrado\nTente novamente!")    
                return
            
    except Exception as error:
        print(f'{error} ❌')

def cliente_compras(estoque): #função cliente, comprar produtos
    while True:
        try:
            from time import sleep
            ver_estoque(estoque), print()
            with open(estoque, 'r', encoding='utf=8') as arq:
                estoque_produtos = json.load(arq)
                
                produto_comprar = str(input('Qual produto deseja comprar[ID]: ')).strip()
                
                if produto_comprar == '':
                    break
                
                if produto_comprar in estoque_produtos:
                    print(f"[blue]{estoque_produtos[produto_comprar]['nome']}[/] selecionado ✅")
                    
                    quantidade = int(input('Selecione a quantidade:'))
                    if quantidade < estoque_produtos[produto_comprar]['quantidade']:
                        
                        valor = estoque_produtos[produto_comprar]['preço'] * quantidade
                        estoque_produtos[produto_comprar]['quantidade'] += - quantidade
                        
                        print(f'Valor da compra R$:{valor:.2f}')
                        print(f'Confirmando a compra...'), sleep(2)
                        print(f'Compra efetuada✅\nVolte sempre')
                        with open (estoque, 'w', encoding='utf=8') as arq:
                            json.dump(estoque_produtos, arq, indent=4, ensure_ascii=False)
                        break
                        
                    else:
                        print('Não temos essa quantidade em estoque\nTente novamente!')
                else:
                    print('Produto não encontrado ❌, tente novamente')
                                    
            
        except Exception as error:
            print(f'{error} ❌')