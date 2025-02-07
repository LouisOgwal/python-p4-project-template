from flask import Flask, request, jsonify, abort
from flask_migrate import Migrate
from flask_cors import CORS
from flask_restful import Api, Resource
from models import db, bcrypt, User, Product, Store, StoreProduct
from config import Config
import os
from dotenv import load_dotenv  

load_dotenv()

app = Flask(__name__)
app.config.from_object(server.config.Config)

db.init_app(app)
bcrypt.init_app(app)
migrate = Migrate(app, db)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)
api = Api(app)

@app.route('/')
def index():
    return '<h1>Project Server Running</h1>'

class ProductListResource(Resource):
    def get(self):
        products = Product.query.all()
        return jsonify([{"id": p.id, "name": p.name, "description": p.description} for p in products])

    def post(self):
        try:
            data = request.get_json()
            if not data.get("name"):
                return jsonify({"error": "Product name is required"}), 400
            product = Product(name=data["name"], description=data.get("description", ""))
            db.session.add(product)
            db.session.commit()
            return jsonify({"id": product.id, "name": product.name, "description": product.description}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

class ProductResource(Resource):
    def delete(self, product_id):
        product = Product.query.get(product_id)
        if not product:
            return jsonify({"error": "Product not found"}), 404
        db.session.delete(product)
        db.session.commit()
        return jsonify({"message": "Product deleted"}), 200

class StoreListResource(Resource):
    def get(self):
        stores = Store.query.all()
        return jsonify([{"id": s.id, "name": s.name, "address": s.address} for s in stores])

    def post(self):
        try:
            data = request.get_json()
            if not data.get("name") or not data.get("address"):
                return jsonify({"error": "Store name and address are required"}), 400
            store = Store(name=data["name"], address=data["address"])
            db.session.add(store)
            db.session.commit()
            return jsonify({"id": store.id, "name": store.name, "address": store.address}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

class StoreResource(Resource):
    def delete(self, store_id):
        store = Store.query.get(store_id)
        if not store:
            return jsonify({"error": "Store not found"}), 404
        db.session.delete(store)
        db.session.commit()
        return jsonify({"message": "Store deleted"}), 200

class StoreProductResource(Resource):
    def post(self):
        try:
            data = request.get_json()
            if not all(k in data for k in ("price", "product_id", "store_id")):
                return jsonify({"error": "Missing required fields: price, product_id, store_id"}), 400

            store_product = StoreProduct(price=data["price"], product_id=data["product_id"], store_id=data["store_id"])
            db.session.add(store_product)
            db.session.commit()
            return jsonify({"id": store_product.id, "price": store_product.price, "product_id": store_product.product_id, "store_id": store_product.store_id}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

api.add_resource(ProductListResource, "/products")
api.add_resource(ProductResource, "/products/<int:product_id>")
api.add_resource(StoreListResource, "/stores")
api.add_resource(StoreResource, "/stores/<int:store_id>")
api.add_resource(StoreProductResource, "/store_products")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5555))
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=port, debug=False)  # Ensure proper hosting
