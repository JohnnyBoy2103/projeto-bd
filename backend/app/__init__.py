# -*- coding: utf-8 -*-
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from app.config import Config
from app.resources.opportunityResource import JobOpportunityResource
from app.resources.companyResource import CompanyResource
from app.resources.tagsResource import TagsResource
from app.resources.queryResource import *

from dao import db

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    CORS(app, resources={r'/*': {'origins': '*'}})

    api = Api(app)

    api.add_resource(JobOpportunityResource, '/vaga')
    api.add_resource(TagsResource, '/tags')
    api.add_resource(CompanyResource, '/empresa')
    api.add_resource(CompanyTagsResource, '/query-tags/', '/query-tags/<string:tag>')
    api.add_resource(CompanyOpportunitiesResource, '/query-vagas/', '/query-vagas/<string:company>')
    api.add_resource(StudentHistoryResource, '/query-historico/', '/query-historico/<string:student>')
    api.add_resource(AverageSalaryResource, '/query-salario-medio/', '/query-salario-medio/<string:company>')
    api.add_resource(CompaniesWithMostStudentsResource, '/query-maiores-contratadoras')

    return app
    