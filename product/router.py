from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from core.security import role_required
from core.session import SessionLocal, get_db
from product.schemas import ProductCreate,ProductUpdate,ProductResponse
from product.crud import create_product,get_all_products,get_product_by_id,update_product,delete_product

router = APIRouter(prefix="/products", tags=["Products"])




@router.get("/",response_model=list[ProductResponse])
def list_products(db:Session = Depends(get_db)):
    return get_all_products(db)

@router.get("/{product_id}",response_model=ProductResponse)
def get_product(product_id:int,db : Session = Depends(get_db)):
    product = get_product_by_id(db,product_id)
    if not product:
        raise HTTPException(status_code=404,detail="Product not found")
    return product

@router.post("/",response_model=ProductResponse)
def add_product(
    data: ProductCreate,
    db:Session = Depends(get_db),
    user = Depends(role_required("admin"))
):
    return create_product(db,data)

@router.put("/{product_id}",response_model=ProductResponse)
def edit_product(
    product_id : int,
    data: ProductUpdate,
    db: Session = Depends(get_db),
    user = Depends(role_required("admin"))
):
    product = get_product_by_id(db,product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return update_product(db, product,data)

@router.delete("/{product_id}")
def remove_product(
    product_id:int,
    db: Session = Depends(get_db),
    user = Depends(role_required("admin"))
):
    product = get_product_by_id(db,product_id)
    if not product:
        raise HTTPException(status_code=404, detail="product not found")
    delete_product(db,product)
    return {"message":"Product deleted"}

    