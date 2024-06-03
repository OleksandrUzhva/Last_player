from enum import StrEnum, auto
from functools import lru_cache

class Positions(StrEnum):
    SUPPORT = auto()
    MID = auto()
    TANK= auto()

    @classmethod
    @lru_cache(maxsize=1)
    def users(cls) -> list[str]:
        return [cls.SUPPORT, cls.MID, cls.TANK]

    @classmethod
    @lru_cache(maxsize=1)
    def users_value(cls) -> list[str]:
        return [cls.SUPPORT.value, cls.MID.value, cls.TANK.value]

    @classmethod
    @lru_cache(maxsize=1)
    def choices(cls) -> list[tuple[str, str]]:
        results = []

        for element in cls:
            _element = (element.value, element.name.lower().capitalize())
            results.append(_element)

        return results