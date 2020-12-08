# -*- coding: utf-8 -*-
from sqlalchemy.sql import func
from dao import db, Base
from app.models.association_tables import has_interest, opportunity_tags
class JobOpportunityModel(Base):
    __tablename__ = 'Vaga'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    company_id = db.Column(db.Integer, db.ForeignKey('Empresa.id'), primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(50), nullable=False)
    grant = db.Column(db.Numeric(7,2), nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    company = db.relationship('CompanyModel', back_populates='opportunity')
    students = db.relationship('StudentModel', secondary=has_interest, back_populates='opportunities')
    tags = db.relationship('TagsModel', secondary=opportunity_tags, back_populates='opportunity')
    history = db.relationship('History', back_populates='opportunity')

    def __init__(self, company_id, title, description, location, grant, status):
        self.company_id = company_id
        self.title = title
        self.description = description
        self.location = location
        self.grant = grant
        self.status = status

    def add_opportunity(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id =_id).first()

    @classmethod
    def find_by_company_id(cls, company_id):
        return cls.query.filter((company_id == cls.company_id) & (cls.status == 1)).all()

    @classmethod
    def list_all(cls):
        return cls.query.filter_by(status = 1).all()
       