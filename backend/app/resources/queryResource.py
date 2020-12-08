# -*- coding: utf-8 -*-
from flask_restful import Resource, abort
from app.models.company import CompanyModel
from app.models.job_opportunity import JobOpportunityModel
from app.models.student import StudentModel
from app.models.history import History
from app.schemas.company import CompanySchema, StudentCountSchema
from app.schemas.job_opportunity import JobOpportunitySchema
from app.schemas.history import HistorySchema
from app.schemas.averageSalary import AverageSalarySchema

class CompanyTagsResource(Resource):
    def get(self, tag=''):
        try:
            companies = CompanyModel.find_by_tag(tag)

            schema = CompanySchema(many=True)
            json = schema.dump(companies)
        except Exception as e:
            abort(404, message=str(e))

        return json, 201

class CompanyOpportunitiesResource(Resource):
    def get(self, company=''):
        try:
            company = CompanyModel.find_by_name(company)

            if company:
                company_id = company.id
            else:
                company_id = 999999999

            opportunities = JobOpportunityModel.find_by_company_id(company_id)

            schema = JobOpportunitySchema(many=True)
            json = schema.dump(opportunities)
        except Exception as e:
            abort(404, message=str(e))
        
        return json, 201

class StudentHistoryResource(Resource):
    def get(self, student=''):
        try:
            student = StudentModel.find_by_name(student)

            if student:
                student_id = student.id
            else:
                student_id = 99999999

            history = History.find_by_opportunity_professor(student_id)

            schema = HistorySchema()
            json = schema.dump(history)
        except Exception as e:
            abort(404, message=str(e))
        
        return json, 201

class AverageSalaryResource(Resource):
    def get(self, company=''):
        try:
            company = CompanyModel.calculate_average_salary(company)

            schema = AverageSalarySchema()
            json = schema.dump(company)

        except Exception as e:
            abort(404, message=str(e))

        return json, 201

class CompaniesWithMostStudentsResource(Resource):
    def get(self):
        try:
            companies = CompanyModel.find_companies_with_most_students()

            schema = StudentCountSchema(many=True)
            json = schema.dump(companies)

        except Exception as e:
            abort(404, message=str(e))

        return json, 201
