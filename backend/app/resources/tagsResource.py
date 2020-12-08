# -*- coding: utf-8 -*-
from flask_restful import Resource, abort
from app.models.tags import TagsModel
from app.schemas.tags import TagsSchema

class TagsResource(Resource):
    def get(self):
        try:
            tags = TagsModel.list_all()
            schema = TagsSchema(many=True)
            json = schema.dump(tags)
        except Exception as e:
            abort(404, message=str(e))

        return json, 201
