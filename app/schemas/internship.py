from typing import Optional
from pydantic import BaseModel

class InternshipCreate(BaseModel):
    title:str
    company:str
    country:str
    remote:bool
    url:str

class InternshipResponse(BaseModel):
    id:int
    title:str
    company:str
    country:str
    remote:bool
    url:str

class InternshipUpdate(BaseModel):
    title:str
    company:str
    country:str
    remote:bool
    url:str

class InternshipPatch(BaseModel):
    title: Optional[str] = None
    company: Optional[str] = None
    country: Optional[str] = None
    remote: Optional[bool] = None
    url: Optional[str] = None