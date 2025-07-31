from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base 


class Account(Base):
    __tablename__ = 'accounts'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
    
    user = relationship('User', back_populates='accounts')
    transactions = relationship('Transaction', back_populates='account')