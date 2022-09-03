from flask import request, Response
from model.TblAdmin import TblAdmin
from flask_restful import Resource
from db import db
import hashlib

# Update Admin details.


class UpdateAdminListResource(Resource):
    def put(self, _id):
        if request.method == 'PUT':

            admin_to_update = TblAdmin.query.filter_by(id=_id).first()

            updated_info = request.get_json()
            update_fields = updated_info.keys()

            for i in update_fields:
                if i == 'full_name':
                    admin_to_update.full_name = updated_info[i]

                elif i == "email":
                    admin_to_update.email = updated_info[i]

                elif i == "password":
                    _hashed_password = hashlib.md5(
                        updated_info[i].encode('utf8')).hexdigest()

                    admin_to_update.password = _hashed_password

                elif i == "phone":
                    admin_to_update.phone = updated_info[i]

                elif i == "role":
                    admin_to_update.role = updated_info[i]

                elif i == "status":
                    admin_to_update.status = updated_info[i]

                else:
                    pass

            db.session.commit()

            response = Response("Admin Updated!!!", 201,
                                mimetype='application/json')
            return response
