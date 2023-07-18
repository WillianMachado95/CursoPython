
import random

'''
Criação de uma tupla
'''
jogadas = ("pedra", "papel", "tesoura")


player1 = input("Player 1: Digite sua escolha: ")

'''
Validação da jogada do player 1 se está dentro da tupla
'''
if player1 not in jogadas:
    print("Opção Inválida")
    player1 = input("Player 1: Digite sua escolha: ")

'''
Deixando a jogada do player 2 automática e randomica
'''
player2 = jogadas[random.randint(0,2)]

if player1 == player2:
    print("Empate!")
elif player1 == "pedra":
    if player2 == "papel":
        print(f"computador jogou {player2}, você perdeu!")
    if player2 == "tesoura":
        print(f"computador jogou {player2}, você ganhou!")
elif player1 == "papel":
    if player2 == "pedra":
        print(f"computador jogou {player2}, você ganhou!")
    if player2 == "tesoura":
        print(f"computador jogou {player2}, você perdeu!")
elif player1 == "tesoura":
    if player2 == "papel":
        print(f"computador jogou {player2}, você ganhou!")
    if player2 == "pedra":
        print(f"computador jogou {player2}, você perdeu!")
else:
    print("Opção inválida")







'''
if (player1 == "pedra" and player2 == "tesoura") or (player1 == "papel" and player2 == "pedra") or (player1 == "tesoura" and player2 == "papel"):
    print ("Player 1 é o vencedor")
elif (player1 == "pedra" and player2 == "papel") or (player1 == "papel" and player2 == "tesoura")  or (player1 == "tesoura" and player2 == "pedra"):
    print ("player 2 é o vencedor")
else:
    print ("Empate")
'''


''''
if player1 == "pedra" and player2 == "tesoura":
    print ("Player 1 é o vencedor")
elif player1 == "pedra" and player2 == "papel":
    print ("Player 2 é o vencedor")
elif player1 == "papel" and player2 == "pedra":
    print ("player 1 é o vencedor")
elif player1 == "papel" and player2 == "tesoura":
    print ("player 2 é o vencedor")
elif player1 == "tesoura" and player2 == "pedra":
    print ("player 2 é o vencedor")
elif player1 == "tesoura" and player2 == "papel":
    print ("player 1 é o vencedor")
else: 
    print("Empate")

'''




