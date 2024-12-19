from flask import Blueprint, jsonify
from repository import ProductRepository

produto_repository = ProductRepository()

produto_controller = Blueprint('produto', __name__)

# Joias e Bijuteria

@produto_controller.route('/colar')
def colar():
    name = "Colar Aurora"
    description = "Colar com pingente em forma de estrela, feito de prata 925 com banho de ouro rosé"
    price = 150
    stock_quantity = 25
    category_id = 1

    new_produto = produto_repository.add_product(name = name, description = description, price = price, stock_quantity = stock_quantity, category_id = category_id)

    return jsonify(new_produto.to_json()), 201

@produto_controller.route('/brinco')
def brinco():
    name = "Brinco Pérola Lunar"
    description = "Par de brincos clássicos com pérolas naturais e acabamento em prata"
    price = 90
    stock_quantity = 40
    category_id = 1

    new_produto = produto_repository.add_product(name = name, description = description, price = price, stock_quantity = stock_quantity, category_id = category_id)

    return jsonify(new_produto.to_json()), 201

# Relógios

@produto_controller.route('/esporte')
def esporte():
    name = "Relógio Sport Active"
    description = "Relógio esportivo resistente à água com funções de cronômetro e alarme"
    price = 180
    stock_quantity = 30
    category_id = 2

    new_produto = produto_repository.add_product(name = name, description = description, price = price, stock_quantity = stock_quantity, category_id = category_id)

    return jsonify(new_produto.to_json()), 201

@produto_controller.route('/moderno')
def moderno():
    name = "Relógio Modern Steel"
    description = "Relógio unissex com pulseira de aço inoxidável e viseira minimalista"
    price = 300
    stock_quantity = 15
    category_id = 2

    new_produto = produto_repository.add_product(name = name, description = description, price = price, stock_quantity = stock_quantity, category_id = category_id)

    return jsonify(new_produto.to_json()), 201

# Óculos de Sol

@produto_controller.route('/aviador')
def aviador():
    name = "Óculos Aviador Classic"
    description = "Modelo clássico de óculos aviador com armação dourada e lentes polarizadas"
    price = 200
    stock_quantity = 20
    category_id = 3

    new_produto = produto_repository.add_product(name = name, description = description, price = price, stock_quantity = stock_quantity, category_id = category_id)

    return jsonify(new_produto.to_json()), 201

@produto_controller.route('/retro')
def retro():
    name = "Óculos Cat Eye Retro"
    description = "Óculos de sol com armação preta e formato cat eye, ideal para looks vintage"
    price = 150
    stock_quantity = 35
    category_id = 3

    new_produto = produto_repository.add_product(name = name, description = description, price = price, stock_quantity = stock_quantity, category_id = category_id)

    return jsonify(new_produto.to_json()), 201

# Bolsas e Mochilas

@produto_controller.route('/elegante')
def elegante():
    name = "Bolsa Elegance Compact"
    description = "Bolsa de couro sintético com design minimalista e alça ajustável"
    price = 240
    stock_quantity = 18
    category_id = 4

    new_produto = produto_repository.add_product(name = name, description = description, price = price, stock_quantity = stock_quantity, category_id = category_id)

    return jsonify(new_produto.to_json()), 201

@produto_controller.route('/urbana')
def urbana():
    name = "Mochila Urban Explorer"
    description = "Mochila leve e resistente, com vários compartimentos e estilo moderno"
    price = 190
    stock_quantity = 25
    category_id = 4

    new_produto = produto_repository.add_product(name = name, description = description, price = price, stock_quantity = stock_quantity, category_id = category_id)

    return jsonify(new_produto.to_json()), 201

# Cintos

@produto_controller.route('/vintage')
def vintage():
    name = "Cinto Vintage Brown"
    description = "Cinto de couro marrom com fivela dourada e design clássico"
    price = 100
    stock_quantity = 40
    category_id = 5

    new_produto = produto_repository.add_product(name = name, description = description, price = price, stock_quantity = stock_quantity, category_id = category_id)

    return jsonify(new_produto.to_json()), 201

@produto_controller.route('/fit')
def fit():
    name = "into Stretch Fit"
    description = "Cinto elástico preto com ajuste automático, ideal para conforto diário"
    price = 80
    stock_quantity = 50
    category_id = 5

    new_produto = produto_repository.add_product(name = name, description = description, price = price, stock_quantity = stock_quantity, category_id = category_id)

    return jsonify(new_produto.to_json()), 201

# Lenços e Cachecóis

@produto_controller.route('/floral')
def floral():
    name = "Lenço Floral Breeze"
    description = "Lenço leve com estampas florais coloridas, perfeito para dias quentes"
    price = 50
    stock_quantity = 60
    category_id = 6

    new_produto = produto_repository.add_product(name = name, description = description, price = price, stock_quantity = stock_quantity, category_id = category_id)

    return jsonify(new_produto.to_json()), 201

@produto_controller.route('/luxo')
def luxo():
    name = "Cachecol Winter Luxe"
    description = "Cachecol de lã trançada com toque macio, disponível em tons neutros"
    price = 100
    stock_quantity = 30
    category_id = 6

    new_produto = produto_repository.add_product(name = name, description = description, price = price, stock_quantity = stock_quantity, category_id = category_id)

    return jsonify(new_produto.to_json()), 201

# Chapéus e Bonés

@produto_controller.route('/fedora')
def fedora():
    name = "Chapéu Fedora Summer"
    description = "Chapéu de palha estilo fedora com faixa decorativa preta"
    price = 130
    stock_quantity = 20
    category_id = 7

    new_produto = produto_repository.add_product(name = name, description = description, price = price, stock_quantity = stock_quantity, category_id = category_id)

    return jsonify(new_produto.to_json()), 201

@produto_controller.route('/casual')
def casual():
    name = "Boné Casual Fit"
    description = "Boné de algodão com ajuste traseiro e design básico"
    price = 60
    stock_quantity = 45
    category_id = 7

    new_produto = produto_repository.add_product(name = name, description = description, price = price, stock_quantity = stock_quantity, category_id = category_id)

    return jsonify(new_produto.to_json()), 201

# Luvas

@produto_controller.route('/classica')
def classica():
    name = "Luvas de Couro Clássicas"
    description = "Luvas de couro preto com forro interno macio, ideais para dias frios"
    price = 150
    stock_quantity = 12
    category_id = 8

    new_produto = produto_repository.add_product(name = name, description = description, price = price, stock_quantity = stock_quantity, category_id = category_id)

    return jsonify(new_produto.to_json()), 201

@produto_controller.route('/inverno')
def inverno():
    name = "Luvas Touchscreen Winter"
    description = "Luvas térmicas compatíveis com telas touch, disponíveis em preto"
    price = 100
    stock_quantity = 25
    category_id = 8

    new_produto = produto_repository.add_product(name = name, description = description, price = price, stock_quantity = stock_quantity, category_id = category_id)

    return jsonify(new_produto.to_json()), 201

# Sapatos e Calçados

@produto_controller.route('/comfort')
def comfort():
    name = "Sandália Comfort Walk"
    description = "Sandália de couro com palmilha anatômica, ideal para o dia a dia"
    price = 200
    stock_quantity = 22
    category_id = 9

    new_produto = produto_repository.add_product(name = name, description = description, price = price, stock_quantity = stock_quantity, category_id = category_id)

    return jsonify(new_produto.to_json()), 201

@produto_controller.route('/bota')
def bota():
    name = "Bota Urban Trekker"
    description = "Bota em couro sintético com solado atualizado, ideal para aventuras urbanas"
    price = 260
    stock_quantity = 15
    category_id = 9

    new_produto = produto_repository.add_product(name = name, description = description, price = price, stock_quantity = stock_quantity, category_id = category_id)

    return jsonify(new_produto.to_json()), 201

# Acessórios de Cabelo

@produto_controller.route('/tiara')
def tiara():
    name = "Tiara Glam Pearl"
    description = "Tiara dourada com aplicação de pérolas, ideal para eventos sofisticados"
    price = 70
    stock_quantity = 35
    category_id = 10

    new_produto = produto_repository.add_product(name = name, description = description, price = price, stock_quantity = stock_quantity, category_id = category_id)

    return jsonify(new_produto.to_json()), 201

@produto_controller.route('/presilha')
def presilha():
    name = "Presilha Shine Crystal"
    description = "Presilha de metal com cristais, ideal para penteados elegantes"
    price = 40
    stock_quantity = 50
    category_id = 10

    new_produto = produto_repository.add_product(name = name, description = description, price = price, stock_quantity = stock_quantity, category_id = category_id)

    return jsonify(new_produto.to_json()), 201