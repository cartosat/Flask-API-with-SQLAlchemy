from db import db


class TblAdmin(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(255), nullable=False,
                         default='f91e15dbec69fc40f81f0876e7009648')
    photo = db.Column(db.String(255), nullable=False, default='admin-104.jpg')
    role = db.Column(db.String(30), nullable=False, default='Admin')
    status = db.Column(db.String(10), nullable=False, default='Active')
