import os
from flask import request
from flask_restful import Resource
from flask import Response
from app import app
from werkzeug.utils import secure_filename


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower(
           ) in app.config['ALLOWED_EXTENSIONS']


class UploadImage(Resource):
    def post(self):
        file = request.files['file']
        if file and allowed_file(file.filename):
            # From flask uploading tutorial
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            response = Response("File successfully uploaded!!!", 201,
                                mimetype='application/json')
            return response
        else:
            response = Response("File upload failed!!!", 400,
                                mimetype='application/json')
            return response
