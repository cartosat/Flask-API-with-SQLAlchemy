from flask import request, Response
from model.TblAdmin import TblAdmin
from flask_restful import Resource
from db import db
import hashlib

# Add Admin details.


class AddAdminListResource(Resource):
    def post(self):
        if request.method == 'POST':

            _name = request.json.get('full_name')
            _email = request.json.get('email')
            _phone = request.json.get('phone')
            _password = request.json.get('password')
            _role = request.json.get('role')
            _status = request.json.get('status')

            _hashed_password = hashlib.md5(
                _password.encode('utf8')).hexdigest()

            new_admin = TblAdmin(full_name=_name, email=_email, phone=_phone,
                                 password=_hashed_password, role=_role, status=_status)

            db.session.add(new_admin)
            db.session.commit()

            response = Response("Admin added!!!", 201,
                                mimetype='application/json')
            return response
