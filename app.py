import tkinter as tk
from tkinter import Tk, Label, Button, Entry, ttk

class AppCotacao:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.configure(bg="#66b2b2")
        self.janela.geometry("800x600")

        self.janela.columnconfigure(0, weight=1)
        self.janela.columnconfigure(1, weight=1)

        self.entrada_moeda = None  # Inicializa a variável de entrada de moeda
        self.montar_tela_inicial()

        self.moedas = {
            "USD": "Dólar Americano",
            "EUR": "Euro",
            "GBP": "Libra Esterlina",
            "JPY": "Iene Japonês",
            "BRL": "Real Brasileiro",
            "CAD": "Dólar Canadense",
            "AUD": "Dólar Australiano",
            "CHF": "Franco Suíço"}

    def montar_tela_inicial(self):
        imagem = tk.PhotoImage(file="./img/fundo_2.png")

        self.imagem = imagem  # Armazena a imagem como um atributo da classe para evitar coleta de lixo

        fundo = tk.Label(self.janela, image=imagem)
        fundo.place(x=0, y=0, relwidth=1, relheight=1)

        titulo = tk.Label(
        self.janela,
        text="Bem-vindo ao\n Sistema de Cotação de Moedas",
        bg="#66b2b2",
        fg="white",
        font=("Arial", 20, "bold")
        )
        titulo.place(relx=0.5, rely=0.2, anchor="center")

        botao = tk.Button(
            self.janela,
            text="Entrar",
            bg="black",
            fg="white",
            font=("Arial", 20, "bold"),
            command=self.abrir_programa
        )
        botao.place(relx=0.5, rely=0.9, anchor="center")

    # ----------------
    # JANELA PRINCIPAL
    # ----------------
    def abrir_programa(self):

        # Remove os elementos da tela inicial
        for element in self.janela.winfo_children():
            element.destroy()

        mensagem = tk.Label(
        self.janela, 
        text="Sistema de busca para cotação de moedas",
        bg="#008080",
        fg="white",
        font=("Arial", 20, "bold")
        )
        mensagem.grid(row=0, column=0, pady=10, columnspan=2, sticky="ew")

        mensagem_entrada = tk.Label(
        self.janela,
        text="Digite a moeda que deseja consultar:",
        bg="#66b2b2",
        fg="white",
        font=("Arial", 14, "bold")
        )
        mensagem_entrada.grid(row=1, column=0, pady=60)

        opcoes = [f"{sigla} - {nome}" for sigla, nome in self.moedas.items()]

        self.entrada_moeda = ttk.Combobox(self.janela,
                                          values=opcoes,
                                          state="readonly",
                                          width=30,)
        self.entrada_moeda.grid(row=1, column=1, pady=20, sticky="w", padx=10)

        botao_cotacao = tk.Button(
        self.janela,
        text="Buscar Cotação",
        bg="black",
        fg="white",
        font=("Arial", 20, "bold"),
        command=self.buscar_cotacao
        )
        botao_cotacao.grid(row=2, column=0, pady=20, columnspan=2, sticky="ew", padx=10)

    def buscar_cotacao(self):
        
        moeda = self.entrada_moeda.get()
        print(f"Moeda pesquisada: {moeda}")

    def executar(self):
        self.janela.mainloop()




if __name__ == "__main__":
    app = AppCotacao()
    app.executar()