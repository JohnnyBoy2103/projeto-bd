# -*- coding: utf-8 -*-
from dao import db, Base
from app.models.association_tables import student_tags, opportunity_tags, company_tags

class TagsModel(Base):
    __tablename__ = 'Tags'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    value = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    student = db.relationship('StudentModel', secondary=student_tags, back_populates='tags')
    opportunity = db.relationship('JobOpportunityModel', secondary=opportunity_tags, back_populates='tags')
    company = db.relationship('CompanyModel', secondary=company_tags, back_populates='tags')

    def __init__(self, name, value, status):
        self.name = name
        self.value = value
        self.status = status
    
    def add_tag(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_ids(cls, ids):
        return cls.query.filter(cls.id.in_(ids))

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id =_id).first()

    @classmethod
    def list_all(cls):
        return cls.query.filter_by(status = 1).all()
