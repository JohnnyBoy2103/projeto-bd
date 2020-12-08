from dao import db, Base

has_interest = db.Table('MostraInteresse', Base.metadata,
    db.Column('student_id', db.Integer, db.ForeignKey('Aluno.id')),
    db.Column('opportunity_id', db.Integer, db.ForeignKey('Vaga.id'))
)

student_tags = db.Table('Escolhe', Base.metadata,
    db.Column('student_id', db.Integer, db.ForeignKey('Aluno.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('Tags.id'))
)

opportunity_tags = db.Table('Tem', Base.metadata,
    db.Column('opportunity_id', db.Integer, db.ForeignKey('Vaga.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('Tags.id'))
)

company_tags = db.Table('Possui', Base.metadata,
    db.Column('company_id', db.Integer, db.ForeignKey('Empresa.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('Tags.id'))
)
