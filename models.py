from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

    
class Card(Base):
	__tablename__ = "cards"

	cardid = Column(Integer, primary_key=True, index=True)
	cardname = Column(String, index=True)
    
	fortunes = relationship("Fortune", back_populates="card")
    

class Fortune(Base):
	__tablename__ = "fortunes"

	# composite primary key
	cardid = Column(Integer, ForeignKey("cards.cardid"), primary_key=True)
	cardifreversed = Column(Boolean, primary_key=True)
    
	cardfortune = Column(String, index=True)
    
	card = relationship("Card", back_populates="fortunes")


