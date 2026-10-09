
"""Verificacao do modelo POO-P1.

Executa testes sem precisar subir a API.
Testa encapsulamento, heranca, polimorfismo,
regras de negocio e associacao entre as models.
"""

from app.models.cliente import Cliente, carregar_clientes
from app.models.marmita import (
    Marmita,
    MarmitaTradicional,
    MarmitaFitness,
    carregar_marmitas,
)
from app.models.pedido import Pedido, carregar_pedidos

falhas = 0


def checar(ok, descricao):
    global falhas

    if ok:
        print(f"  OK      {descricao}")
    else:
        print(f"  FALHOU  {descricao}")
        falhas += 1


# --------------------------------------------------
print("\n1. Encapsulamento: Cliente")
# --------------------------------------------------

try:
    Cliente(99, "   ", "11987654321")
    checar(False, "Cliente deveria recusar nome vazio")
except ValueError:
    checar(True, "Cliente recusa nome vazio")

try:
    Cliente(99, "Teste", "123")
    checar(False, "Cliente deveria recusar telefone invalido")
except ValueError:
    checar(True, "Cliente recusa telefone invalido")

cliente = Cliente(1, " Ana ", "11987654321")

checar(cliente.mostrar_nome() == "Ana", "Nome removendo espacos externos")
checar(
    cliente.mostrar_telefone() == "11987654321",
    "Telefone armazenado somente com digitos",
)
checar(
    not hasattr(Cliente, "mostrar_senha"),
    "Cliente nao possui metodo mostrar_senha",
)


# --------------------------------------------------
print("\n2. Encapsulamento: Marmita")
# --------------------------------------------------

try:
    Marmita(99, "   ", "Grande")
    checar(False, "Marmita deveria recusar nome vazio")
except ValueError:
    checar(True, "Marmita recusa nome vazio")

try:
    MarmitaFitness(99, "Fitness", "Media", -1)
    checar(False, "MarmitaFitness deveria recusar adicional negativo")
except ValueError:
    checar(True, "MarmitaFitness recusa adicional negativo")

checar(
    not hasattr(Marmita, "alterar_id"),
    "Nao existe metodo alterar_id",
)


# --------------------------------------------------
print("\n3. Heranca: tipos de marmita")
# --------------------------------------------------

checar(
    issubclass(MarmitaTradicional, Marmita),
    "MarmitaTradicional herda de Marmita",
)

checar(
    issubclass(MarmitaFitness, Marmita),
    "MarmitaFitness herda de Marmita",
)

checar(
    "calcular_preco" in MarmitaTradicional.__dict__,
    "MarmitaTradicional implementa calcular_preco",
)

checar(
    "calcular_preco" in MarmitaFitness.__dict__,
    "MarmitaFitness implementa calcular_preco",
)


# --------------------------------------------------
print("\n4. Polimorfismo: calculo dos precos")
# --------------------------------------------------

tradicional = MarmitaTradicional(1, "Caseira", "Media")
fitness = MarmitaFitness(2, "Fitness", "Grande", 3.0)

checar(
    tradicional.calcular_preco() == 18.0,
    "MarmitaTradicional custa 18 reais",
)

checar(
    fitness.calcular_preco() == 25.0,
    "MarmitaFitness soma o adicional ao valor base",
)

marmitas = [tradicional, fitness]

checar(
    [m.calcular_preco() for m in marmitas] == [18.0, 25.0],
    "A mesma chamada calcula precos conforme o tipo",
)


# --------------------------------------------------
print("\n5. Carregamento dos dados mock")
# --------------------------------------------------

clientes = carregar_clientes()
marmitas_carregadas = carregar_marmitas()
pedidos = carregar_pedidos()

checar(isinstance(clientes, list), "Clientes carregados como lista")
checar(isinstance(marmitas_carregadas, list), "Marmitas carregadas como lista")
checar(isinstance(pedidos, list), "Pedidos carregados como lista")

checar(
    all(isinstance(c, Cliente) for c in clientes),
    "Mock de clientes gera objetos Cliente",
)

checar(
    all(isinstance(m, Marmita) for m in marmitas_carregadas),
    "Mock de marmitas gera objetos Marmita ou subclasses",
)

checar(
    all(isinstance(p, Pedido) for p in pedidos),
    "Mock de pedidos gera objetos Pedido",
)


# --------------------------------------------------
print("\n6. Pedido: regra de negocio")
# --------------------------------------------------

try:
    Pedido(99, 1, [])
    checar(False, "Pedido deveria recusar lista de itens vazia")
except ValueError:
    checar(True, "Pedido exige pelo menos um item")


# --------------------------------------------------
print("\n7. Pedido: calculo do total")
# --------------------------------------------------

catalogo_teste = [
    MarmitaTradicional(1, "Tradicional", "Media"),
    MarmitaFitness(2, "Fitness", "Grande", 3.0),
]

pedido_teste = Pedido(
    99,
    1,
    [
        {"id_marmita": 1, "quantidade": 2},
        {"id_marmita": 2, "quantidade": 1},
    ],
)

checar(
    pedido_teste.calcular_total(catalogo_teste) == 61.0,
    "Total soma 2 tradicionais e 1 fitness",
)

try:
    pedido_invalido = Pedido(
        100,
        1,
        [{"id_marmita": 1, "quantidade": 0}],
    )
    pedido_invalido.calcular_total(catalogo_teste)
    checar(False, "Pedido deveria recusar quantidade zero")
except ValueError:
    checar(True, "Pedido recusa quantidade zero")

try:
    pedido_invalido = Pedido(
        101,
        1,
        [{"id_marmita": 1, "quantidade": -1}],
    )
    pedido_invalido.calcular_total(catalogo_teste)
    checar(False, "Pedido deveria recusar quantidade negativa")
except ValueError:
    checar(True, "Pedido recusa quantidade negativa")


# --------------------------------------------------
print("\n8. Pedido: status inicial")
# --------------------------------------------------

checar(
    pedido_teste.mostrar_status() == "aberto",
    "Pedido inicia com status aberto",
)


# --------------------------------------------------
print("\n9. Camadas: models nao dependem do FastAPI")
# --------------------------------------------------

import app.models.cliente as modulo_cliente
import app.models.marmita as modulo_marmita
import app.models.pedido as modulo_pedido

for modulo in (modulo_cliente, modulo_marmita, modulo_pedido):
    with open(modulo.__file__, encoding="utf-8") as arquivo:
        conteudo = arquivo.read().lower()

    checar(
        "fastapi" not in conteudo,
        f"{modulo.__name__.split('.')[-1]}.py nao importa FastAPI",
    )


# --------------------------------------------------
print("\n10. Resultado final")
# --------------------------------------------------

if falhas == 0:
    print("\nTODOS OS TESTES PASSARAM!")
else:
    print(f"\n{falhas} teste(s) falharam.")
