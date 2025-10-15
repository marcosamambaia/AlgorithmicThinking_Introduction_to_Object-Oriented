import json

def salvar_json(tipo, quartos, garagem, criancas, valor_aluguel, valor_contrato, parcelas=12):
    dados = {
        "tipo_imovel": tipo,
        "quartos": quartos,
        "garagem": garagem,
        "criancas": criancas,
        "valor_aluguel_mensal": round(valor_aluguel, 2),
        "valor_contrato_total": round(valor_contrato, 2),
        "parcelas_contrato": parcelas,
        "valor_parcela_contrato": round(valor_contrato / parcelas, 2),
        "parcelas_mensais": []
    }

    for i in range(1, parcelas + 1):
        total_mes = round(valor_aluguel + (valor_contrato / parcelas), 2)
        dados["parcelas_mensais"].append({
            "mes": i,
            "valor_total": total_mes
        })

    with open("data/orcamento.json", "w", encoding="utf-8") as file:
        json.dump(dados, file, indent=4, ensure_ascii=False)