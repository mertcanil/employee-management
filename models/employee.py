from datetime import datetime
from services.database import db 

class Employee(db.Model):
    __tablename__ = "employee"
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    birth_date = db.Column(db.DateTime)
    street = db.Column(db.String(255))
    house_number = db.Column(db.String(128))
    zip_code = db.Column(db.String(32))
    city = db.Column(db.String(255))
    position = db.Column(db.String(255))
    created_date = db.Column(db.DateTime)

    def __init__(self, firstname: str, lastname: str, birth_date: datetime, street: str, house_number: str, 
    zip_code: str, city: str, position: str):
        self.firstname = firstname 
        self.lastname = lastname 
        self.birth_date = birth_date
        self.street = street 
        self.house_number = house_number
        self.zip_code = zip_code 
        self.city = city 
        self.position = position
        self.created_date = datetime.now()

    def insert(self):
        db.session.add(self)
        db.session.commit()