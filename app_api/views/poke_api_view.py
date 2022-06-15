from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
import requests
from app_api.models import Game, Pokemon, Type


from app_api.models.egg_group import EggGroup

class PokeApiView(ViewSet):
    """Filling out database from pokeapi"""
    @action(methods=['get'], detail=False)
    def get_games(self, request):
        games = requests.get('https://pokeapi.co/api/v2/version?limit=36').json()
        
        for game in games['results']:
            Game.objects.create(title=game['name'].capitalize())
            
        return Response(None)
    
    @action(methods=['get'], detail=False)
    def get_pokemon(self, request):
        pokemons = requests.get('https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0').json()
        
        for pokemon in pokemons['results']:
            created_pokemon = Pokemon.objects.create(name=pokemon['name'].capitalize())
            current_pokemon = requests.get(pokemon['url']).json()
            created_pokemon.default_sprite=current_pokemon['sprites']['front_shiny']
            
            if current_pokemon['sprites']['front_shiny_female'] is not None:
                created_pokemon.female_sprite = current_pokemon['sprites']['front_shiny_female']
                
            created_pokemon.save()
            
            games_list = []
            
            for game in current_pokemon['game_indices']:
                games_list.append(game['version']['url'].split('/')[-2])
                
            created_pokemon.games.add(*games_list)
            
        return Response(None)
    
    @action(methods=['get'], detail=False)
    def get_types(self, request):
        types = requests.get('https://pokeapi.co/api/v2/type').json()
        
        for type in types['results']:
            created_type = Type.objects.create(label=type['name'])
            
            current_type = requests.get(type['url']).json()
            
            
            pokemons = []
            
            for pokemon in current_type['pokemon']:
                current_pokemon = pokemon['pokemon']['url'].split('/')[-2]
                if len(current_pokemon) <= 3:
                    pokemons.append(current_pokemon)
                
            created_type.pokemon.add(*pokemons)
            
        return Response(None)
    
    @action(methods=['get'], detail=False)
    def get_egg_groups(self, request):
        egg_groups = requests.get('https://pokeapi.co/api/v2/egg-group').json()
        
        for egggroup in egg_groups['results']:
            created_egggroup = EggGroup.objects.create(name=egggroup['name'])
            
            current_egggroup = requests.get(egggroup['url']).json()
            
            
            pokemons = []
            
            for pokemon in current_egggroup['pokemon_species']:
                current_pokemon = pokemon['url'].split('/')[-2]
                if len(current_pokemon) <= 3:
                    pokemons.append(current_pokemon)
                
            created_egggroup.pokemon.add(*pokemons)
            
        return Response(None)
    
            