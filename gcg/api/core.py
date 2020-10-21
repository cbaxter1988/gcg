import http.client as http_status_codes
from functools import wraps

# import psutil
from flask import Flask, jsonify, render_template
from flask_restful import Api
from gcg.api.resources import (
    GCGResource
)
from gcg.schemas.config.ios.ios_base import IOSNodeSchema
from gcg.env import DB_HOST, DB_PORT, DB
from gcg.utils import make_json_response
from mongoengine import connect

# ---- Flask Config ----
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'app/static/uploads'

api = Api(app)

connect(db=DB, host=DB_HOST, port=DB_PORT)

# --- API Registration ---
api.add_resource(GCGResource, "/api/v1/gcg")

template_types = [
    {
        "name": "ios_base_node",
        "url": "/gui/ios_base"

    }

]


# --- Routes ---
@app.route("/gui")
def index():
    return render_template("base.j2", template_types=template_types)


@app.route('/gui/ios_base')
def ios_base():
    fields = [
        {
            "name": "hostname",
            "type": "str"
        },
        {
            "name": "domain",
            "type": "str"
        }

    ]
    schema = IOSNodeSchema()
    print(schema.fields.keys())

    return render_template("ios_base.j2", template_types=template_types, fields=fields)


@app.route("/health")
@app.route("/health_check")
def health_v2():
    return make_json_response(
        data={
            # "cpu_used_percent": psutil.cpu_percent(),
            # "ram_used_percent": psutil.virtual_memory().percent,
            # "ram_avail_percent": psutil.virtual_memory().available * 100 / psutil.virtual_memory().total,
        },
        msg="System is Healthy",
        status_code=http_status_codes.OK
    )


# --- psutil fails on Docker image build, need to troubleshoot, this function returns valuable server info.
# def health_v1():
#     return make_json_response(
#         data={
#             "cpu_used_percent": psutil.cpu_percent(),
#             "ram_used_percent": psutil.virtual_memory().percent,
#             "ram_avail_percent": psutil.virtual_memory().available * 100 / psutil.virtual_memory().total,
#         },
#         msg="System is Healthy",
#         status_code=http_status_codes.OK
#     )


@app.route("/api/v1/login")
def api_login():
    # TODO: Implement login logic, return JWT token to requester.
    return make_json_response(
        data=jsonify({"token": None}),
        msg="Not Implemented",
        status=http_status_codes.NOT_IMPLEMENTED
    )


@app.route("/api/v1/logout")
def api_logout():
    # TODO: Implement logic for logging the requester out.
    return make_json_response(
        data={},
        msg="Not Implemented",
        status=http_status_codes.NOT_IMPLEMENTED
    )


@app.route("/api/v1/register")
def api_register():
    # TODO: Implement logic for registering users that will utilize the API.
    return make_json_response(
        data={},
        msg="Not Implemented",
        status=http_status_codes.NOT_IMPLEMENTED
    )


# --- Helper Funcs and Decorators ---
def token_required(f):
    """
    Use this decorator to protect API calls
    :param f:
    :return:
    """

    @wraps
    def decorated(*args, **kwargs):
        # TODO: Implement JWT authentication logic
        return f(*args, **kwargs)

    return decorated
