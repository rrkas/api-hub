import os

from flask import *

from app.config import conf
from app.csv_gen.generator import generate

csv_gen_bp = Blueprint("csv_gen_bp", __name__)

out_path = os.path.join(conf.OUTPUT_DIR, "csv")
if not os.path.exists(out_path):
    os.makedirs(out_path)


@csv_gen_bp.route("/csv-generate", methods=["GET", "POST"])
def csv_gen_route():
    if request.method == "POST":
        schema = parse_scheme()
        if "count" not in request.args:
            return {"error": "count missing from args!"}
        try:
            count = int(request.args["count"])
        except BaseException as e:
            print(e)
            return {"error": str(e)}
        data = {
            "schema": schema,
            "count": count,
        }
        file_name = generate(schema, count)
        data["file_path"] = request.root_url[:-1] + url_for(
            "csv_gen_bp.file_url", file_name=file_name
        )
        data["file_name"] = file_name + ".csv"
        return data
    return {
        "api-name": "csv-generate",
    }


def parse_scheme():
    if request.is_json:
        data = request.json
    else:
        data = dict(request.form)
    return data


@csv_gen_bp.route("/csv-generate/<string:file_name>")
def file_url(file_name):
    file_path = os.path.join(out_path, file_name + ".csv")
    if not os.path.exists(file_path):
        return {}
    return send_file(file_path)
