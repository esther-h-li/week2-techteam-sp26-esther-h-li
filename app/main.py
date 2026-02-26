from fastapi import FastAPI
from model import User, Product
from fastapi import HTTPException

app = FastAPI()


db_users = {}
db_products = {}


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.get("/users")
def read_users():
    return list(db_users.values())


@app.post("/user", status_code = 201)
def create_user(user: User):
    db_users[user.id] = user
    return user


@app.put("/user")
def update_user(user: User):
    if user.id in db_users:
        db_users[user.id] = user
        return user
    else: raise HTTPException(status_code=404, detail="User not found")



@app.get("/user")
def get_all_users_prefix(prefix: str):
    users = []
    for user in db_users:
        if(user.name.startsWith(prefix)):
            users.append(user)
    return users
 


@app.delete("/user")
def delete_user(_id:int):
    if _id in db_users:
        del db_users[_id]
        return {"message": "User deleted"}
    else:
       raise HTTPException(status_code=404, detail="User not found")        


@app.get("/products")
def read_products():
    return list(db_products.values())


@app.post("/product", status_code = 201)
def create_product(product: Product):
    db_products[product.id] = product
    return product


@app.put("/product")
def update_product(product: Product):
    if(product.id in db_products):
        db_products[product.id] = product
        return product
    else:
       raise HTTPException(status_code=404, detail="Product not found")


@app.delete("/product")
def delete_product(_id:int):
        if(_id in db_products):
            del db_products[_id]
        else:
            raise HTTPException(status_code=404, detail="Product not found")
        return {"message": "Product deleted"}