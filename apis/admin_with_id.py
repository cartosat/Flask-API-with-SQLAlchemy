from flask_restful import Resource
from flask import Response
from model.TblAdmin import TblAdmin
from ma import ma

# Get Admin with specific id


class SingleAdminSchema(ma.Schema):
    class Meta:
        fields = ('id', 'full_name', 'email',
                  'phone', 'photo', 'role', 'status')


admin_schema = SingleAdminSchema()


class SingleAdminListResource(Resource):
    def get(self, _id):

        admin = TblAdmin.query.filter_by(id=_id).first()
        response = admin_schema.dump(admin)
        try:
            response['id']
            return response
        except:
            response = Response("Admin with specified id was not found in Database!!!", 400,
                                mimetype='application/json')
            return response
