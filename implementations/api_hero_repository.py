
from sys import implementation
from typing import List
from repositories.hero_repository import HeroRepository
from entities.hero import Hero, HeroClass


heroes = [
    Hero('Abbadon', 'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/abaddon.png', HeroClass.STRENGTH),
    Hero('Alchemist', 'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/alchemist.png', HeroClass.STRENGTH),
    Hero('Ancient Apparition', 'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/ancient_apparition.png', HeroClass.INTELLIGENCE),
    Hero('Anti-Mage', 'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/antimage.png', HeroClass.AGILITY),
    Hero('Axe', 'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/axe.png', HeroClass.STRENGTH),
    Hero('Bane', 'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/bane.png',
         HeroClass.INTELLIGENCE),
    Hero('Batrider', 'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/batrider.png',
         HeroClass.INTELLIGENCE),
    Hero('Beastmaster', 'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/beastmaster.png', HeroClass.STRENGTH),
    Hero('Bloodseeker', 'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/bloodseeker.png', HeroClass.AGILITY),
    Hero('Bounty Hunter', 'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/bounty_hunter.png', HeroClass.AGILITY),
    Hero('Brewmaster', 'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/brewmaster.png', HeroClass.STRENGTH),
    Hero('Bristleback', 'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/bristleback.png', HeroClass.STRENGTH),
    Hero('Broodmother', 'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/broodmother.png', HeroClass.STRENGTH),
    Hero('Centaur Warrunner', 'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/centaur.png', HeroClass.STRENGTH),
    Hero('Chaos Knight', 'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/chaos_knight.png', HeroClass.STRENGTH),
    Hero('Chen', 'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/chen.png',
         HeroClass.INTELLIGENCE),
    Hero('Clinkz', 'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/clinkz.png', HeroClass.AGILITY),
    Hero('Clockwerk', 'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/clockwerk.png', HeroClass.STRENGTH),
    Hero('Crystal Maiden', 'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/crystal_maiden.png', HeroClass.INTELLIGENCE),
    Hero('Dark Seer', 'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/dark_seer.png', HeroClass.INTELLIGENCE),
    Hero('Dazzle', 'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/dazzle.png',
         HeroClass.INTELLIGENCE),
    Hero('Death Prophet', 'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/death_prophet.png', HeroClass.INTELLIGENCE),
    Hero('Disruptor', 'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/disruptor.png', HeroClass.AGILITY),
    Hero('Doom', 'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/doom_bringer.png',
         HeroClass.INTELLIGENCE),
    Hero('Dragon Knight', 'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/dragon_knight.png', HeroClass.STRENGTH),
    Hero('Drow Ranger', 'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/drow_ranger.png', HeroClass.AGILITY),
    Hero('Earthshaker', 'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/earthshaker.png', HeroClass.STRENGTH),
    Hero('Elder Titan', 'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/elder_titan.png', HeroClass.STRENGTH),
    Hero('Ember Spirit', 'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/ember_spirit.png', HeroClass.AGILITY),
    Hero('Enchantress', 'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/enchantress.png', HeroClass.INTELLIGENCE),
    Hero('Enigma', 'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/enigma.png',
         HeroClass.INTELLIGENCE),
    Hero('Faceless Void', 'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/faceless_void.png', HeroClass.INTELLIGENCE),
    Hero('Gyrocopter', 'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/gyrocopter.png', HeroClass.AGILITY),
    Hero('Huskar', 'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/huskar.png', HeroClass.STRENGTH),
]


class ApiHeroRepository(HeroRepository):
    def get_heroes(self) -> List[Hero]:
        return heroes

    def get_intelligence_heroes(self) -> List[Hero]:
        return [hero for hero in heroes if hero.type == HeroClass.INTELLIGENCE]

    def get_strength_heroes(self) -> List[Hero]:
        return [hero for hero in heroes if hero.type == HeroClass.STRENGTH]

    def get_agility_heroes(self) -> List[Hero]:
        return [hero for hero in heroes if hero.type == HeroClass.AGILITY]
