from app.data.marmitas_mock import MARMITAS

class Marmita:
    VALOR_BASE = 0.0

    def __init__(self, id, nome, tamanho):
        self._id = id
        self.alterar_nome(nome)
        self._tamanho = tamanho

    def mostrar_id(self): 
        return self._id
        
    def mostrar_nome(self): 
        return self._nome
        
    def mostrar_tamanho(self): 
        return self._tamanho
        
    def alterar_nome(self, nome):
        if not nome.strip():
            raise ValueError('O nome não pode ser vazio')
        self._nome = nome.strip()

    def calcular_preco(self):
        return self.VALOR_BASE

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self._id}, nome='{self._nome}')"


class MarmitaTradicional(Marmita):
    VALOR_BASE = 18.0

    def calcular_preco(self):
        return self.VALOR_BASE


class MarmitaFitness(Marmita):
    VALOR_BASE = 22.0

    def __init__(self, id, nome, tamanho, adicional_embalagem):
        super().__init__(id, nome, tamanho)
        if adicional_embalagem < 0:
            raise ValueError('O adicional da embalagem não pode ser negativo')
        self._adicional_embalagem = adicional_embalagem

    def calcular_preco(self):
        return self.VALOR_BASE + self._adicional_embalagem

TIPOS_MARMITA = {
    'tradicional': MarmitaTradicional,
    'fitness': MarmitaFitness
}

def carregar_marmitas():
    marmitas_carregadas = []
    for m in MARMITAS:
        dados = m.copy()
        tipo = dados.pop('tipo')
        ClasseCorreta = TIPOS_MARMITA[tipo]
        marmitas_carregadas.append(ClasseCorreta(**dados))
    return marmitas_carregadas