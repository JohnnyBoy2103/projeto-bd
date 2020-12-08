# -*- coding: utf-8 -*-
from flask_restful import Resource, abort
from app.models.company import CompanyModel
from app.schemas.company import CompanySchema

class CompanyResource(Resource):
    def get(self):
        try:
            companies = CompanyModel.list_all()
            schema = CompanySchema(many=True)
            json = schema.dump(companies)
        except Exception as e:
            abort(404, message=str(e))

        return json, 201