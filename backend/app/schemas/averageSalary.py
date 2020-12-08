# -*- coding: utf-8 -*-
from marshmallow import Schema, fields

class AverageSalarySchema(Schema):
    name = fields.Str()
    avg = fields.Float()
