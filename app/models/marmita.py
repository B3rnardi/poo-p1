from app.data.marmitas_mock import MARMITAS

class Marmita:
    def __init__(self, id, nome, tamanho, preco):
        self._id = id
        self.alterar_nome(nome)
        self._tamanho = tamanho
        self.alterar_preco(preco)

    def mostrar_id(self): 
        return self._id
        
    def mostrar_nome(self): 
        return self._nome
        
    def mostrar_tamanho(self): 
        return self._tamanho
        
    def mostrar_preco(self): 
        return self._preco

    def alterar_nome(self, nome):
        if not nome.strip():
            raise ValueError('nome não pode ser vazio')
        self._nome = nome.strip()

    def alterar_preco(self, novo_preco):
        if novo_preco < 0:
            raise ValueError('preço não pode ser negativo')
        self._preco = novo_preco

def carregar_marmitas():
    return [Marmita(m['id'], m['nome'], m['tamanho'], m['preco']) for m in MARMITAS]