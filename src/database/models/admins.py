from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base 


class Admin(Base):
    __tablename__ = 'admins'
    
    id:                 Mapped[int] = mapped_column(Integer, primary_key=True)
    full_name:          Mapped[str] = mapped_column(String(50), nullable=False)
    email:              Mapped[str] = mapped_column(String(50), nullable=False)
    hashed_password:    Mapped[str] = mapped_column(String, nullable=False)