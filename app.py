import tkinter as tk
from tkinter import Tk, Label, Button, Entry, ttk, messagebox, filedialog
from tkinter import messagebox
import requests
from datetime import datetime
from openpyxl import Workbook

class AppCotacao:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.configure(bg="#265051")
        self.janela.geometry("1000x850")

        self.janela.columnconfigure(0, weight=1)
        self.janela.columnconfigure(1, weight=1)

        self.entrada_moeda = None  # Inicializa a variável de entrada de moeda

        self.historico = []  # Lista para armazenar o histórico de cotações
        
        self.tabela_historico = None  # Referência para o Treeview do histórico

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
        """
        Monta a tela de boas-vindas (primeira tela exibida ao abrir o app).
        """

        # --- Paleta de cores desta tela ---
        # O dourado remete a moeda/valor (tema do app) e aparece só no
        # filete decorativo e no botão "Entrar" — único ponto de destaque
        # da tela, o resto fica discreto em tons de teal escuro/branco.
        COR_FUNDO = "#0F3D3E"  # teal escuro — agora é o fundo da janela inteira
        COR_DESTAQUE = "#D9A441"  # dourado — cor do filete e do botão
        COR_DESTAQUE_HOVER = "#C78F2E"  # dourado mais escuro — efeito hover
        COR_TEXTO_PRINCIPAL = "#FFFFFF"
        COR_TEXTO_SECUNDARIO = "#BFD9D8"

        # ALTERADO: em vez de carregar uma imagem com tk.PhotoImage, um Frame
        # preenche a janela inteira com a cor do antigo painel. Usamos um
        # Frame (e não self.janela.configure(bg=...)) para que essa cor valha
        # só para esta tela — a tela principal (abrir_programa) continua
        # usando sua própria paleta sem ser afetada por essa troca.
        fundo = tk.Frame(self.janela, bg=COR_FUNDO)
        fundo.place(x=0, y=0, relwidth=1, relheight=1)

        # Frame que agrupa o conteúdo e fica centralizado na janela
        conteudo = tk.Frame(fundo, bg=COR_FUNDO)
        conteudo.place(relx=0.5, rely=0.5, anchor="center")

        # NOVO: filete dourado curto, centralizado, como detalhe decorativo
        # acima da saudação — sem uma "borda de cartão" para encostar, um
        # filete largo ficaria estranho, por isso ele é estreito e centrado
        filete = tk.Frame(conteudo, bg=COR_DESTAQUE, width=70, height=3)
        filete.pack(anchor="center", pady=(0, 18))
        filete.pack_propagate(False)

        saudacao = tk.Label(
            conteudo,
            text="Bem-vindo(a)",
            bg=COR_FUNDO,
            fg=COR_TEXTO_SECUNDARIO,
            font=("Segoe UI", 12)
        )
        saudacao.pack(anchor="center")

        titulo = tk.Label(
            conteudo,
            text="Cotação de Moedas",
            bg=COR_FUNDO,
            fg=COR_TEXTO_PRINCIPAL,
            font=("Segoe UI", 30, "bold")
        )
        titulo.pack(anchor="center", pady=(4, 10))

        subtitulo = tk.Label(
            conteudo,
            text="Consulte cotações atualizadas de\nmoedas estrangeiras",
            bg=COR_FUNDO,
            fg=COR_TEXTO_SECUNDARIO,
            font=("Segoe UI", 11),
            justify="center"
        )
        subtitulo.pack(anchor="center", pady=(0, 30))

        botao = tk.Button(
            conteudo,
            text="Entrar",
            bg=COR_DESTAQUE,
            fg="#1A1A1A",
            activebackground=COR_DESTAQUE_HOVER,
            activeforeground="#1A1A1A",
            font=("Segoe UI", 13, "bold"),
            relief="flat",
            bd=0,
            padx=36,
            pady=10,
            cursor="hand2",  # NOVO: cursor de "mãozinha" ao passar o mouse, indicando que é clicável
            command=self.abrir_programa
        )
        botao.pack(anchor="center")

        # NOVO: efeito de hover — escurece o botão quando o mouse passa por cima
        # e volta à cor original quando o mouse sai
        botao.bind("<Enter>", lambda e: botao.configure(bg=COR_DESTAQUE_HOVER))
        botao.bind("<Leave>", lambda e: botao.configure(bg=COR_DESTAQUE))

    # ----------------
    # JANELA PRINCIPAL
    # ----------------
    def abrir_programa(self):

        # Remove os elementos da tela inicial
        for element in self.janela.winfo_children():
            element.destroy()

        self.janela.rowconfigure(4, weight=1)

        mensagem = tk.Label(
        self.janela, 
        text="Sistema de busca para cotação de moedas",
        bg="#0F3D3E",
        fg="white",
        font=("Arial", 20, "bold")
        )
        mensagem.grid(row=0, column=0, pady=10, columnspan=2, sticky="ew")

        mensagem_entrada = tk.Label(
        self.janela,
        text="Digite a moeda que deseja consultar:",
        bg="#265051",
        fg="white",
        font=("Arial", 14, "bold")
        )
        mensagem_entrada.grid(row=1, column=0, pady=30)

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
        font=("Arial", 16, "bold"),
        command=self.buscar_cotacao
        )
        botao_cotacao.grid(row=2, column=0, pady=20, columnspan=2, padx=10, ipadx=10, ipady=10)

        self.montar_area_historico()  # Chama o método para montar a área de histórico


    def montar_area_historico(self):

        container_historico = tk.Frame(self.janela, bg="#265051")
        container_historico.grid(row=4,
                                column=0,
                                columnspan=2,
                                padx=10,
                                pady=10,
                                sticky="nsew")

        # Botões (posicionados primeiro)
        frame_botoes = tk.Frame(container_historico, bg="#265051")
        frame_botoes.pack(side="bottom", fill="x", pady=(10, 0))

        botao_exportar_excel = tk.Button(
                    frame_botoes,
                    text="Exportar para Excel",
                    bg="black",
                    fg="white",
                    font=("Arial", 12, "bold"),
                    command=self.exportar_excel
                )
        botao_exportar_excel.pack(side="left", expand=True, padx=10, ipady=4)
        
        botao_exportar_txt = tk.Button(
                            frame_botoes,
                            text="Exportar para TXT",
                            bg="black",
                            fg="white",
                            font=("Arial", 12, "bold"),
                            command=self.exportar_txt
                        )
        botao_exportar_txt.pack(side="left", expand=True, padx=10, ipady=4)


        # Tabela de histórico (ocupa o espaço acima dos botões)
        frame_tabela = tk.Frame(container_historico)
        frame_tabela.pack(side="top", fill="both", expand=True)

        colunas = ("Data", "Hora", "Moeda", "Cotação")

        self.tabela_historico = ttk.Treeview(frame_tabela,
                                            columns=colunas,
                                            show="headings",
                                        )

        # Define o texto do cabeçalho da coluna
        self.tabela_historico.heading("Data", text="Data")
        self.tabela_historico.heading("Hora", text="Hora")
        self.tabela_historico.heading("Moeda", text="Moeda")
        self.tabela_historico.heading("Cotação", text="Cotação")


        # Define a largura/alinhamente de cada coluna
        self.tabela_historico.column("Data", width=100, anchor="center")
        self.tabela_historico.column("Hora", width=100, anchor="center")
        self.tabela_historico.column("Moeda", width=250, anchor="center")
        self.tabela_historico.column("Cotação", width=150, anchor="center")
                    
        # Barra de rolagem vertical
        scrollbar = ttk.Scrollbar(frame_tabela,
                                orient="vertical",
                                command=self.tabela_historico.yview)
        self.tabela_historico.configure(yscrollcommand=scrollbar.set)

        self.tabela_historico.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")


    def buscar_cotacao(self):
        
        moeda = self.entrada_moeda.get()

        if not moeda:
            messagebox.showwarning("Aviso:", "Por favor, selecione uma moeda.")
            return

        uri = f"https://api.frankfurter.dev/v2/rate/brl/{moeda[0:3]}"

        try:

            response = requests.get(uri, timeout=10)

        except requests.exceptions.RequestException as e:
            messagebox.showerror("Erro de conexão:", f"Não foi possível conectar à API:\n{e}")
            return

        if response.status_code == 200:
            data = response.json()
            resultado = data["rate"]

        else:
            resultado = f"Erro na requisição: {response.status_code}"

        data_atual = datetime.now().strftime("%d/%m/%Y")
        hora_atual = datetime.now().strftime("%H:%M:%S")

        # Registro da consulta
        registro = {
            "data": data_atual,
            "hora": hora_atual,
            "moeda": moeda,
            "cotacao": resultado
        }
        self.historico.append(registro)

        # Insere linha na tabela exibida na tela
        self.tabela_historico.insert(
            "", "end",
            values=(data_atual, hora_atual, moeda, resultado)
        )  
            
       
    def exportar_excel(self):

        if not self.historico:
            messagebox.showinfo("Histórico de cotações vazio.")
            return

        # Janela do sistema para o usuário escolher onde salvar
        caminho = filedialog.asksaveasfilename(
            defaultextension=".xlsx",
            filetypes=[("Planilha Excel", "*.xlsx")],
            initialfile="historico_cotacoes.xlsx",
            title="Salvar histórico como..."
        )

        if not caminho: # Caso o usuário cancele o salvamento
            return

        planilha = Workbook()
        aba = planilha.active
        aba.title = "Histórico de cotações"

        # Cabeçalho da planilha
        aba.append(["Data", "Hora", "Moeda", "Cotação (BRL)"])


        for registro in self.historico:
            aba.append([
                registro["data"],
                registro["hora"],
                registro["moeda"],
                registro["cotacao"]
            ])

        try:
            planilha.save(caminho)
            messagebox.showinfo("Salvo.", f"Histórico exportado para:\n{caminho}.")
        except Exception as e:
            messagebox.showerror("Erro ao salvar: {e}.")

    def exportar_txt(self):

        if not self.historico:
                    messagebox.showinfo("Histórico de cotações vazio.")
                    return

        caminho = filedialog.asksaveasfilename(
                    defaultextension=".txt",
                    filetypes=[("Arquivo de texto", "*.txt")],
                    initialfile="historico_cotacoes.txt",
                    title="Salvar histórico como..."
                )
        
        if not caminho: 
            return

        try:
            with open(caminho, "w", encoding="utf-8") as arquivo:
                arquivo.write("Histórico de Cotações\n")
                arquivo.write("=" * 40 + "\n\n")

                for registro in self.historico:
                    arquivo.write(
                        f"Data: {registro["data"]} | "
                        f"Hora: {registro["hora"]} | "
                        f"Moeda: {registro["moeda"]} | "
                        f"Cotação: {registro["cotacao"]}\n"
                    )
            messagebox.showinfo("Sucesso.", f"Histórico exportado para\n{caminho}.")

        except Exception as e:
            messagebox.showerror(f"Erro ao salvar: {e}.")

    def executar(self):
        self.janela.mainloop()



if __name__ == "__main__":
    app = AppCotacao()
    app.executar()