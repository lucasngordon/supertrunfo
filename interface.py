import random
import tkinter as tk
from tkinter import messagebox

class Animal:
    def __init__(self, nome, peso, velocidade, longevidade, altura, emoji):
        self.nome = nome
        self.peso = peso
        self.velocidade = velocidade
        self.longevidade = longevidade
        self.altura = altura
        self.emoji = emoji

# Criando o baralho de cartas
animais = [
    Animal("Leão", 190, 74, 15, 210, "🦁"),
    Animal("Elefante", 6000, 40, 70, 320, "🐘"),
    Animal("Girafa", 1200, 60, 33, 570, "🦒"),
    Animal("Tigre", 310, 65, 25, 310, "🐯"),
    Animal("Humano", 62, 44, 72, 170, "🙋‍♂️"),
    Animal("Guepardo", 64, 130, 12, 150, "🐆"),
    Animal("Avestruz", 140, 70, 60, 280, "🐦"),
    Animal("Tartaruga", 180, 0, 67, 136, "🐢")
]

class SuperTrunfoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Super Trunfo Animal 🦁")
        self.root.geometry("450x550")
        self.root.configure(bg="#f0f4f8")

        # Inicializando variáveis do jogo
        self.vidas_jogador = 3
        self.vidas_computador = 3
        self.cartaJogador = None
        self.cartaComputador = None

        self.criar_interface()
        self.nova_rodada()

    def criar_interface(self):
        # --- PLACAR ---
        self.lbl_placar = tk.Label(
            self.root, 
            text=f"Jogador: {self.vidas_jogador}  |  Computador: {self.vidas_computador}", 
            font=("Arial", 14, "bold"), bg="#334e68", fg="white", pady=10
        )
        self.lbl_placar.pack(fill="x")

        # --- ÁREA DA CARTA DO JOGADOR ---
        self.frame_carta = tk.LabelFrame(
            self.root, text=" SUA CARTA ", font=("Arial", 12, "bold"), 
            bg="white", bd=2, relief="groove", padx=15, pady=15
        )
        self.frame_carta.pack(padx=20, pady=20, fill="x")

        self.lbl_nome_animal = tk.Label(self.frame_carta, text="", font=("Arial", 18, "bold"), bg="white", fg="#243b53")
        self.lbl_nome_animal.pack(pady=5)

        # Labels para mostrar os atributos da carta atual
        self.lbl_peso = tk.Label(self.frame_carta, text="", font=("Arial", 11), bg="white")
        self.lbl_peso.pack(anchor="w")
        self.lbl_vel = tk.Label(self.frame_carta, text="", font=("Arial", 11), bg="white")
        self.lbl_vel.pack(anchor="w")
        self.lbl_long = tk.Label(self.frame_carta, text="", font=("Arial", 11), bg="white")
        self.lbl_long.pack(anchor="w")
        self.lbl_alt = tk.Label(self.frame_carta, text="", font=("Arial", 11), bg="white")
        self.lbl_alt.pack(anchor="w")

        # --- BOTÕES DE ATRIBUTOS ---
        self.frame_botoes = tk.LabelFrame(self.root, text=" Escolha um Atributo para Duelar ", bg="#f0f4f8")
        self.frame_botoes.pack(padx=20, pady=10, fill="x")

        # Criando botões estilizados
        btn_configs = {"font": ("Arial", 11, "bold"), "bg": "#627d98", "fg": "white", "activebackground": "#486581", "pady": 5}
        
        tk.Button(self.frame_botoes, text="Peso (kg)", command=lambda: self.comparar("peso"), **btn_configs).pack(fill="x", pady=2)
        tk.Button(self.frame_botoes, text="Velocidade (km/h)", command=lambda: self.comparar("velocidade"), **btn_configs).pack(fill="x", pady=2)
        tk.Button(self.frame_botoes, text="Longevidade (anos)", command=lambda: self.comparar("longevidade"), **btn_configs).pack(fill="x", pady=2)
        tk.Button(self.frame_botoes, text="Altura (cm)", command=lambda: self.comparar("altura"), **btn_configs).pack(fill="x", pady=2)

        # --- ÁREA DE RESULTADO ---
        self.lbl_resultado = tk.Label(self.root, text="Escolha um atributo acima!", font=("Arial", 12, "italic"), bg="#f0f4f8", fg="#486581", pady=10)
        self.lbl_resultado.pack()

    def nova_rodada(self):
        # Sorteia as cartas sem repetição
        self.cartaJogador = random.choice(animais)
        opcoes_comp = [a for a in animais if a != self.cartaJogador]
        self.cartaComputador = random.choice(opcoes_comp)

        # Atualiza o texto da interface com os dados da nova carta do jogador
        self.lbl_nome_animal.config(text=f"{self.cartaJogador.emoji} {self.cartaJogador.nome.upper()}")
        self.lbl_peso.config(text=f"Peso: {self.cartaJogador.peso} kg")
        self.lbl_vel.config(text=f"Velocidade: {self.cartaJogador.velocidade} km/h")
        self.lbl_long.config(text=f"Longevidade: {self.cartaJogador.longevidade} anos")
        self.lbl_alt.config(text=f"Altura: {self.cartaJogador.altura} cm")
        
        self.lbl_resultado.config(text="Sua vez! Escolha um atributo.", fg="#486581")

    def comparar(self, atributo):
        val_jogador = getattr(self.cartaJogador, atributo)
        val_computador = getattr(self.cartaComputador, atributo)

        texto_comp = f"Computador tinha: {self.cartaComputador.nome} ({val_computador})"

        # Lógica de vitória
        if val_jogador > val_computador:
            self.vidas_computador -= 1
            resultado_texto = f"Você ganhou! {texto_comp}"
            cor_resultado = "green"
        elif val_jogador < val_computador:
            self.vidas_jogador -= 1
            resultado_texto = f"Você perdeu! {texto_comp}"
            cor_resultado = "red"
        else:
            resultado_texto = f"Empate! {texto_comp}"
            cor_resultado = "orange"

        # Atualiza a tela com o resultado e o novo placar
        self.lbl_resultado.config(text=resultado_texto, fg=cor_resultado)
        self.lbl_placar.config(text=f"Jogador: {self.vidas_jogador}  |  Computador: {self.vidas_computador}")

        # Verifica se o jogo acabou
        if self.vidas_jogador == 0:
            messagebox.showinfo("Fim de Jogo", "Fim de jogo! O computador venceu.")
            self.reiniciar_jogo()
        elif self.vidas_computador == 0:
            messagebox.showinfo("Fim de Jogo", "Parabéns! Você foi o grande vencedor!")
            self.reiniciar_jogo()
        else:
            self.root.after(3000, self.nova_rodada)

    def reiniciar_jogo(self):
        self.vidas_jogador = 3
        self.vidas_computador = 3
        self.lbl_placar.config(text=f"Jogador: {self.vidas_jogador}  |  Computador: {self.vidas_computador}")
        self.nova_rodada()


if __name__ == "__main__":
    janela = tk.Tk()
    app = SuperTrunfoApp(janela)
    janela.mainloop()