# -*- coding: utf-8 -*-
from marshmallow import Schema, fields
from app.schemas.student import StudentSchema
from app.schemas.professor import ProfessorSchema
from app.schemas.job_opportunity import JobOpportunitySchema

class HistorySchema(Schema):
    start_date = fields.Date()
    end_date = fields.Date()
    student = fields.Nested(StudentSchema)
    professor = fields.Nested(ProfessorSchema)
    opportunity = fields.Nested(JobOpportunitySchema)
