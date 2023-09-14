import tkinter as tk

def calcular():
    try:
        expressao = entrada.get()
        resultado = str(eval(expressao))
        resultado_label.config(text="Resultado: " + resultado)
        entrada.delete(0, 'end')
    except Exception as e:
        resultado_label.config(text="Erro")

def apagar_ultimo():
    entrada.delete(len(entrada.get()) - 1, 'end')

def apagar_tudo():
    entrada.delete(0, 'end')

janela = tk.Tk()
janela.title("Calculadora")

# Define o tamanho mínimo e máximo da janela
largura = 400
altura = 600
janela.geometry(f"{largura}x{altura}")
janela.minsize(largura, altura)
janela.maxsize(largura, altura)

# Desativa a capacidade de redimensionamento
janela.resizable(False, False)

# Estilo dos botões
botao_estilo = {
    'padx': 20,
    'pady': 20,
    'bd': 4,
    'bg': '#E0E0E0',  # Cor de fundo cinza claro
    'fg': 'black',    # Cor do texto preto
    'font': ('Helvetica', 14),
}

# Entrada de texto
entrada = tk.Entry(janela, font=('Helvetica', 18), justify="right")
entrada.grid(row=0, column=0, columnspan=4, padx=20, pady=20, ipady=10)

# Rótulo para exibir o resultado
resultado_label = tk.Label(janela, text="Resultado: ", font=('Helvetica', 14))
resultado_label.grid(row=1, column=0, columnspan=4, padx=20, pady=10, sticky="nsew")

# Layout dos botões em uma grade no estilo de uma calculadora física
botoes = [
    'C', '', '', '⌫',
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Coordenadas dos botões
coordenadas = [
    (2, 0), (2, 1), (2, 2), (2, 3),
    (3, 0), (3, 1), (3, 2), (3, 3),
    (4, 0), (4, 1), (4, 2), (4, 3),
    (5, 0), (5, 1), (5, 2), (5, 3),
    (6, 0), (6, 1), (6, 2), (6, 3)
]

for i, btn_text in enumerate(botoes):
    row_val, col_val = coordenadas[i]
    if btn_text == '⌫':
        tk.Button(janela, text=btn_text, command=apagar_ultimo, **botao_estilo).grid(row=row_val, column=col_val, sticky="nsew")
    elif btn_text == 'C':
        tk.Button(janela, text=btn_text, command=apagar_tudo, **botao_estilo).grid(row=row_val, column=col_val, sticky="nsew")
    elif btn_text == '=':
        tk.Button(janela, text=btn_text, command=calcular, **botao_estilo).grid(row=row_val, column=col_val, sticky="nsew")
    elif btn_text == '':
        pass  # Espaço vazio
    else:
        tk.Button(janela, text=btn_text, command=lambda btn_text=btn_text: entrada.insert("end", btn_text), **botao_estilo).grid(row=row_val, column=col_val, sticky="nsew")

# Ajustar a largura das colunas
for i in range(4):
    janela.grid_columnconfigure(i, weight=1)

# Ajustar a altura da primeira linha
janela.grid_rowconfigure(0, weight=1)

# Ajustar a altura das outras linhas
for i in range(1, 7):
    janela.grid_rowconfigure(i, weight=2)

# Iniciar a interface gráfica
janela.mainloop()
