from sqlalchemy import Float, Float, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from .base import Base 


class Transaction(Base):
    __tablename__ = 'transactions'
    
    id:         Mapped[str] = mapped_column(UUID, primary_key=True)
    account_id: Mapped[int] = mapped_column(Integer, ForeignKey('accounts.id', ondelete="CASCADE"))
    amount:     Mapped[float] = mapped_column(Float)
    
    account = relationship('Account', back_populates='transactions')