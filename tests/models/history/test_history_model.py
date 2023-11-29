import json
from src.models.history_model import HistoryModel


# Req. 7
def test_request_history(prepare_base):
    history = json.loads(HistoryModel.list_as_json())
    text_to_translate = ["Hello, I like videogame", "Do you love music?"]
    assert isinstance(history, list)
    for index, data in enumerate(history):
        assert isinstance(data["_id"], str)
        assert data["text_to_translate"] == text_to_translate[index]
        assert data["translate_from"] == "en"
        assert data["translate_to"] == "pt"
