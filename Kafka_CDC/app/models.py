from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class MyTable(Base):
    __tablename__ = "my_table"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    value = Column(String(255))
    created_at = Column(DateTime)
