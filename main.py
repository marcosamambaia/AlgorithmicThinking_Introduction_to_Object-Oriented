# Importa as classes e funções necessárias de outros arquivos
from imovel_model import Imovel
from contrato_model import Contrato
from exportador_json import salvar_json
from exportador_csv import salvar_csv

# Mensagem de boas-vindas
print("Bem-vindo à Imobiliária R.M!")
print("Vamos gerar seu orçamento de aluguel mensal.\n")

# Função auxiliar para validar entrada de tipo de imóvel
def entrada_tipo_imovel():
    tipos_validos = ["apartamento", "casa", "estudio"]
    while True:
        tipo = input("Tipo de imóvel (apartamento, casa, estudio): ").strip().lower()
        if tipo in tipos_validos:
            return tipo
        print(" Tipo inválido. Escolha entre: apartamento, casa ou estudio.")

# Função auxiliar para validar entrada de número inteiro
def entrada_int(pergunta):
    while True:
        try:
            return int(input(pergunta))
        except ValueError:
            print(" Valor inválido. Digite um número inteiro.")

# Função auxiliar para validar entrada booleana (sim/não)
def entrada_bool(pergunta):
    while True:
        resposta = input(pergunta + " (s/n): ").strip().lower()
        if resposta in ["s", "n"]:
            return resposta == "s"
        print(" Entrada inválida. Digite 's' para sim ou 'n' para não.")

#  Entrada do tipo de imóvel com validação
tipo = entrada_tipo_imovel()

#  Entrada da quantidade de quartos com validação (1 a 4)
def entrada_quartos():
    while True:
        try:
            quartos = int(input("Quantidade de quartos (1 a 4): "))
            if 1 <= quartos <= 4:
                return quartos
            else:
                print(" Valor inválido. Digite um número entre 1 e 4.")
        except ValueError:
            print(" Entrada inválida. Digite um número inteiro.")

quartos = entrada_quartos()

def gerar_pdf_orcamento():
    try:
        with open("data/orcamento.json", "r", encoding="utf-8") as f:
            dados = json.load(f)
    except FileNotFoundError:
        print(" Arquivo 'orcamento.json' não encontrado.")
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
    print(" PDF gerado com sucesso em 'data/orcamento.pdf'")
# ↓↓↓ Entrada sobre vaga de garagem com validação
garagem = entrada_bool("Deseja vaga de garagem?")

# ↓↓↓ Entrada sobre presença de crianças com validação
criancas = entrada_bool("Possui crianças?")

# ↓↓↓ Entrada sobre vagas de estacionamento (apenas para estúdios)
vagas_estudio = 0
if tipo == "estudio":
    vagas_estudio = entrada_int("Quantas vagas de estacionamento? (mínimo 2): ")

# Instancia a classe Imovel com os dados fornecidos
imovel = Imovel(tipo, quartos, garagem, criancas, vagas_estudio)

# Calcula o valor do aluguel com base nas regras de negócio
valor_aluguel = imovel.calcular_aluguel()

# Instancia a classe Contrato com valor fixo de R$ 2.000,00
contrato = Contrato()

# Calcula o valor da parcela do contrato
valor_parcela = contrato.calcular_parcela()

# Exibe o orçamento final para o usuário
print("\n ORÇAMENTO FINAL")
print(f"Tipo de imóvel: {tipo.capitalize()}")
print(f"Valor mensal do aluguel: R$ {valor_aluguel:.2f}")
print(f"Valor do contrato: R$ {contrato.valor_total:.2f}")
print(f"Parcelado em até {contrato.parcelas}x de R$ {valor_parcela:.2f}")

# Salva os dados em um arquivo JSON
salvar_json(tipo, quartos, garagem, criancas, valor_aluguel, contrato.valor_total)

# Salva os dados em um arquivo CSV
salvar_csv(valor_aluguel, contrato.valor_total)

## Confirmação de geração do arquivo
print("\n Arquivo 'orcamento.json' gerado com sucesso na pasta /data")
print(" Arquivo 'orcamento.csv' gerado com sucesso na pasta /data")


# Gera o PDF com os dados do orçamento
gerar_pdf_orcamento()

from fpdf import FPDF
import json

