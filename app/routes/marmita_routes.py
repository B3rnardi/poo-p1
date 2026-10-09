from fastapi import APIRouter, HTTPException
from app.controllers.marmita_controller import MarmitaController

router = APIRouter(prefix='/api/marmitas', tags=['Marmitas'])
controller = MarmitaController()

@router.get('')
def listar_marmitas():
    return controller.listar_todas()

@router.get('/tamanho/{tamanho}')
def listar_marmitas_por_tamanho(tamanho: str):
    # Rota extra para consumir a list comprehension do controller
    return controller.listar_por_tamanho(tamanho)

@router.get('/{id}')
def buscar_marmita(id: int):
    marmita = controller.buscar_por_id(id)
    if marmita is None:
        raise HTTPException(status_code=404, detail='Marmita não encontrada')
    return marmita