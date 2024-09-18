import os

#Calculadora Simples.
def exebir_nome():
    print ("""
       
░█████╗░░█████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗░░░░░░█████╗░██████╗░░█████╗░██████╗░░█████╗░
██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║░░░██║██║░░░░░██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗
██║░░╚═╝███████║██║░░░░░██║░░╚═╝██║░░░██║██║░░░░░███████║██║░░██║██║░░██║██████╔╝███████║
██║░░██╗██╔══██║██║░░░░░██║░░██╗██║░░░██║██║░░░░░██╔══██║██║░░██║██║░░██║██╔══██╗██╔══██║
╚█████╔╝██║░░██║███████╗╚█████╔╝╚██████╔╝███████╗██║░░██║██████╔╝╚█████╔╝██║░░██║██║░░██║
░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝
       """)


#Funções declaradas. Declaração de todas as operações com variáveis x e y

def adicao (x,y):
    return x + y
def  subtracao (x,y):
    return x - y
def  mulplicacao (x,y):
    return x * y
def  divisao (x,y):
    if y == 0:
        return 'Nao é possível dividir por 0'
    else:
        return x / y
    
#Escolher Opções e numeros para as operações.
def opcoes():
    print ('Escolha uma operação')
    print ('Opção 1: Adição')
    print ('Opção 2: Subtração')
    print ('Opção 3: Multiplicação')
    print ('Opção 4: Divisão')



escolha_uma_operacao = int(input('Escolha uma opção 1/2/3/4: '))

n1 = float(input('Digite o primeiro número desejado: '))
n2 = float(input('Digite o segundo número desejado: '))


def finalizar_app():
    os.system ('cls')
    print ('finalizando o app\n')


def opcao_invalida():
    print('opção Inválida\n')
    input ('Digieta uma tecla para voltar ao menu principal')
    main()



#Operações condicionais.
def operacao():
    try:
        if escolha_uma_operacao == 1:
            print ('Resultado: ', adicao(n1, n2))
        elif escolha_uma_operacao == 2:
            print ('Resultado: ', subtracao(n1,n2))
        elif escolha_uma_operacao == 3:
            print ('Resultado: ', mulplicacao(n1,n2))
        elif escolha_uma_operacao == 4:
            print ('Resultado: ', divisao(n1,n2))
        else:
            finalizar_app()
    except:
        opcao_invalida()


def main():
    os.system ('cls')
    exebir_nome()
    opcoes()
    operacao()
    

if __name__ == '__main__':
    main()
