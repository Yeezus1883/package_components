# main.py
# from app.database import init_db

# if __name__ == "__main__":
#     init_db()
#     print("Database initialized")
    


from typing import List
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from auth import auth
from . import models, schemas, database
app = FastAPI()

# Dependency to get the DB session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/root')
def root():
    return {"message": "Backend is up and running"}

@app.post("/packages/", response_model=schemas.Package)
def create_package(package: schemas.PackageCreate, db: Session = Depends(get_db),user=Depends(auth.auth_handler.get_current_user)):
    db_package = models.Package(
        package_name=package.package_name,
        display_description=package.display_description,
        status=package.status,
        candidate_type=package.candidate_type,
        check_type=package.check_type,
        rack_id=package.rack_id,
        created_at=package.created_at,
        updated_at=package.updated_at,
    )
    db.add(db_package)
    db.commit()
    db.refresh(db_package)
    
    # Add components
    for component in package.components:
        db_component = models.PackageComponent(
            component_name=component.component_name, package_id=db_package.id
        )
        db.add(db_component)
    
    db.commit()
    return db_package

@app.get("/packages/", response_model=List[schemas.Package])
def read_packages(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    packages = db.query(models.Package).offset(skip).limit(limit).all()
    return packages

@app.get("/packages/{package_id}", response_model=schemas.Package)
def read_package(package_id: int, db: Session = Depends(get_db)):
    package = db.query(models.Package).filter(models.Package.id == package_id).first()
    if package is None:
        raise HTTPException(status_code=404, detail="Package not found")
    return package

@app.delete("/packages/{package_id}", response_model=dict)
def delete_package(package_id: int, db: Session = Depends(get_db)):
    package = db.query(models.Package).filter(models.Package.id == package_id).first()
    if package is None:
        raise HTTPException(status_code=404, detail="Package not found")
    db.delete(package)
    db.commit()
    return {"message": "Package deleted successfully"}
