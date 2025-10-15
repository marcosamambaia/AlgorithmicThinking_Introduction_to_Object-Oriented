# 🏠 Imobiliária R.M — Geração de Orçamento de Aluguel

Aplicação desenvolvida como parte do desafio técnico de Algorithmic Thinking, com foco em introdução à programação orientada a objetos. O sistema permite calcular o valor do aluguel mensal de imóveis, simular contratos parcelados e exportar os dados em múltiplos formatos.

---

## 🎯 Objetivo

Automatizar o processo de geração de orçamento para locação de imóveis (casas, apartamentos e estúdios), oferecendo uma interface intuitiva e exportações profissionais.

---

## ⚙️ Funcionalidades

- Cálculo automático do aluguel mensal com base nas características do imóvel
- Simulação de contrato imobiliário parcelado
- Exportação dos dados em:
  - `.json`: estrutura de dados
  - `.pdf`: documento formatado
  - `.csv`: planilha com 12 parcelas mensais
- Interface gráfica com Tkinter
- Versão terminal via `main.py`

---

## 🧠 Regras de Negócio

- **Valores base:**
  - Apartamento: R$ 700,00 (1 quarto)
  - Casa: R$ 900,00 (1 quarto)
  - Estúdio: R$ 1200,00

- **Adicionais:**
  - Apartamento com 2 quartos: + R$ 200,00
  - Casa com 2 quartos: + R$ 250,00
  - Garagem: + R$ 300,00
  - Estúdio com 2 vagas: + R$ 250,00
  - Vagas extras no estúdio: + R$ 60,00 por vaga

- **Desconto:**
  - Apartamentos sem crianças recebem 5% de desconto no aluguel

- **Contrato:**
  - Valor fixo: R$ 2.000,00
  - Parcelado em até 5 vezes

---

## 🛠️ Tecnologias Utilizadas

- `Python`: linguagem principal
- `Tkinter`: interface gráfica
- `JSON`: exportação estruturada
- `FPDF`: geração de PDF
- `CSV`: exportação de parcelas mensais

---

## 📁 Estrutura de Arquivos

| Arquivo                | Função principal                          |
|------------------------|-------------------------------------------|
| `main.py`              | Versão terminal do app                    |
| `app.py`               | Interface gráfica com Tkinter             |
| `imovel_model.py`      | Lógica de cálculo do aluguel              |
| `contrato_model.py`    | Lógica de contrato e parcelas             |
| `exportador_json.py`   | Exportação dos dados para JSON            |
| `exportador_csv.py`    | Exportação das parcelas mensais para CSV |
| `data/orcamento.json`  | Arquivo gerado com os dados do orçamento |
| `data/orcamento.pdf`   | Arquivo PDF gerado com os dados formatados |
| `data/orcamento.csv`   | Arquivo CSV com as 12 parcelas mensais   |

---

## ▶️ Como Executar

### Interface gráfica:

```bash
python app.py

Autor
Marco Samambaia
Projeto acadêmico — Algorithmic Thinking
Universidade: UNIFECAF
