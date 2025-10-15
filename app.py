import tkinter as tk
from tkinter import messagebox
from imovel_model import Imovel
from contrato_model import Contrato
from exportador_json import salvar_json
import json
import os
from exportador_csv import salvar_csv

# Função para calcular e exibir o orçamento
def calcular_orcamento():
    tipo = tipo_var.get()
    try:
        quartos = int(quartos_var.get())
        if quartos < 1 or quartos > 4:
            raise ValueError
    except ValueError:
        messagebox.showerror("Erro", "Quantidade de quartos deve ser um número entre 1 e 4.")
        return

    garagem = garagem_var.get()
    criancas = criancas_var.get()
    vagas_estudio = 0
    if tipo == "estudio":
        try:
            vagas_estudio = int(vagas_var.get())
            if vagas_estudio < 2:
                raise ValueError
        except ValueError:
            messagebox.showerror("Erro", "Estúdios devem ter no mínimo 2 vagas.")
            return

    imovel = Imovel(tipo, quartos, garagem, criancas, vagas_estudio)
    valor_aluguel = imovel.calcular_aluguel()
    contrato = Contrato()
    valor_parcela = contrato.calcular_parcela()

    salvar_json(tipo, quartos, garagem, criancas, valor_aluguel, contrato.valor_total)
    

    resultado = (
        f" ORÇAMENTO FINAL\n"
        f"Tipo de imóvel: {tipo.capitalize()}\n"
        f"Quartos: {quartos}\n"
        f"Garagem: {'Sim' if garagem else 'Não'}\n"
        f"Crianças: {'Sim' if criancas else 'Não'}\n"
        f"Valor do aluguel: R$ {valor_aluguel:.2f}\n"
        f"Contrato: R$ {contrato.valor_total:.2f} em {contrato.parcelas}x de R$ {valor_parcela:.2f}"
    )
    resultado_texto.delete("1.0", tk.END)
    resultado_texto.insert(tk.END, resultado)

# Função para exibir o conteúdo do JSON
def mostrar_json():
    try:
        with open("data/orcamento.json", "r", encoding="utf-8") as f:
            dados = json.load(f)
            texto = json.dumps(dados, indent=4, ensure_ascii=False)
            resultado_texto.delete("1.0", tk.END)
            resultado_texto.insert(tk.END, texto)
    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo JSON não encontrado.")


from fpdf import FPDF

def gerar_pdf_orcamento():
    try:
        with open("data/orcamento.json", "r", encoding="utf-8") as f:
            dados = json.load(f)
    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo 'orcamento.json' não encontrado.")
        return

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Orçamento Imobiliário R.M", ln=True, align="C")
    pdf.ln(10)

    for chave, valor in dados.items():
        if chave != "parcelas_mensais":
            texto = f"{chave.replace('_', ' ').capitalize()}: {valor}"
            pdf.cell(200, 10, txt=texto, ln=True)

    pdf.ln(10)
    pdf.cell(200, 10, txt="Parcelas Mensais:", ln=True)
    for parcela in dados["parcelas_mensais"]:
        linha = f"Mês {parcela['mes']}: R$ {parcela['valor_total']:.2f}"
        pdf.cell(200, 10, txt=linha, ln=True)

    pdf.output("data/orcamento.pdf")
    messagebox.showinfo("PDF gerado", "✅ PDF salvo como 'orcamento.pdf' na pasta /data")


def gerar_csv_orcamento():
    try:
        with open("data/orcamento.json", "r", encoding="utf-8") as f:
            dados = json.load(f)
    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo 'orcamento.json' não encontrado.")
        return

    valor_aluguel = dados["valor_aluguel_mensal"]
    valor_contrato = dados["valor_contrato_total"]
    salvar_csv(valor_aluguel, valor_contrato)
    messagebox.showinfo("CSV gerado", "✅ Arquivo 'orcamento.csv' salvo na pasta /data")

# Interface gráfica
janela = tk.Tk()
janela.title("Imobiliária R.M")

# Campos de entrada
tk.Label(janela, text="Tipo de imóvel:").grid(row=0, column=0, sticky="w")
tipo_var = tk.StringVar(value="apartamento")
tk.OptionMenu(janela, tipo_var, "apartamento", "casa", "estudio").grid(row=0, column=1)

tk.Label(janela, text="Quartos (1 a 4):").grid(row=1, column=0, sticky="w")
quartos_var = tk.StringVar()
tk.Entry(janela, textvariable=quartos_var).grid(row=1, column=1)

tk.Label(janela, text="Garagem:").grid(row=2, column=0, sticky="w")
garagem_var = tk.BooleanVar()
tk.Checkbutton(janela, variable=garagem_var).grid(row=2, column=1, sticky="w")

tk.Label(janela, text="Crianças:").grid(row=3, column=0, sticky="w")
criancas_var = tk.BooleanVar()
tk.Checkbutton(janela, variable=criancas_var).grid(row=3, column=1, sticky="w")

tk.Label(janela, text="Vagas (estúdio):").grid(row=4, column=0, sticky="w")
vagas_var = tk.StringVar()
tk.Entry(janela, textvariable=vagas_var).grid(row=4, column=1)

# Botões
tk.Button(janela, text="Calcular orçamento", command=calcular_orcamento).grid(row=5, column=0, pady=10)
tk.Button(janela, text="Mostrar JSON", command=mostrar_json).grid(row=5, column=1)
tk.Button(janela, text="Exportar PDF", command=gerar_pdf_orcamento).grid(row=5, column=2, padx=10) 
tk.Button(janela, text="Exportar CSV", command=gerar_csv_orcamento).grid(row=5, column=3, padx=10)

# Área de resultado
resultado_texto = tk.Text(janela, width=70, height=20)
resultado_texto.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

janela.mainloop()