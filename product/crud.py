from sqlalchemy.orm import Session

from backend.product.model import Product


def create_product(db:Session,data):
    product = Product(**data.dict())
    db.add(product)
    db.commit()
    db.refresh(product)

def get_all_products(db:Session):
    return db.query(Product).all()

def get_product_by_id(db: Session,product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

def update_product(db:Session,product,data):
    for key,value in data.dict(exclude_unset = True).items():
        setattr(product,key,value)
    db.commit()
    db.refresh(product)
    return product

def delete_product(db:Session,product):
    db.delete(product)
    db.commit()