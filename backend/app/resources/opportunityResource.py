# -*- coding: utf-8 -*-
from flask_restful import Resource, reqparse, abort
from flask import request
from app.models.job_opportunity import JobOpportunityModel
from app.models.company import CompanyModel
from app.models.tags import TagsModel
from app.schemas.job_opportunity import JobOpportunitySchema

class JobOpportunityResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('opportunity', type = list, location='json')

    def get(self):
        try:
            opportunities = JobOpportunityModel.list_all()
            schema = JobOpportunitySchema(many=True)
            json = schema.dump(opportunities)
        except Exception as e:
            abort(404, message=str(e))

        return json, 201
    
    def post(self):
        try:
            json = request.get_json(force=True)
            company_name = str(json['company'])
            company_id = int(CompanyModel.find_by_name(company_name).id)
            title = json['title']
            description = json['description']
            location = json['location']
            grant = float(json['grant'])
            status = 1

            tag_ids = json['tags']

            tags = TagsModel.find_by_ids(tag_ids)

            opportunity = JobOpportunityModel(company_id, title, description, location, grant, status)
            opportunity.tags.extend(tags)
            opportunity.add_opportunity()
        except Exception as e:
            abort(404, message=str(e))

        return {"message": "OK"}, 201
