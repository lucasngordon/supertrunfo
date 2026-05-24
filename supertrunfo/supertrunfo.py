#Importar bibliotecas que serão utilizadas no programa
import random
import time

#Criar uma classe animal com os atributos do Supertrunfo
class Animal:
    def __init__(self, nome, peso, velocidade, longevidade, altura):
        self.nome = nome
        self.peso = peso
        self.velocidade = velocidade
        self.longevidade = longevidade
        self.altura = altura

#Criando cartas usando a classe Animal:
leao = Animal("Leão", 190, 74, 15, 210)
elefante = Animal("Elefante", 6000, 40, 70,320)
girafa = Animal("Girafa", 1200, 60, 33, 570)
tigre = Animal("Tigre", 310, 65, 25, 310)
humano = Animal("Humano", 62, 44, 72, 170)
guepardo = Animal("Guepardo", 64, 130, 12, 150)
avestruz = Animal("Avestruz", 140, 70, 60, 280)
tartaruga = Animal("Tartaruga", 180, 0,67,136)

#Guardar os animais criados em uma lista
animais = [leao, elefante, girafa, tigre, humano, guepardo, avestruz, tartaruga]

#Criar uma função para definir o funcionamento do jogo
def jogar():
    vidasJogador = 3
    vidasComputador = 3

    while vidasComputador > 0 and vidasJogador > 0:
        cartaJogador = random.choice(animais)
        cartaComputador = random.choice(animais)
        while cartaComputador == cartaJogador:
            cartaComputador = random.choice(animais)

        print("===============================")
        print(f"Sua carta: {cartaJogador.nome}")
        atributo = input("Escolha um atributo (peso, velocidade, longevidade, altura): ").lower()

        if atributo in ["peso", "velocidade", "longevidade", "altura"]:
            time.sleep(1)
            print(f"Carta do computador: {cartaComputador.nome}")
            time.sleep(0.5)
            if getattr(cartaJogador, atributo) > getattr(cartaComputador, atributo):
                vidasComputador -= 1
                print("Você ganhou a rodada!")
            elif getattr(cartaJogador, atributo) < getattr(cartaComputador, atributo):
                vidasJogador -= 1
                print("Você perdeu a rodada!")
            else:
                print("Empate!")
        else:
             print("\nAtributo inválido. Escolha entre peso, velocidade, longevidade e altura. ")
             jogar()

        print(f"\nSuas vidas: {vidasJogador}")
        print(f"Vidas do Computador: {vidasComputador}")

        if vidasJogador == 0:
            print("\nComputador venceu!")
        elif vidasComputador == 0:
            print("\nVocê venceu!")
        else:
            print("\nPróxima rodada!")

jogar()