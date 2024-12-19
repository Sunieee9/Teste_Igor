from flask import Blueprint, jsonify
from repository import OrdersRepository

orders_repository = OrdersRepository()


pedido_controller = Blueprint('pedidos', __name__)

# Rota para adicionar um novo pedido

# Pedido da Maria Eduarda

@pedido_controller.route('/pedido2')
def pedido_2():
    
    person_id = 1
    date = "19/12/2024"
    status = "Pendente"
    total = 240

    # Crie uma instância de OrdersRepository antes de chamar add_order

    new_order = orders_repository.add_order(person_id=person_id, date=date, status=status, total=total)

    return jsonify(new_order.to_json()), 201

# Pedido do Rafael Pires

@pedido_controller.route('/pedido1')
def pedido_1():
    
    person_id = 2
    date = "18/12/2024"
    status = "Pendente"
    total = 380

    # Crie uma instância de OrdersRepository antes de chamar add_order

    new_order = orders_repository.add_order(person_id=person_id, date=date, status=status, total=total)

    return jsonify(new_order.to_json()), 201

# Pedido da Yasmin Bastos

@pedido_controller.route('/pedido3')
def pedido_3():
    
    person_id = 3
    date = "20/12/2024"
    status = "Pendente"
    total = 170

    # Crie uma instância de OrdersRepository antes de chamar add_order

    new_order = orders_repository.add_order(person_id=person_id, date=date, status=status, total=total)

    return jsonify(new_order.to_json()), 201