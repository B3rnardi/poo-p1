from app.models.pedido import carregar_pedidos, Pedido
from app.models.marmita import carregar_marmitas

class PedidoController:
    def __init__(self):
        self._pedidos = carregar_pedidos()
        self._catalogo_marmitas = carregar_marmitas() 

    def _para_dicionario(self, pedido):
        return {
            'id': pedido.mostrar_id(),
            'id_cliente': pedido.mostrar_id_cliente(),
            'itens': pedido.mostrar_itens(),
            'status': pedido.mostrar_status(),
            'total': pedido.calcular_total(self._catalogo_marmitas) 
        }

    def listar_todos(self):
        return [self._para_dicionario(p) for p in self._pedidos]

    def buscar_por_id(self, id_pedido):
        for p in self._pedidos:
            if p.mostrar_id() == id_pedido:
                return self._para_dicionario(p)
        return None

    def criar_pedido(self, dados_pedido):
        novo_id = max([p.mostrar_id() for p in self._pedidos] + [0]) + 1
        
        novo_pedido = Pedido(
            id=novo_id,
            id_cliente=dados_pedido.get('id_cliente'),
            itens=dados_pedido.get('itens', [])
        )
        
        novo_pedido.calcular_total(self._catalogo_marmitas)
        
        self._pedidos.append(novo_pedido)
        return self._para_dicionario(novo_pedido)