# -*- coding: utf-8 -*-
from marshmallow import Schema, fields

class StudentSchema(Schema):
    name = fields.Str()
    email = fields.Str()
    recover_email = fields.Str()
    year = fields.Integer()
    phone_number = fields.Str()
