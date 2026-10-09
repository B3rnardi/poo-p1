# MARMITA DO DIA 

Sistema de gestão de pedidos e catálogo de marmitas desenvolvido em FastAPI, estruturado sob os princípios de Orientação a Objetos, polimorfismo, encapsulamento e validações robustas de regras de negócio.

---

## Estrutura do Projeto

O projeto segue uma arquitetura modularizada, separando as regras de domínio técnico das rotas da API:

```text
marmita_do_dia/
│
├── app/
│   ├── models/
│   │   ├── marmita.py          # Classe base e hierarquia (Tradicional e Fitness)
│   │   ├── cliente.py          # Modelo de clientes
│   │   └── pedido.py           # Modelo de pedidos e itens
│   ├── routes/
│   │   ├── marmita_routes.py   # Endpoints de marmitas e filtros
│   │   ├── cliente_routes.py   # Endpoints de clientes
│   │   └── pedido_routes.py    # Endpoints de pedidos e transações
│   └── data/                   # Ficheiros de dados simulados (mock)
│
├── main.py                     # Ponto de entrada da aplicação FastAPI
└── README.md                   # Documentação oficial do projeto

DIAGRAMA DE CLASSES

```mermaid
classDiagram
    direction TB

    class Marmita {
        # int _id
        # str _nome
        # float _preco_base
        +__init__(id, nome, preco_base)
        +mostrar_id() int
        +alterar_nome(nome) void
        +calcular_preco() float
    }

    class MarmitaTradicional {
        +VALOR_BASE: float
        +calcular_preco() float
    }

    class MarmitaFitness {
        +TAXA_FIT: float
        +calcular_preco() float
    }

    class Cliente {
        -int _id
        -str _nome
        -str _telefone
        +__init__(id, nome, telefone)
        +mostrar_id() int
        +alterar_nome(nome) void
        +alterar_telefone(telefone) void
    }

    class Pedido {
        -int _id
        -int _id_cliente
        -list _itens
        -str _status
        -float _total
        +__init__(id, id_cliente, itens, status)
        +mostrar_id() int
        +alterar_itens(itens) void
        +calcular_total(catalogo_marmitas) float
    }

    Marmita <|-- MarmitaTradicional
    Marmita <|-- MarmitaFitness
    Pedido --> Cliente : referencia