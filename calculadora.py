
#Calculadora Simples.

print ("""
       
░█████╗░░█████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗░░░░░░█████╗░██████╗░░█████╗░██████╗░░█████╗░
██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║░░░██║██║░░░░░██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗
██║░░╚═╝███████║██║░░░░░██║░░╚═╝██║░░░██║██║░░░░░███████║██║░░██║██║░░██║██████╔╝███████║
██║░░██╗██╔══██║██║░░░░░██║░░██╗██║░░░██║██║░░░░░██╔══██║██║░░██║██║░░██║██╔══██╗██╔══██║
╚█████╔╝██║░░██║███████╗╚█████╔╝╚██████╔╝███████╗██║░░██║██████╔╝╚█████╔╝██║░░██║██║░░██║
░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝
       """)


#Abrir terminal (VSCode)

#PARA ABRIR O 𝑇𝐸𝑅𝑀𝐼𝑁𝐴𝐿, DIGITE: CTRL + J

#---------------------------

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
print ('Escolha uma operação')
print ('Opção 1: Adição')
print ('Opção 2: Subtração')
print ('Opção 3: Multiplicação')
print ('Opção 4: Divisão')

escolha_uma_operacao = int(input('Escolha uma opção 1/2/3/4: '))

n1 = float(input('Digite o primeiro número desejado: '))
n2 = float(input('Digite o segundo número desejado: '))

#Operações condicionais.

if escolha_uma_operacao == 1:
    print ('Resultado: ', adicao(n1, n2))
elif escolha_uma_operacao == 2:
    print ('Resultado: ', subtracao(n1,n2))
elif escolha_uma_operacao == 3:
    print ('Resultado: ', mulplicacao(n1,n2))
else:
    print ('Resultado: ', divisao(n1,n2))

#Limpar Terminal 

print('PARA LIMPAR O 𝑇𝐸𝑅𝑀𝐼𝑁𝐴𝐿, DIGITE: CTRL + L')