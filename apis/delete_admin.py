from flask import request
from model.TblAdmin import TblAdmin
from flask_restful import Resource
from flask import Response
from db import db

# Delete Admin details from database.


class DeleteAdminListResource(Resource):
    def delete(self, admin_id):
        if request.method == 'DELETE':

            remove_admin = TblAdmin.query.get_or_404(admin_id)

            db.session.delete(remove_admin)
            db.session.commit()

            response = Response("Admin deleted", 201,
                                mimetype='application/json')
            return response
