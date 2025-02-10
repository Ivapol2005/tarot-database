from sqlalchemy.orm import joinedload

from fastapi import FastAPI, Depends
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all


def get_db():
	try:
		db = SessionLocal()
		yield db
	finally:
		db.close()

@app.get("/cards")
def get_cards(db: Session = Depends(get_db)):
	return db.query(models.Card).all()
    

@app.get("/fortunes")
def get_fortunes(db: Session = Depends(get_db)):
	return db.query(models.Fortune).all()


@app.get("/cards_with_fortunes")
def get_cards_with_fortunes(db: Session = Depends(get_db)):
    cards = db.query(models.Card).options(joinedload(models.Card.fortunes)).all()
    
    result = []
    for card in cards:
        card_data = {
            "cardid": card.cardid,
            "cardname": card.cardname,
            "fortunes": [
                {
                    "cardifreversed": fortune.cardifreversed,
                    "cardfortune": fortune.cardfortune
                }
                for fortune in card.fortunes
            ]
        }
        result.append(card_data)
    
    return result

