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

    #Sorteia as cartas
    while vidasComputador > 0 and vidasJogador > 0:
        cartaJogador = random.choice(animais)
        cartaComputador = random.choice(animais)
        while cartaComputador == cartaJogador:
            cartaComputador = random.choice(animais)


        while True:
            print("===============================")
            print(f"Sua carta: {cartaJogador.nome.upper()}")
            atributo = input("Escolha um atributo (peso, velocidade, longevidade, altura): ").strip().lower()

            if atributo in ["peso", "velocidade", "longevidade", "altura"]:
                break
            else:
                print("\nAtributo inválido. Escolha entre peso, velocidade, longevidade e altura.")
         
        val_jogador = getattr(cartaJogador, atributo)
        val_computador = getattr(cartaComputador, atributo)
        
        print(f"\nComputador revelando...")
        time.sleep(1)
        print(f"CARTA DO COMPUTADOR: {cartaComputador.nome} ({atributo}: {val_computador})")
        time.sleep(0.5)
        
        # Lógica de vitória
        if val_jogador > val_computador:
            vidasComputador -= 1
            print("Você ganhou a rodada!")
        elif val_jogador < val_computador:
            vidasJogador -= 1
            print("Você perdeu a rodada!")
        else:
            print("Empate!")

        print(f"\nPLACAR: Jogador {vidasJogador} x {vidasComputador} Computador")

        if vidasJogador == 0:
            print("\nComputador venceu!")
        elif vidasComputador == 0:
            print("\nVocê venceu!")
        else:
            print("\nPróxima rodada!")

jogar()