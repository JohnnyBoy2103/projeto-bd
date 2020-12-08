# # -*- coding: utf-8 -*-
from app import create_app
from dao import db
from app.models.company import CompanyModel
from app.models.student import StudentModel
from app.models.professor import ProfessorModel
from app.models.tags import TagsModel
from app.models.job_opportunity import JobOpportunityModel
from app.models.history import History
from app.models.association_tables import *

app = create_app()

@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000,debug=True)
