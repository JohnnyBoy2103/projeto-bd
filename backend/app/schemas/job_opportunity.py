# -*- coding: utf-8 -*-
from marshmallow import Schema, fields
from app.schemas.company import CompanySchema
from app.schemas.tags import TagsSchema

class JobOpportunitySchema(Schema):
    title = fields.Str()
    description = fields.Str()
    location = fields.Str()
    grant = fields.Str()
    status = fields.Bool()
    company = fields.Nested(CompanySchema)
    tags = fields.List(fields.Nested(TagsSchema))
