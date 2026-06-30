import json

def abrir_arquivo(estoque): 
    try:
        a = open(estoque, 'r')
    except:
        return False
    else:
        return True
    
def criar_arquivo(estoque):
    try:
        with open(estoque, 'w', encoding="utf-8") as arq:
            pass
        
    except Exception as error:
        print({error})

    else:
        print('Arquivo gerado com sucesso')
        
        
def cabecalho():
    print("--"*15)
    print('Eletronicos full '.center(30))
    print("--"*15)
    


def menu_opcoes(estoque, msg):
    try:
        while True:
            from time import sleep
            cabecalho()
            sleep(1)
            print("1 - Ver estoque")
            sleep(1)
            print("2 - Atualizar produto")
            sleep(1)
            print("3 - Adicionar produto")
            sleep(1)
            print("4 - Deletar produto")
            print('--'*16)
            opcao = str(input('Qual das opçoes[Enter para sair]:')).strip()
            if opcao == '':
                print('Encerrando...')
                sleep(1)
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
        print(error)
        

def ver_estoque(estoque):
    try:
        from time import sleep
        with open(estoque, 'r', encoding="utf-8")  as arq:
           estoque_produtos = json.load(arq) 
           print('-='*22)
           print(f'{"ID":<5} {"Produto":<15} {"Quantidade":<14} {"Preço":<10}')
           print('-'*44)
           for id, keys in estoque_produtos.items():
               sleep(1)
               print(f"{id:<5} {keys['nome']:<15} {keys['quantidade']:<14} R$:{keys['preço']:<10.2f}")
               
    except Exception as error:
        print(error)
    
    
def atualizar_produto(estoque):   
    try:
        from time import sleep
        with open (estoque, 'r', encoding= 'utf=8') as arq:
            estoque_produtos = json.load(arq)

            user = (str(input('Digite o produto para atualizar[ID:]:')))
            print('Proucurando...')
            sleep(1)
            if user in estoque_produtos:
                print(f'Produto selecionado: {estoque_produtos[user]['nome']}')
                
                nova_quantidade= input('Qual a nova quantidade :').strip()
                
                novo_preco = input('Qual o novo preço do item: ').strip()
                
                if nova_quantidade != '':
                    estoque_produtos[user]['quantidade'] = int(nova_quantidade)
                    
                if novo_preco != '':
                    estoque_produtos[user]['preço'] = int(novo_preco)

                with open (estoque,'w', encoding='utf= 8') as arq:
                    json.dump(estoque_produtos, arq, indent= 4, ensure_ascii= False)
                
                print('Atualiazando...')
                sleep(1)
                print(f'{estoque_produtos[user]['nome']} atualizado com sucesso')
            else:
                print('Produto não encontrado!')    
                
    except Exception as error:
        print(error)


def adicionar_produto(estoque):
    try:
        from time import sleep
        with open(estoque, 'r', encoding="utf-8") as arq:
            estoque_produto = json.load(arq)
            
            user = str(input('Deseja adicionar qual produto:')).strip().capitalize()
            if user == '':
                print("Invalido!")
                return
            for linha in estoque_produto.values():
                    if linha["nome"] == user:
                        print(f'{user} ja existe!')
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
                print(f'{user} adicionado com sucesso!')

    except Exception as error:
        print(error)


def deletar_produto(estoque):
    try:
        from time import sleep
        with open(estoque, 'r', encoding="utf=8") as arq:
            estoque_produto = json.load(arq)
            user = str(input('Qual produto deseja excluir do estoque[ID]:')).strip()
            if user in estoque_produto:
                print(f'Produto encontrado: {estoque_produto[user]["nome"]}')
                print("Excluindo o produto...")
                del estoque_produto[user]
                sleep(3)
                print("Excluido com sucesso!")
                with open(estoque, 'w', encoding="utf=8") as arq:
                    json.dump(estoque_produto, arq, indent= 4, ensure_ascii=False)
                
            else:
                print("Produto não encontrado\nTente novamente!")    
                return
            
    except Exception as error:
        print(error)

