from fastapi import APIRouter, HTTPException
from app.controllers.cliente_controller import ClienteController

router = APIRouter(prefix='/api/clientes', tags=['Clientes'])
controller = ClienteController()

@router.get('')
def listar_clientes():
    return controller.listar_todos()

@router.get('/{id}')
def buscar_cliente(id: int):
    cliente = controller.buscar_por_id(id)
    if cliente is None:
        raise HTTPException(status_code=404, detail='Cliente não encontrado')
    return cliente