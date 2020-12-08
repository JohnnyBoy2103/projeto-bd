# -*- coding: utf-8 -*-
from marshmallow import Schema, fields

class TagsSchema(Schema):
    name = fields.Str()
    value = fields.Integer()
    