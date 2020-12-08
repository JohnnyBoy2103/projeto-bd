# -*- coding: utf-8 -*-
from marshmallow import Schema, fields

class ProfessorSchema(Schema):
    name = fields.Str()
    email = fields.Str()
    phone_number = fields.Str()
    