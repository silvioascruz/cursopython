print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 29

chute_str = input("Digite o seu número: ")
print("Você digitou: ", chute_str)
chute = int(chute_str)

if(numero_secreto != chute):
    print("Você errou!")
else:
    print("Você acertou!")

print("Fim do jogo")