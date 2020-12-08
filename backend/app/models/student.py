# -*- coding: utf-8 -*-
from dao import db, Base
from app.models.association_tables import has_interest, student_tags

class StudentModel(Base):
    __tablename__ = 'Aluno'
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('Empresa.id'), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    recover_email = db.Column(db.String(50))
    year = db.Column(db.Integer, nullable=False)
    phone_number = db.Column(db.String(20))
    company = db.relationship('CompanyModel', back_populates='student')
    tags = db.relationship('TagsModel', secondary=student_tags, back_populates='student')
    opportunities = db.relationship('JobOpportunityModel', secondary=has_interest, back_populates='students')
    history = db.relationship('History', back_populates='student')

    def __init__(self, name, phone_number, contact_email, address, description):
        self.name = name
        self.phone_number = phone_number
        self.contact_email = contact_email
        self.address = address
        self.description = description

    def add_company(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id = _id).first()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def list_all(cls):
        return cls.query.all()