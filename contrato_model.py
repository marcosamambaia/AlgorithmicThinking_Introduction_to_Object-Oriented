# contrato.py

class Contrato:
    def __init__(self, valor_total=2000, parcelas=5):
        self.valor_total = valor_total
        self.parcelas = parcelas

    def calcular_parcela(self):
        return round(self.valor_total / self.parcelas, 2)