from models.language_model import LanguageModel
from flask import render_template, Blueprint


translate_controller = Blueprint("translate", __name__)


@translate_controller.get("/")
def index():
    data = {
        "languages": LanguageModel.list_dicts(),
        "text_to_translate": "O que deseja traduzir?",
        "translate_from": "pt",
        "translate_to": "en",
        "translated": "What do you want to translate?",
    }

    return render_template("index.html", **data)
