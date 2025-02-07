from flask_restful import Api, Resource
from flask import request, jsonify
from .models import Product, User, Category
from server.database import db  

api = Api()

class ProductResource(Resource):
    def get(self):
        products = Product.query.all()
        return jsonify([product.to_dict() for product in products])

    def post(self):
        data = request.get_json()
        new_product = Product(name=data['name'], price=data['price'], category_id=data['category_id'])
        db.session.add(new_product)
        db.session.commit()
        return jsonify(new_product.to_dict()), 201

class ProductDeleteResource(Resource):
    def delete(self, product_id):
        product = Product.query.get(product_id)
        if not product:
            return jsonify({"error": "Product not found"}), 404
        db.session.delete(product)
        db.session.commit()
        return jsonify({"message": "Product deleted"})

class CategoryResource(Resource):
    def get(self):
        categories = Category.query.all()
        return jsonify([category.to_dict() for category in categories])

class UserResource(Resource):
    def get(self):
        users = User.query.all()
        return jsonify([user.to_dict() for user in users])


def register_routes(api):
    api.add_resource(ProductResource, "/products")
    api.add_resource(ProductDeleteResource, "/products/<int:product_id>")
    api.add_resource(CategoryResource, "/categories")
    api.add_resource(UserResource, "/users")
