from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import repository
import schemas
from database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/clients/{client_id}", response_model=schemas.ClientOut)
def read_client(client_id: int, db: Session = Depends(get_db)):
    db_client = repository.get_client(db, client_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return db_client

@app.get("/clients/", response_model=list[schemas.ClientOut])
def read_clients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return repository.get_clients(db, skip=skip, limit=limit)

