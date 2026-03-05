from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import get_db, engine, Base
from models import User
from crud import get_users, get_user, create_user, update_user, delete_user, UserCreate, UserUpdate

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/users")
def read_users(db: Session = Depends(get_db)):
    return get_users(db)

@app.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/users")
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@app.put("/users/{user_id}")
def update_user_endpoint(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    updated_user = update_user(db, user_id, user)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@app.delete("/users/{user_id}")
def delete_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    deleted_user = delete_user(db, user_id)
    if deleted_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}