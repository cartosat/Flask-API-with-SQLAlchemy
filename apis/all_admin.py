from flask_restful import Resource
from model.TblAdmin import TblAdmin
from authentication import token_required
from ma import ma

# Get all Admins


class AllAdminSchema(ma.Schema):
    class Meta:
        fields = ('id', 'full_name', 'email',
                  'phone', 'photo', 'role', 'status')


all_admin_schema = AllAdminSchema()
all_admin_schema = AllAdminSchema(many=True)


class AllAdminListResource(Resource):
    @token_required
    def get(self, current_admin):
        admins = TblAdmin.query.all()
        return all_admin_schema.dump(admins)
