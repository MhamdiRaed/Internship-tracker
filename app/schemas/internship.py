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
