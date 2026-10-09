from app.models.cliente import carregar_clientes, Cliente

class ClienteController:
    def _init_(self):
        self._clientes = carregar_clientes()

    def _para_dicionario(self, cliente):
        return {
            'id': cliente.mostrar_id(),
            'nome': cliente.mostrar_nome(),
            'telefone': cliente.mostrar_telefone()
        }

    def listar_todos(self):
        return [self._para_dicionario(c) for c in self._clientes]

    def buscar_por_id(self, id_cliente):
        for c in self._clientes:
            if c.mostrar_id() == id_cliente:
                return self._para_dicionario(c)
        return None