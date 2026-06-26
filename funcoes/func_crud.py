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
        
        
def cabecalho(msg):
    print("--" *len(msg))
    print(msg.center (len(msg)* 2))
    print("--" * len(msg))
    


def menu_opcoes(estoque, msg):
    try:
        while True:
            from time import sleep
            cabecalho(msg)
            print("1 - Ver estoque")
            print("2 - Atualizar produto")
            print("3 - Adicionar produto")
            print("4 - Deletar produto")
            print('--'*16)
            opcao = str(input('Qual das opçoes[enter para sair]:')).strip()
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
        ver_estoque(estoque)
        from time import sleep
        with open (estoque, 'r', encoding= 'utf=8') as arq:
            estoque_produtos = json.load(arq)

            user = (str(input('Digite o produto a atualizar[ID:]:')))
            print('Proucurando...')
            sleep(1)
            if user in estoque_produtos:
                print(f'Produto selecionado: {estoque_produtos[user]['nome']}')
                
                nova_quantidade= input('Qual a nova quantidade do item:').strip()
                
                novo_preco = input('Qual o novo preço do item: ').strip()
                
                if nova_quantidade != '':
                    estoque_produtos[user]['quantidade'] = int(nova_quantidade)
                    
                if novo_preco != '':
                    estoque_produtos[user]['preço'] = int(novo_preco)

                with open (estoque,'w', encoding='utf= 8') as arq:
                    json.dump(estoque_produtos, arq, indent= 4, ensure_ascii= False)
                
                print(f'{estoque_produtos[user]['nome']} atualizado com sucesso')
            else:
                print('Produto não encontrado!')    
    except Exception as error:
        print(error)


def adicionar_produto(estoque):
    print()


def deletar_produto(estoque):
    print()