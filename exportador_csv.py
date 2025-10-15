import csv  # Importa o módulo CSV para manipulação de arquivos de planilha

def salvar_csv(valor_aluguel, valor_contrato, parcelas=12):  # Função para salvar as parcelas mensais em um arquivo CSV
    caminho = "data/orcamento.csv"  # Define o caminho e nome do arquivo
    valor_parcela = round(valor_contrato / parcelas, 2)  # Calcula o valor de cada parcela do contrato

    with open(caminho, mode="w", newline="", encoding="utf-8") as file:  # Abre o arquivo CSV para escrita
        writer = csv.writer(file)  # Cria o objeto escritor
        writer.writerow(["Mês", "Valor do Aluguel", "Parcela do Contrato", "Valor Total"])  # Cabeçalho da planilha

        for mes in range(1, parcelas + 1):  # Loop para gerar os dados de cada mês
            total_mes = round(valor_aluguel + valor_parcela, 2)  # Soma do aluguel com a parcela do contrato
            writer.writerow([mes, f"{valor_aluguel:.2f}", f"{valor_parcela:.2f}", f"{total_mes:.2f}"])  # Escreve a linha no CSV
