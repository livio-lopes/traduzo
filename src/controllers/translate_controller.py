from models.language_model import LanguageModel
from flask import render_template, Blueprint, request
from deep_translator import GoogleTranslator

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


@translate_controller.post("/")
def translate():
    text_to_translate = request.form.get("text-to-translate")
    translate_from = request.form.get("translate-from")
    translate_to = request.form.get("translate-to")
    translated = GoogleTranslator(
        source=translate_from or "auto", target=translate_to
    ).translate(text_to_translate)
    data = {
        "languages": LanguageModel.list_dicts(),
        "text_to_translate": text_to_translate,
        "translate_from": translate_from,
        "translate_to": translate_to,
        "translated": translated,
    }

    return render_template("index.html", **data)


@translate_controller.post("/reverse")
def reverse():
    text_to_translate = request.form.get("text-to-translate")
    translate_from = request.form.get("translate-from")
    translate_to = request.form.get("translate-to")
    translated = GoogleTranslator(
        source=translate_from or "auto", target=translate_to
    ).translate(text_to_translate)
    data = {
        "languages": LanguageModel.list_dicts(),
        "text_to_translate": translated,
        "translate_from": translate_to,
        "translate_to": translate_from,
        "translated": text_to_translate,
    }
    return render_template("index.html", **data)
