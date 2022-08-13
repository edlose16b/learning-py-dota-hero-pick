import string
from typing import List
from entities.hero import Hero, HeroClass
from implementations.api_hero_repository import ApiHeroRepository


def pick_hero(heroes: List[Hero]):
    print('Please, choose your hero:')
    x = 0
    for hero in heroes:
        x += 1
        print(f'{x} {hero.name} - {hero.type}')

    heroId = int(input())

    return heroes[heroId - 1]


def pick_hero_class() -> HeroClass:
    print('Please, choose your hero class:')
    for hero_class in HeroClass:
        print(f'{hero_class.value} - {hero_class.name}')
    hero_class = int(input())

    if (hero_class == 1):
        return HeroClass.INTELLIGENCE
    elif (hero_class == 2):
        return HeroClass.STRENGTH
    elif (hero_class == 3):
        return HeroClass.AGILITY


def main():

    print('Welcome to DOTA2 Pick')
    hero_class = pick_hero_class()
    
    heroRepository = ApiHeroRepository();

    if (hero_class == HeroClass.INTELLIGENCE):
        heroes = heroRepository.get_intelligence_heroes()
    elif (hero_class == HeroClass.STRENGTH):
        heroes = heroRepository.get_strength_heroes()
    elif (hero_class == HeroClass.AGILITY):
        heroes = heroRepository.get_agility_heroes()

    hero = pick_hero(heroes)

    print('You have chosen {} - {}'.format(hero.name, hero.type))


main()
