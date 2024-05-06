import os
import random

def exibir_nome_do_programa():
    print('-----------------------------------------------------------------------------------------------------------')
    print("""
░█████╗░██████╗░░█████╗░░██████╗████████╗░█████╗░░██████╗  ███████╗░░███╗░░  ██╗░░░░░██╗░██████╗░░█████╗░
██╔══██╗██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔════╝  ██╔════╝░████║░░  ██║░░░░░██║██╔════╝░██╔══██╗
███████║██████╔╝██║░░██║╚█████╗░░░░██║░░░███████║╚█████╗░  █████╗░░██╔██║░░  ██║░░░░░██║██║░░██╗░███████║
██╔══██║██╔═══╝░██║░░██║░╚═══██╗░░░██║░░░██╔══██║░╚═══██╗  ██╔══╝░░╚═╝██║░░  ██║░░░░░██║██║░░╚██╗██╔══██║
██║░░██║██║░░░░░╚█████╔╝██████╔╝░░░██║░░░██║░░██║██████╔╝  ██║░░░░░███████╗  ███████╗██║╚██████╔╝██║░░██║
╚═╝░░╚═╝╚═╝░░░░░░╚════╝░╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░  ╚═╝░░░░░╚══════╝  ╚══════╝╚═╝░╚═════╝░╚═╝░░╚═╝
""")
    print('-----------------------------------------------------------------------------------------------------------')

def exibir_opcao():
    print('1. Fazer aposta')
    print('2. Limpa a tela')
    print('3. Sair\n')

def limpa_tela():
    os.system('cls')
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def finalizar_app():
    os.system('cls')
    print('Finalizar a aplicativo...')

def opcao_invalida():
    os.system('cls')
    print('Opcao invalida!')
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def fazer_aposta():
    
    # Gera numero aleatorio: 
    numeros_aleatorios = random.sample(range(1, 100), 10)

    numeros_armazenados = numeros_aleatorios[:]
    
    # Pede os valores
    numeros_verificar = []
    for i in range(5):
        numero = int(input("\nInforme numero a ser apostado: "))
        numeros_verificar.append(numero)

    print('\n------------------------------------------------')

    # Mostra os valores
    print("Números de aposta:", end=" ")
    for numero in numeros_aleatorios:
        print(numero, end=" ")
    

    print('\n------------------------------------------------')
    
    # Verifica os numeros
    for numero in numeros_verificar:
        if numero in numeros_aleatorios:
            print(f"\nO número {numero} está presente.")
            pontos = numeros_aleatorios.count(numero) 
        else:
            print(f"\nO número {numero} não está presente na lista.")

    try:
        if pontos == 5:
            print('\nParabéns acertou os 5 numeros, valor total de 20 mil de reais !!!')
        elif pontos == 4:
            print('\nParabéns acertou os 4 numeros, valor total de 8 mil de reais !!!')
        elif pontos == 3:
            print('\nParabéns acertou os 3 numeros, valor total de 6 mil de reais !!')
        elif pontos == 2:
            print('\nParabéns acertou os 2 numeros, valor total de 4 mil de reais !')
        elif pontos == 1:
            print('\nParabéns acertou os 1 numeros, valor total de 2 mil de reais ')
    except:
        print('\nNao foi dessa vez...')

    print('\n------------------------------------------------')
    exibir_opcao()
    escolher_opcao()

try:
    def escolher_opcao():
        opcao_escolhida = int(input('Escolha a opcao: '))
        if opcao_escolhida == 1:
            fazer_aposta()
        elif opcao_escolhida == 2:
            limpa_tela()
        elif opcao_escolhida == 3:
            finalizar_app()
        else:
            opcao_invalida()
except:
    opcao_invalida()

def main():
    exibir_nome_do_programa()
    exibir_opcao()
    escolher_opcao()

if __name__ == '__main__':
    main()
