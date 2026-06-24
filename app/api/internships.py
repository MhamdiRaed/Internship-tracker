from fastapi import APIRouter, Depends, HTTPException
# pyrefly: ignore [missing-import]
from sqlalchemy.orm import Session
# pyrefly: ignore [missing-import]
from sqlalchemy.exc import IntegrityError
from app.db.database import get_db
from app.db.models import Internship
from app.schemas.internship import InternshipCreate, InternshipResponse, InternshipUpdate

router=APIRouter()

@router.get("/")
def root():
    return {"status": "ok"}

@router.post("/internships")
def create_internship(internship: InternshipCreate, db : Session = Depends(get_db)):
    db_internship = Internship(
        title=internship.title,
        company=internship.company,
        country=internship.country,
        remote=internship.remote,
        url=internship.url
    )
    try:
        db.add(db_internship)
        db.commit()
        db.refresh(db_internship)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Internship already exists"
        )
    return db_internship    

@router.get("/internships/{id}", response_model=InternshipResponse)
def get_internship(id :int , db : Session = Depends(get_db)):
    internship = db.query(Internship).filter(Internship.id == id).first()
    if internship is None:
        raise HTTPException(
            status_code=404,
            detail="internship not found"
        )
    return internship

@router.get("/internships")
def get_internships( country: str = None,remote: bool = None,db: Session = Depends(get_db)):
    query = db.query(Internship)

    filters = []

    if country:
        filters.append(Internship.country == country)
    if remote is not None:
        filters.append(Internship.remote == remote)
    if filters:
        query = query.filter(*filters)

    return query.all()

@router.put("/internships/{id}", response_model=InternshipResponse)
def update_internship(id: int, internship: InternshipUpdate, db: Session=Depends(get_db)):
    item= db.query(Internship).filter(Internship.id == id).first()
    if not item:
        raise HTTPException(status_code=404,detail="Internship not found")
    item.title = internship.title
    item.company = internship.company
    item.country = internship.country
    item.remote = internship.remote
    item.url = internship.url
    db.commit()
    db.refresh(item)
    return item


@router.delete("/internships/{id}")
def delete_internship(id: int , db: Session= Depends(get_db)):
    item = db.query(Internship).filter(Internship.id == id).first()
    if not item:
        raise HTTPException( status_code=404, detail="Internship not found")
    db.delete(item)
    db.commit()
    return {"message": "Internship deleted successfully"}




