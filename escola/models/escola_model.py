from shared.database import Base
from sqlalchemy import Column, Integer


class ContaPagarReceber(Base):
    __tablename__ = 'contas_a_pagar_e_receber'

    id = Column(Integer, autoincrement=True)
