# -*- coding: utf-8 -*-
from marshmallow import Schema, fields
from app.schemas.tags import TagsSchema

class CompanySchema(Schema):
    name = fields.Str()
    phone_number = fields.Str()
    contact_email = fields.Str()
    address = fields.Str()
    description = fields.Str()
    tags = fields.List(fields.Nested(TagsSchema))

class StudentCountSchema(Schema):
    name = fields.Str()
    count = fields.Integer()
