# app/models/pedido.py
from app.data.pedidos_mock import PEDIDOS

class Pedido:
    def __init__(self, id, id_cliente, itens):
        self._id = id
        self._id_cliente = id_cliente
        self.alterar_itens(itens)
        self._status = "aberto"

    def mostrar_id(self):
        return self._id

    def mostrar_id_cliente(self):
        return self._id_cliente
        
    def mostrar_itens(self):
        return self._itens

    def mostrar_status(self):
        return self._status

    def alterar_itens(self, itens):
        # 4ª Regra de Negócio com Raise da prova
        if not itens or len(itens) == 0:
            raise ValueError("Um pedido precisa ter pelo menos um item")
        self._itens = itens
        
    def calcular_total(self, catalogo_marmitas):
        # Calcula o valor somando os itens sem saber qual o tipo da marmita (polimorfismo)
        total = 0
        for item in self._itens:
            id_marmita = item['id_marmita']
            quantidade = item['quantidade']
            
            if quantidade <= 0:
                 raise ValueError("A quantidade de marmitas deve ser maior que zero")
            
            # Localiza a marmita recebida do controller
            marmita_obj = next((m for m in catalogo_marmitas if m.mostrar_id() == id_marmita), None)
            if marmita_obj:
                total += marmita_obj.calcular_preco() * quantidade
        return total
        
    def __repr__(self):
        return f"Pedido(id={self._id}, cliente={self._id_cliente})"

def carregar_pedidos():
    return [Pedido(p['id'], p['id_cliente'], p['itens']) for p in PEDIDOS]