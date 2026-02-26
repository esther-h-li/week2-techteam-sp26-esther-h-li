from fastapi import FastAPI
from model import User, Product

app = FastAPI()


db_users = {}
db_products = {}


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.get("/users")
def read_users():
    return db_users


@app.post("/user")
def create_user(user: User):
    db_users[user.id] = user


@app.put("/user")
def update_user(user: User):
    if user.id in db_users:
        db_users[user.id] = user


@app.get("/user")
def get_all_users_prefix(prefix: str):
    users = []
    for user in db_users:
        if(user.name.startsWith(prefix)):
            users.append(user)
    return users

 


@app.delete("/user")
def delete_user(user: User):
    if user.id in db_users:
        db_users.remove(user.id)


@app.get("/products")
def read_products():
    return db_products


@app.post("/product")
def create_product(product: Product):
    db_products[product.id] = product


@app.put("/product")
def update_product(product: Product):
    if(product.id in db_products):
        db_products[product.id] = product


@app.delete("/product")
def delete_product(product: Product):
        if(product.id in db_products):
            del db_products[product.id]