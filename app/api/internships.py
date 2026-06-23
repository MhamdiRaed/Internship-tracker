from fastapi import APIRouter, Depends, HTTPException
# pyrefly: ignore [missing-import]
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models import Internship
from app.schemas.internship import InternshipCreate, InternshipResponse

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
    db.add(db_internship)
    db.commit()
    db.refresh(db_internship)
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