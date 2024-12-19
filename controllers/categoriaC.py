from flask import Blueprint, jsonify
from repository import CategoriaRepository

categoria_contreller = Blueprint('categoria', __name__)

@categoria_contreller.route('/bijuteria')
def add_bijuteria():
    name = "Joias e Bijuterias"
    description = "Usados para adicionar sofisticação ao visual"

    # Crie uma instância de CategoriaRepository antes de chamar add_order
    category_repository = CategoriaRepository()

    new_category = category_repository.add_category(name = name, description = description)

    return jsonify(new_category.to_json()), 201

@categoria_contreller.route('/relogio')
def add_relogio():
    name = "Relógios"
    description = "Combinação de funcionalidade e estilo, variando de modelos clássicos a esportivos"

    # Crie uma instância de CategoriaRepository antes de chamar add_order
    category_repository = CategoriaRepository()

    new_category = category_repository.add_category(name = name, description = description)

    return jsonify(new_category.to_json()), 201

@categoria_contreller.route('/oculos')
def add_oculos():
    name = "Óculos de Sol"
    description = "Protegem os olhos dos raios UV e são acessórios essenciais para compor um look casual ou elegante"

    # Crie uma instância de CategoriaRepository antes de chamar add_order
    category_repository = CategoriaRepository()

    new_category = category_repository.add_category(name = name, description = description)

    return jsonify(new_category.to_json()), 201

@categoria_contreller.route('/bolsa')
def add_bolsa():
    name = "Bolsas e Mochilas"
    description = "Acessórios práticos e estilosos, disponíveis em diversos tamanhos e materiais para diversos benefícios"

    # Crie uma instância de CategoriaRepository antes de chamar add_order
    category_repository = CategoriaRepository()

    new_category = category_repository.add_category(name = name, description = description)

    return jsonify(new_category.to_json()), 201

@categoria_contreller.route('/cinto')
def add_cinto():
    name = "Cintos"
    description = "Usados ​​para ajustar roupas ou como destaque visual"

    # Crie uma instância de CategoriaRepository antes de chamar add_order
    category_repository = CategoriaRepository()

    new_category = category_repository.add_category(name = name, description = description)

    return jsonify(new_category.to_json()), 201

@categoria_contreller.route('/cachecol')
def add_cachecou():
    name = "Lenços e Cachecóis"
    description = "Acessórios versáteis para qualquer estação, que podem ser usados ​​no pescoço, cabelo ou amarrados à bolsa"

    # Crie uma instância de CategoriaRepository antes de chamar add_order
    category_repository = CategoriaRepository()

    new_category = category_repository.add_category(name = name, description = description)

    return jsonify(new_category.to_json()), 201

@categoria_contreller.route('/chapeu')
def add_chapeu():
    name = "Chapéus e Bonés"
    description = "Complementam o estilo e oferecem proteção contra o sol, variando de modelos clássicos como chapéus de palha a bonés esportivos"

    # Crie uma instância de CategoriaRepository antes de chamar add_order
    category_repository = CategoriaRepository()

    new_category = category_repository.add_category(name = name, description = description)

    return jsonify(new_category.to_json()), 201

@categoria_contreller.route('/luva')
def add_luva():
    name = "Luvas"
    description = "Acessórios funcionais e decorativos, disponíveis em opções de couro, lã ou tecido, ideais para dias frios ou sofisticados"

    # Crie uma instância de CategoriaRepository antes de chamar add_order
    category_repository = CategoriaRepository()

    new_category = category_repository.add_category(name = name, description = description)

    return jsonify(new_category.to_json()), 201

@categoria_contreller.route('/sapato')
def add_sapato():
    name = "Sapatos e Calçados"
    description = "Sapatos elegantes, sofisticados e botas podem ser verdadeiros acessórios para completar um visual"

    # Crie uma instância de CategoriaRepository antes de chamar add_order
    category_repository = CategoriaRepository()

    new_category = category_repository.add_category(name = name, description = description)

    return jsonify(new_category.to_json()), 201

@categoria_contreller.route('/cabelo')
def add_cabelo():
    name = "Acessórios de Cabelo"
    description = "Incluem tiaras, presilhas, elásticos, bandanas e grampos decorativos que ajudam a realçar o penteado e o estilo pessoal"

    # Crie uma instância de CategoriaRepository antes de chamar add_order
    category_repository = CategoriaRepository()

    new_category = category_repository.add_category(name = name, description = description)

    return jsonify(new_category.to_json()), 201
