from flask import request, jsonify, make_response
from functools import wraps
from model.TblAdmin import TblAdmin
from app import app
import jwt
from ma import ma


class ActiveAdminSchema(ma.Schema):
    class Meta:
        fields = ('id', 'email', 'role', 'status')


active_admin_schema = ActiveAdminSchema()


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]
        if not token:

            response = make_response(
                jsonify(
                    {
                        "message": "Authentication Token is missing!",
                        "error": "Unauthorized"
                    }
                ),
                401,
            )
            response.headers["Content-Type"] = "application/json"
            return response
        try:
            data = jwt.decode(
                token, app.config["SECRET_KEY"], algorithms=["HS256"])

            active_admin = TblAdmin.query.filter_by(id=data["id"]).first()

            current_admin = active_admin_schema.dump(active_admin)

            if current_admin is None:
                response = make_response(
                    jsonify(
                        {
                            "message": "Invalid Authentication token!",
                            "data": None,
                            "error": "Unauthorized"
                        }
                    ),
                    401,
                )
                response.headers["Content-Type"] = "application/json"
                return response

            if current_admin['status'] != "Active":
                response = make_response(
                    jsonify(
                        {
                            "message": "Your Account is suspended by Super admin!!!",
                            "error": "Unauthorized",
                            "status": "In-Active"
                        }
                    ),
                    403,
                )
                response.headers["Content-Type"] = "application/json"
                return response

        except jwt.ExpiredSignatureError:
            response = make_response(
                jsonify(
                    {
                        "message": "Token expired. Get new one",
                        "error": "expired"
                    }
                ),
                401,
            )
            response.headers["Content-Type"] = "application/json"
            return response

        except jwt.InvalidTokenError:
            response = make_response(
                jsonify(
                    {
                        "message": "Invalid token!!!",
                        "error": "invalid"
                    }
                ),
                401,
            )
            response.headers["Content-Type"] = "application/json"
            return response

        except Exception as e:
            response = make_response(
                jsonify(
                    {
                        "message": "Something went wrong",
                        "error": str(e)
                    }
                ),
                500,
            )
            response.headers["Content-Type"] = "application/json"
            return response

        return f(current_admin, *args, **kwargs)

    return decorated
