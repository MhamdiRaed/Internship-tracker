# pyrefly: ignore [missing-import]
from sqlalchemy import Column, Integer, String, Boolean
# pyrefly: ignore [missing-import]
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Internship(Base):
    __tablename__ = "internships"
    id=Column(Integer, primary_key=True,index=True)
    title=Column(String, nullable=False)
    company=Column(String, nullable=False)
    country=Column(String, nullable=True)
    remote=Column(Boolean, default=False)
    url=Column(String, unique=True)