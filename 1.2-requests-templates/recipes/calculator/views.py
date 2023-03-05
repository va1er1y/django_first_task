from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def change_recept(request, recept):
    servings = request.GET.get('servings')
    prelimary_recept = dict()
    prelimary_recept['recipe'] = DATA.get(recept).copy()
    if servings:
        quanity = int(servings)
        for key, value in prelimary_recept['recipe'].items():
            prelimary_recept['recipe'][key] = value * quanity
        context = prelimary_recept
    else:
        context = prelimary_recept
    return render(request, 'calculator/index.html', context)