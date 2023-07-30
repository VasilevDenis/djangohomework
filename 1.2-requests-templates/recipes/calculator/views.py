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
    context = get_recipe(request, 'omlet')
    return render(request, 'calculator/index.html', context)


def pasta(request):
    context = get_recipe(request, 'pasta')
    return render(request, 'calculator/index.html', context)


def buter(request):
    context = get_recipe(request, 'buter')
    return render(request, 'calculator/index.html', context)


def get_recipe(request, meal):
    print(meal)
    servings = request.GET.get('servings')
    if servings is None:
        servings = 1
    else:
        servings = int(servings)
    new_data = DATA[meal].copy()
    print(DATA, new_data)
    for key, value in new_data.items():
        new_data[key] = value * servings
    context = {"recipe": new_data}
    return context


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
