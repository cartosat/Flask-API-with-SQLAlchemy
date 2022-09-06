from app import app
from flask import render_template
from ma import api

# Import resources
from apis.admin_with_id import SingleAdminListResource
from apis.all_admin import AllAdminListResource
from apis.add_admin import AddAdminListResource
from apis.update_admin import UpdateAdminListResource
from apis.delete_admin import DeleteAdminListResource
from apis.upload_file import UploadImage
from apis.admin_login import AdminLogin


api.add_resource(SingleAdminListResource, "/admin/<int:_id>")

api.add_resource(AllAdminListResource, "/all_admin/")

api.add_resource(AddAdminListResource, "/add_admin/")

api.add_resource(UpdateAdminListResource, "/update_admin/<int:_id>")

api.add_resource(DeleteAdminListResource, "/delete_admin/<int:admin_id>")

api.add_resource(UploadImage, '/upload_file')

api.add_resource(AdminLogin, "/admin_login")


# Load home page.
@app.route('/', methods=['GET'])
def home():
    return "Hello, API server is running fine! Use postman to check API's"


if __name__ == "__main__":
    app.run(debug=True)
