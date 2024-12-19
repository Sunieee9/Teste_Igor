from models import Category, db
from sqlalchemy.orm import joinedload

class CategoryDAO:  # Criação do elemetento category

    @staticmethod
    def add_category(name, description):  # Funcionalidade para adicionar categoria
        new_category = Category(name = name, description = description)
        db.session.add(new_category)
        db.session.commit()
        return new_category
    
    @staticmethod
    def get_category(id_category):  # Vasualizar Category
        return Category.query.get(id_category)

    @staticmethod
    def get_all_category(): # Visualizar todos as tuplas em category
        return Category.query.all()

    @staticmethod
    def get_filter_category(name):  # Filtrar category por nome
        query = Category.query.filter((Category.name.ilike(f"%{name}%")))
        return query.all()

    @staticmethod
    def edit_category(self, id_category, name, description):
        category = self.get_category_by_id(id_category)  # Busca a categoria pelo ID
        if category:
            category.name = name
            category.description = description
            self.db.session.commit()  # Salva as alterações no banco
            return category  # Retorna a categoria atualizada
        return None  # Retorna None se a categoria não for encontrada
   