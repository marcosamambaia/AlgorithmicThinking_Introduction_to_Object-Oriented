# imovel_model.py

class Imovel:
    def __init__(self, tipo, quartos, garagem, criancas, vagas_estudio=0):
        self.tipo = tipo.lower()
        self.quartos = quartos
        self.garagem = garagem
        self.criancas = criancas
        self.vagas_estudio = vagas_estudio

    def calcular_aluguel(self):
        if self.tipo == "apartamento":
            valor = 700
            if self.quartos == 2:
                valor += 200
            if self.garagem:
                valor += 300
            if not self.criancas:
                valor *= 0.95

        elif self.tipo == "casa":
            valor = 900
            if self.quartos == 2:
                valor += 250
            if self.garagem:
                valor += 300

        elif self.tipo == "estudio":
            valor = 1200
            if self.vagas_estudio >= 2:
                valor += 250
                vagas_extras = self.vagas_estudio - 2
                if vagas_extras > 0:
                    valor += 60 * vagas_extras
        else:
            raise ValueError("Tipo de imóvel inválido.")

        return round(valor, 2)