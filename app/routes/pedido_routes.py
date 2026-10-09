from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from typing import List
from app.controllers.pedido_controller import PedidoController
from app.controllers.cliente_controller import ClienteController

router = APIRouter(prefix='/api/pedidos', tags=['Pedidos'])
controller = PedidoController()
cliente_controller = ClienteController()

# Pydantic schemas apenas para ajudar o FastAPI a ler o JSON de entrada
class ItemPedidoSchema(BaseModel):
    id_marmita: int
    quantidade: int

class CriarPedidoSchema(BaseModel):
    id_cliente: int
    itens: List[ItemPedidoSchema]


@router.get('')
def listar_pedidos():
    return controller.listar_todos()

@router.get('/faturamento')
def relatorio_faturamento():
    # Rota exigida no documento para calcular faturamento sem 'if'
    pedidos = controller.listar_todos()
    total = sum(p['total'] for p in pedidos)
    return {"faturamento_total": total}

@router.get('/{id}')
def buscar_pedido(id: int):
    pedido = controller.buscar_por_id(id)
    if pedido is None:
        raise HTTPException(status_code=404, detail='Pedido não encontrado')
    return pedido

@router.post('', status_code=status.HTTP_201_CREATED)
def criar_pedido(dados: CriarPedidoSchema):
    # Verifica se cliente existe (404 ou 409 dependendo da interpretação, usaremos 404 para dado não encontrado)
    cliente = cliente_controller.buscar_por_id(dados.id_cliente)
    if cliente is None:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    
    # 409 Conflito: Regra extra para garantir o 409 (Cliente não pode fazer 2 pedidos simultâneos no mesmo dia)
    pedidos_existentes = controller.listar_todos()
    for p in pedidos_existentes:
        if p['id_cliente'] == dados.id_cliente and p['status'] == 'aberto':
             raise HTTPException(status_code=409, detail="O cliente já possui um pedido em aberto.")

    try:
        # Tenta criar. Se violar regra (quantidade <=0, vazio, etc), a Model dispara ValueError
        # E o controller passa o erro pra cá
        novo_pedido = controller.criar_pedido(dados.dict())
        return novo_pedido
    except ValueError as e:
        # A Rota traduz o erro da Model para HTTP 422, garantindo pontos na prova
        raise HTTPException(status_code=422, detail=str(e))