from abc import abstractmethod
from html import entities
from typing import List
from entities.hero import Hero


class HeroRepository():
    @abstractmethod
    def get_heroes(self) -> List[Hero]:
        pass

    @abstractmethod
    def get_intelligence_heroes(self) -> List[Hero]:
        pass

    @abstractmethod
    def get_strength_heroes(self) -> List[Hero]:
        pass

    @abstractmethod
    def get_agility_heroes(self) -> List[Hero]:
        pass
