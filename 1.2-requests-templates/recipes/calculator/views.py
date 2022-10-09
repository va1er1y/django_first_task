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

def omlet(request):
    quanity = int(request.GET.get('servings', 1))
    prelimary_recept = dict()
    prelimary_recept.clear()
    prelimary_recept['recipe'] = DATA.get('omlet').copy()
    if quanity == 1:
        context = prelimary_recept

    else:
        for key, value in prelimary_recept['recipe'].items():
            prelimary_recept['recipe'][key] = value * quanity
        context = prelimary_recept
        print(context)
        print(prelimary_recept)
    return render(request, 'calculator/index.html', context)

def pasta(request):
    quanity = int(request.GET.get('servings', 1))
    prelimary_recept = dict()
    prelimary_recept['recipe'] = DATA.get('pasta').copy()
    if quanity == 1:
        context = prelimary_recept.copy()

    else:
        for key, value in prelimary_recept['recipe'].items():
            prelimary_recept['recipe'][key] = value * quanity
        context = prelimary_recept.copy()
    return render(request, 'calculator/index.html', context)

def buter(request):
    quanity = int(request.GET.get('servings', 1))
    prelimary_recept = dict()
    prelimary_recept['recipe'] = DATA.get('buter').copy()
    if quanity == 1:
        context = prelimary_recept.copy()

    else:
        for key, value in prelimary_recept['recipe'].items():
            prelimary_recept['recipe'][key] = value * quanity
        context = prelimary_recept.copy()
    return render(request, 'calculator/index.html', context)

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
