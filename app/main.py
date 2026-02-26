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
    return list(db_users.values)


@app.post("/user")
def create_user(user: User):
    db_users[user._id] = user
    return user


@app.put("/user")
def update_user(user: User):
    if user._id in db_users:
        db_users[user._id] = user
    return {"message": "User deleted"}


@app.get("/user")
def get_all_users_prefix(prefix: str):
    users = []
    for user in db_users:
        if(user.name.startsWith(prefix)):
            users.append(user)
    return users.values

 


@app.delete("/user")
def delete_user(_id:int):
    if _id in db_users:
        db_users.remove(_id)


@app.get("/products")
def read_products():
    return list(db_products.values)


@app.post("/product")
def create_product(product: Product):
    db_products[product._id] = product
    return product


@app.put("/product")
def update_product(product: Product):
    if(product.id in db_products):
        db_products[product._id] = product
    return product


@app.delete("/product")
def delete_product(_id:int):
        if(_id in db_products):
            del db_products[_id]
        return {"message": "Product deleted"}