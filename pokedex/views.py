from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Move, Pokemon, Pokemon_Types, Types, Item, CustomUser


def get_move_identifier(request, move_id):
    try :
        move = Move.objects.get(id=move_id)
        identifier = move.identifier
        return JsonResponse({'identifier ': identifier })
    
    except Move.DoesNotExist :
        return JsonResponse({'error': 'Move not found'}, status=404)
    


def get_pokemon_identifier(request, pokemon_id) :
    try :
        pokemon = Pokemon.objects.get(id=pokemon_id)
        identifier = pokemon.identifier
        return JsonResponse({'identifier ': identifier})
    
    except Pokemon.DoesNotExist :
        return JsonResponse({'error': 'Pokemon not found'}, status=404)
    


def get_pokemon_features(request, pokemon_name) :
    try :
        pokemon = Pokemon.objects.get(identifier=pokemon_name)

        identifier = pokemon.identifier
        height = pokemon.height
        weight = pokemon.weight
        base_experience = pokemon.base_experience

        return JsonResponse({'identifier ': identifier, 'height': height, 'weight': weight, 'base_experience': base_experience})
    
    except Pokemon.DoesNotExist :
        return JsonResponse({'error': 'Pokemon not found'}, status=404)



def get_pokemon_type(request, pokemon_name):
    try:
        pokemon = Pokemon.objects.get(identifier=pokemon_name)
        pokemon_id = pokemon.id
        
        pokemon_type = Pokemon_Types.objects.filter(pokemon_id=pokemon_id).first()
        type_id = pokemon_type.type_id

        if pokemon_type:
            type_of_pokemon = Types.objects.get(id=type_id)
            type_of_pokemon = type_of_pokemon.identifier
            return JsonResponse({'Pokemon': pokemon_name, 'Type': type_of_pokemon})
        else:
            return JsonResponse({'error': 'Pokemon type not found'}, status=404)
    
    except Pokemon.DoesNotExist:
        return JsonResponse({'error': 'Pokemon not found'}, status=404)
    
    except Types.DoesNotExist:
        return JsonResponse({'error': 'Type not found'}, status=404)
    


def get_item_identifier(request, item_id):
    try:
        item = Item.objects.get(id=item_id)
        data = {
            'Identifier': item.identifier
        }
        return JsonResponse(data)
    except Move.DoesNotExist:
        return JsonResponse({'error': 'Item not found'}, status=404)
    


@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        # Récupérer les données de la requête
        data = json.loads(request.body.decode('utf-8')) 
        pseudo = data.get('pseudo')
        password = data.get('password')
        print(data)

        # Vérifier si les champs nécessaires sont fournis
        if not pseudo or not password :
            return JsonResponse({'error': 'Le pseudo et le mot de passe sont requis'}, status=400)

        # Créer un nouvel utilisateur
        try:
            user = CustomUser.objects.create_user(pseudo=pseudo, password=password)
            return JsonResponse({'success': 'Utilisateur créé avec succès'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Méthode non autorisée'}, status=405)

    