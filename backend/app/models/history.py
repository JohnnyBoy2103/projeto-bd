# -*- coding: utf-8 -*-
from dao import db, Base
from sqlalchemy import desc

class History(Base):
    __tablename__ = 'Historico'
    student_id = db.Column(db.Integer, db.ForeignKey('Aluno.id'), primary_key=True)
    opportunity_id = db.Column(db.Integer, db.ForeignKey('Vaga.id'), primary_key=True)
    professor_id = db.Column(db.Integer, db.ForeignKey('Professor.id'), primary_key=True)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    student = db.relationship('StudentModel', back_populates='history')
    opportunity = db.relationship('JobOpportunityModel', back_populates='history')
    professor = db.relationship('ProfessorModel', back_populates='history')

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
    
    @classmethod
    def find_by_opportunity_professor(cls, student_id):
        return cls.query\
            .filter_by(student_id=student_id)\
            .order_by(desc(cls.start_date))\
            .first()
