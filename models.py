from sqlalchemy import Column, String, BigInteger, CheckConstraint
from database import Base

class Client(Base):
    __tablename__ = "client"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    address = Column(String(255))
    email = Column(String(255))
    first_name = Column(String(255))
    identify = Column(String(255))
    last_name = Column(String(255))
    phone = Column(String(255))
    type_identify = Column(String(255))

    __table_args__ = (
        CheckConstraint(
            "type_identify IN ('CC', 'NIT')",
            name="client_type_identify_check"
        ),
    )
