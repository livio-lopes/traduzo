from models.abstract_model import AbstractModel
from database.db import db


class LanguageModel(AbstractModel):
    _collection = db["languages"]

    def __init__(self, data: dict[str, str]):
        super().__init__(data)

    def to_dict(self) -> dict[str, str]:
        del self.data["_id"]
        return self.data

    @classmethod
    def list_dicts(cls) -> list[dict[str, str]]:
        return [language.to_dict() for language in cls.find()]
