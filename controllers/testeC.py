from flask import Blueprint, jsonify
from repository import CategoriaRepository

teste = Blueprint('teste', __name__)

@teste.route('/filter')
def categoria():
 
    id = 1  # ID da categoria que será alterada
    name = "Batom"
    description = "batom brilhante"

    repository = CategoriaRepository()
    # Passa os argumentos na ordem correta para o método edit_category
    category = repository.edit_category(id_category=id, name=name, description=description)

    # Verifica se a categoria foi encontrada e alterada com sucesso
    if category is not None:
        print(f"Categoria alterada: ID={category.id}, Nome={category.name}, Descrição={category.description}")
        return jsonify({"message": "Categoria alterada com sucesso!", 
                        "id": category.id, 
                        "name": category.name, 
                        "description": category.description})
    else:
        # Caso a categoria não seja encontrada, retorna um erro
        print("Erro: Categoria não encontrada ou alteração falhou.")
        return jsonify({"error": "Categoria não encontrada ou alteração falhou."}), 404
