from flask import request, jsonify, make_response
from datetime import datetime, timedelta
from model.TblAdmin import TblAdmin
from app import app
from flask_restful import Resource
from ma import ma
import jwt
import hashlib


class SingleAdminSchema(ma.Schema):
    class Meta:
        fields = ('id', 'email', 'role', 'status')


admin_schema = SingleAdminSchema()


class AdminLogin(Resource):
    def post(self):
        if request.method == "POST":

            _email = request.json.get("email")
            _password = request.json.get("password")

            _hashed_password = hashlib.md5(
                _password.encode('utf8')).hexdigest()

            admin = TblAdmin.query.filter_by(email=_email).first()

            if admin.password == _hashed_password:
                response = admin_schema.dump(admin)
                response['token'] = jwt.encode(
                    {
                        "id": response['id'],
                        "email": response['email'],
                        'exp': datetime.now() + timedelta(hours=2)
                    },
                    app.config["SECRET_KEY"],
                    algorithm="HS256"
                )
                return response

            else:
                response = make_response(
                    jsonify(
                        {"message": "Wrong Credentials!!!", "severity": "danger"}
                    ),
                    401,
                )
                response.headers["Content-Type"] = "application/json"
                return response
