# pyrefly: ignore [missing-import]
from app.db.models import Base
# pyrefly: ignore [missing-import]
from sqlalchemy import create_engine
# pyrefly: ignore [missing-import]
from sqlalchemy.orm import sessionmaker
# pyrefly: ignore [missing-import]
from sqlalchemy.orm import Session

DATABASE_URL = "postgresql://raedmhamdi:12345@localhost:5432/internships_db"

# engine = connection manager
engine = create_engine(DATABASE_URL)

# session factory (creates sessions per request)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base.metadata.create_all(bind=engine)