from Classe_Compra import *
from Classe_Venda import Venda


class Menu:
    def __init__(self):
        estoque_prod = Estoque()
        compra = Compra()
        venda = Venda()

        venda.entrada = estoque_prod
        compra.entrada = estoque_prod

        ##iniciar menu
        while True:
            print('Menu de operações'
                  '\n1 - Cadastrar'
                  '\n2 - Listar todos'
                  '\n3 - Procurar produto'
                  '\n4 - Alterar produto'
                  '\n5 - Entrada de Produtos'
                  '\n6 - Saida de Produtos'
                  '\n0 - Sair')
            entrada = input('Informe a operação desejada: ')

            if entrada == '1':
                estoque_prod.salvar_cadastro()
            elif entrada == '2':
                estoque_prod.lista_produtos()
            elif entrada == '3':
                estoque_prod.lista_codp()
            elif entrada == '4':
                estoque_prod.alterar_nome()
            elif entrada == '5':
                compra.comprar()
            elif entrada == '6':
                venda.vender()
            elif entrada == '0':
                break
            else:
                print('opção errada!')