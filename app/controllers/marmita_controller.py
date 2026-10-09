from app.models.marmita import carregar_marmitas

class MarmitaController:
    def __init__(self):
        self._marmitas = carregar_marmitas()

    def _para_dicionario(self, marmita):
        return {
            'id': marmita.mostrar_id(),
            'nome': marmita.mostrar_nome(),
            'tamanho': marmita.mostrar_tamanho(),
            'preco_final': marmita.calcular_preco()
        }

    def listar_todas(self):
        return [self._para_dicionario(m) for m in self._marmitas]

    def buscar_por_id(self, id):
        for m in self._marmitas:
            if m.mostrar_id() == id:
                return self._para_dicionario(m)
        return None

    # Regra da prova: pelo menos um filtro com compreensão de lista
    def listar_por_tamanho(self, tamanho):
        return [self._para_dicionario(m) for m in self._marmitas if m.mostrar_tamanho() == tamanho.upper()]