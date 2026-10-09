# app/models/cliente.py
from app.data.clientes_mock import CLIENTES

class Cliente:
    def __init__(self, id, nome, telefone):
        self._id = id
        self.alterar_nome(nome)
        self.alterar_telefone(telefone)

    def mostrar_id(self):
        return self._id

    def mostrar_nome(self):
        return self._nome

    def mostrar_telefone(self):
        return self._telefone

    def alterar_nome(self, nome):
        if not nome.strip():
            raise ValueError("O nome do cliente não pode ser vazio")
        self._nome = nome.strip()

    def alterar_telefone(self, telefone):
        # 3ª Regra de Negócio com Raise da prova
        telefone_limpo = telefone.replace("-", "").replace(" ", "")
        if len(telefone_limpo) != 11 or not telefone_limpo.isdigit():
            raise ValueError("O telefone deve ter exatamente 11 dígitos numéricos")
        self._telefone = telefone_limpo

    def __repr__(self):
        return f"Cliente(id={self._id}, nome='{self._nome}')"

def carregar_clientes():
    return [Cliente(c['id'], c['nome'], c['telefone']) for c in CLIENTES]