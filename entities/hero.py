from enum import Enum


class HeroClass (Enum):
    INTELLIGENCE = 1
    STRENGTH = 2
    AGILITY = 3

    def __str__(self) -> str:
        return self.name


class Hero:

    def __init__(self, name: str, photo: str,   type: HeroClass):
        self.name = name
        self.photo = photo
        self.type = type

    def __str__(self):
        return f'{self.name} - {self.type}'
