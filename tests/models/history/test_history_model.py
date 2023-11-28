import json
from src.models.history_model import HistoryModel


# Req. 7
def test_request_history(prepare_base):
    history = json.loads(HistoryModel.list_as_json())
    TEXT_TO_TRANSLATE = "text_to_translate"
    TRANSLATE_FROM = "translate_from"
    TRANSLATE_TO = "translate_to"
    TEXT_TO_TRANSLATE_EXPECTED = (
        "Hello, I like videogame".casefold() or "Do you love music?".casefold()
    )
    assert isinstance(history, list)
    for data in history:
        assert isinstance(data["_id"], str)
        assert TEXT_TO_TRANSLATE in data
        assert data[TEXT_TO_TRANSLATE].casefold() == TEXT_TO_TRANSLATE_EXPECTED

        assert TRANSLATE_FROM in data
        assert data[TRANSLATE_FROM].casefold() == "en".casefold()
        assert TRANSLATE_TO in data
        assert data[TRANSLATE_TO].casefold() == "pt".casefold()
