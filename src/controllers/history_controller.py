from models.history_model import HistoryModel
from flask import Blueprint, jsonify
import json


history_controller = Blueprint("history", __name__)


@history_controller.get("/")
def index():
    json_data = jsonify(json.loads(HistoryModel.list_as_json()))
    status_code = 200
    return json_data, status_code
