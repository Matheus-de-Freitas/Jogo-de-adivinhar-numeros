import random

from sys import float_repr_style

print("Digite o seu nome: " , end="")

nome = input()

print("\nOlá" , nome , "! Seja bem-vindo ao Desafio dos Números")

opcao = 0
pontuacao = 0
partida = 0

while opcao != '4':

    print("\nMenu: ")
    print("\n1 - Fácil")
    print("2 - Médio")
    print("3 - Difícil")
    print("4 - Sair")

    print("\nDigite o número da sua opção: " , end="")

    opcao = input()

    while opcao !='1' and opcao !='2' and opcao !='3' and opcao !='4':

        print("\nA opção digitada não existe")
        print("Digite novamente: ", end="")
        opcao = float(input())

        if opcao == '1':

            partida = partida + 1
            pontuacao = pontuacao + 10

            print("\nVou escolher um número entre 1 e 10:")
            numeroEscolhido = random.randint(1, 10)
            tentativas = 4

            print("Pronto! Já escolhi!")
            print("\nAdivinhe o número: ", end="")
            chute = int(input())

            while tentativas > 1 and chute != numeroEscolhido:

                while chute >10 or chute <1:
                    print("O número digitado não está no intervalo. Digite novamente: " , end="")
                    chute = int(input())

            else:

                tentativas = tentativas - 1
                pontuacao = pontuacao - 5

                print("\nErrou!!!")
                print("\nVocê tem", tentativas, "tentativas")

                print("Pontuação: " , pontuacao)
                print("Partida " , partida)

            if numeroEscolhido > chute:
                print("\nDica: o número é maior!")

            elif numeroEscolhido < chute:
                print("\nDica: o número é menor!")
                print("Tente novamente: " , end="")

            chute = int(input())

            if numeroEscolhido == chute:
                print("\nParabéns! Eu realmente escolhi o número", numeroEscolhido)

            else:
                print("\nPerdeu!")
                print("Pontuação: " , pontuacao)
                print("Partida " , partida)

            print('\nDeseja continuar ? ("s" para sim ou "n" para não): ' , end="")
            resp = input().lower()

            while resp != 's' and resp !='n':
                print("\nResposta inválida!")
                print("Digite novamente: " , end="")
                resp = input().lower()

            if resp == 'n':
                opcao = '4'

            elif opcao == '2':
                partida = partida + 1
                pontuacao = pontuacao + 25

            print("\nVou escolher um número entre 1 e 50:")
            numeroEscolhido = random.randint(1, 50)
            tentativas = 6

            print("Pronto! Já escolhi!")
            print("\nAdivinhe o número: ", end="")

            chute = int(input())

            while tentativas > 1 and chute != numeroEscolhido:

                while chute > 50 or chute < 1:
                    print("O número digitado não está no intervalo. Digite novamente: " , end="")

                chute = int(input())

            else:

                tentativas = tentativas - 1
                pontuacao = pontuacao - 5

            print("\nErrou!!!")
            print("\nVocê tem", tentativas, "tentativas")
            print("Pontuação: " , pontuacao)
            print("Partida " , partida)

            if numeroEscolhido > chute:

                print("\nDica: o número é maior!")

            elif numeroEscolhido < chute:

                print("\nDica: o número é menor!")
                print("Tente novamente: " , end="")

            chute = int(input())

            if numeroEscolhido == chute:

                print("\nParabéns! Eu realmente escolhi o número", numeroEscolhido)

            else:

                print("\nPerdeu!")
                print("Pontuação: " , pontuacao)
                print("Partida " , partida)

            print('\nDeseja continuar ? ("s" para sim ou "n" para não): ' , end="")
            resp= input().lower()

            while resp != 's' and resp !='n':
                print("\nResposta inválida!")
                print("Digite novamente: " , end="")
                resp = input().lower()

        if resp == 'n':
            opcao = '4'

        elif opcao == '3':
            partida = partida + 1
            pontuacao = pontuacao + 50

            print("\nVou escolher um número entre 1 e 100:")
            numeroEscolhido = random.randint(1, 100)
            tentativas = 7

            print("Pronto! Já escolhi!")
            print("\nAdivinhe o número: ", end="")
            chute = int(input())

        while tentativas > 1 and chute != numeroEscolhido:

            while chute >100 or chute <1:
                print("O número digitado não está no intervalo. Digite novamente: " , end="")

            chute = int(input())

        else:
            tentativas = tentativas - 1
            pontuacao = pontuacao - 5
            
            print("\nErrou!!!")
            print("\nVocê tem", tentativas, "tentativas")
            print("Pontuação: " , pontuacao)
            print("Partida " , partida)

        if numeroEscolhido > chute:
            print("\nDica: o número é maior!")

        elif numeroEscolhido < chute:
            print("\nDica: o número é menor!")
            print("Tente novamente: " , end="")

        chute = int(input())

        if numeroEscolhido == chute:
            print("\nParabéns! Eu realmente escolhi o número", numeroEscolhido)

        else:
            print("\nPerdeu!")
            print("Pontuação: " , pontuacao)
            print("Partida " , partida)

        print('\nDeseja continuar ? ("s" para sim ou "n" para não): ' , end="")
        resp= input().lower()

        while resp != 's' and resp !='n':
            print("\nResposta inválida!")
            print("Digite novamente: " , end="")
        resp = input().lower()

        if resp == 'n':
            opcao = '4'

despedida = random.randint(1, 4)

if despedida == 1:
    print("\nAdeus nobre guerreiro!")

elif despedida == 2:
    print("\nSagas sobre seus feitos serão cantadas por muitas eras" , nome)

elif despedida == 3:
    print("\nHasta la vista" , nome)

elif despedida == 4:
    print("\nFalô" , nome)