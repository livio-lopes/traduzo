from src.models.history_model import HistoryModel
from src.models.user_model import UserModel
import pytest
from src.database.db import db


@pytest.fixture
def seed_user():
    db.get_collection("users").drop()
    user = {"name": "Joaquim", "level": "admin", "token": "bode"}
    UserModel(user).save()

    return db.get_collection("users").find_one({})


@pytest.fixture
def seed_history():
    db.get_collection("history").drop()
    HistoryModel(
        {
            "text_to_translate": "Hello, I like videogame",
            "translate_from": "en",
            "translate_to": "pt",
        }
    ).save()

    HistoryModel(
        {
            "text_to_translate": "Do you love music?",
            "translate_from": "en",
            "translate_to": "pt",
        }
    ).save()
    return db.get_collection("history").find_one({})


def test_history_delete(app_test, seed_history, seed_user):
    _id = seed_history["_id"]
    user = "Joaquim"
    authorization = "bode"
    response = app_test.delete(
        f"/admin/history/{_id}",
        headers={"Authorization": authorization, "User": user},
    )
    assert response.status_code == 204


def test_history_user_unauthorized(app_test, seed_history, seed_user):
    _id = seed_history["_id"]
    user = "Bode Velho"
    authorization = "senha_errada"
    response = app_test.delete(
        f"/admin/history/{_id}",
        headers={"Authorization": authorization, "User": user},
    )
    assert response.status_code == 401
    assert response.json == {"error": "Unauthorized Access"}


def test_history_token_unathorized(app_test, seed_history, seed_user):
    _id = seed_history["_id"]
    user = "Joaquim"
    authorization = "senha_errada"
    response = app_test.delete(
        f"/admin/history/{_id}",
        headers={"Authorization": authorization, "User": user},
    )
    assert response.status_code == 401
    assert response.json == {"error": "Unauthorized Access"}


def test_history_not_found(app_test, seed_history, seed_user):
    _id = seed_user["_id"]
    user = "Joaquim"
    authorization = "bode"
    response = app_test.delete(
        f"/admin/history/{_id}",
        headers={"Authorization": authorization, "User": user},
    )
    assert response.status_code == 404
    assert response.json == {"error": "History not found"}
