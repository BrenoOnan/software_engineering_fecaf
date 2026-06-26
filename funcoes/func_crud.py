
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
            print("2 - Alterar produto")
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
                alterar_produto(estoque)
            elif opcao == '3':
                adicionar_produto(estoque)
            elif opcao == '4':
                deletar_produto(estoque)
            else:
                print('Opção invalida!')  
    except Exception as error:
        print(error)
        

def ver_estoque(estoque):
    
    
    
def alterar_produto(estoque):   



def adicionar_produto(estoque):


def deletar_produto(estoque):