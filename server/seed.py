#!/usr/bin/env python3

# Standard library imports
from random import choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User, Product, Store, StoreProduct

fake = Faker()

if __name__ == '__main__':
    with app.app_context():
        print("Seeding database...")

        db.drop_all()
        db.create_all()

        admin = User(name="Admin", email="admin@example.com", is_admin=True)
        admin.set_password("password")


        users = []
        for _ in range(5):
            user = User(
                name=fake.name(),
                email=fake.email(),
                is_admin=False
            )
            user.set_password("password")
            users.append(user)

        products = [
            Product(name="iPhone 14", description="Latest iPhone model"),
            Product(name="MacBook Pro", description="High-performance laptop"),
            Product(name="iPad Air", description="Lightweight and powerful tablet"),
            Product(name="Apple Watch", description="Smartwatch with health features"),
        ]
        db.session.add_all(products)
        db.session.commit()

        stores = [
            Store(name="Apple Store NYC", address="5th Avenue, New York"),
            Store(name="Apple Store SF", address="Union Square, San Francisco"),
            Store(name="Apple Store LA", address="Beverly Hills, Los Angeles"),
        ]
        db.session.add_all(stores)
        db.session.commit() 

        store_products = []
        for _ in range(10):
            product = rc(products)
            store = rc(stores)

            store_product = StoreProduct(
                price=round(fake.pyfloat(left_digits=3, right_digits=2, positive=True), 2),
                product_id=product.id,
                store_id=store.id,
            )
            store_products.append(store_product)


        db.session.add(admin)
        db.session.add_all(users)
        db.session.add_all(store_products)

        db.session.commit()

        print("Database seeded successfully!")
