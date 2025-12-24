import sys
import simplejson as json
from flask import Flask, jsonify, request
from pydantic import BaseModel, ValidationError

app = Flask(__name__)
rez = 0

# class DataModel(BaseModel):
#     x: int
#     y: int
#
# class InfoModel(BaseModel):
#     name: str
#     lastname: str

json_path = sys.argv[1]

try:
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    parsed_data = DataModel(**data['data'])
    x = parsed_data.x
    y = parsed_data.y
    parsed_data = InfoModel(**data['info'])
    name = parsed_data.name
    lastname = parsed_data.lastname
except (FileNotFoundError, KeyError, ValidationError) as e:
    print(f"Ошибка загрузки данных из JSON: {e}")
    sys.exit(1)

# @app.route("/patchAlfa", methods=["PATCH"])
# def update_y():
#     global y
#     try:
#         data = request.get_json()
#         y = data.get("y", y)
#         return jsonify(message="OK"), 200
#     except Exception as e:
#         return jsonify(message=f"NOT OK {e}"), 400

@app.route("/getRes", methods=["GET"])
def get_result():
    global rez, x, y, name, lastname
    try:
        rez = x + y
        ans = {
            "name": name,
            "lastname": lastname,
            "rez": "OK, COOL" if rez > 0 else "NOT OK, TRY AGAIN"
        }
        return jsonify(ans)
    except Exception as e:
        return jsonify(message=f"NOT OK {e}"), 400

if __name__ == "__main__":
    app.run(port=20000, debug=True)
