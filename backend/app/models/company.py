# -*- coding: utf-8 -*-
from dao import db, Base
from sqlalchemy import desc
from sqlalchemy.sql import func
from app.models.tags import TagsModel
from app.models.association_tables import company_tags
from app.models.history import History
from app.models.job_opportunity import JobOpportunityModel

class CompanyModel(Base):
    __tablename__ = 'Empresa'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    contact_email = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)
    opportunity = db.relationship('JobOpportunityModel', back_populates='company')
    student = db.relationship('StudentModel', back_populates='company')
    tags = db.relationship('TagsModel', secondary=company_tags, back_populates='company')

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
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_tag(cls, tag):
        return cls.query\
            .join(company_tags, cls.id == company_tags.c.company_id)\
            .join(TagsModel, TagsModel.id == company_tags.c.tag_id)\
            .filter(TagsModel.name == tag)\
            .all()
    
    @classmethod
    def find_companies_with_most_students(cls):
        return db.session.query(CompanyModel.name, func.count(History.student_id).label('count'))\
            .join(JobOpportunityModel, cls.id == JobOpportunityModel.company_id)\
            .join(History, JobOpportunityModel.id == History.opportunity_id)\
            .group_by(cls.id)\
            .order_by(desc('count'))\
            .limit(3)
    
    @classmethod
    def calculate_average_salary(cls, company):
        return db.session.query(cls.name, func.avg(JobOpportunityModel.grant).label('avg'))\
            .join(JobOpportunityModel, cls.id == JobOpportunityModel.company_id)\
            .group_by(cls.id)\
            .filter(cls.name == company)\
            .first()

    @classmethod
    def list_all(cls):
        return cls.query.all()
