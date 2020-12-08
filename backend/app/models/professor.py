# -*- coding: utf-8 -*-
from dao import db, Base

class ProfessorModel(Base):
    __tablename__ = 'Professor'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(20))
    status = db.Column(db.Boolean, nullable=False)
    history = db.relationship('History', back_populates='professor')

    def __init__(self, name, email, phone_number, status):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.status = status

    def add_professor(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name = name).first()

    @classmethod
    def list_all(cls):
        return cls.query.all()
