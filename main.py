from pprint import pprint

def pretty(d):
    print('cook_book = {')
    for key, value in d.items():
        print("'", str(key), "': [", sep='')
        for item in value:
            print('\t', item)
        print('\t', '],')
    print('}')

def get_cook_book():
    with open('text.txt', 'r', encoding="utf-8") as f:
        glossary = {}
        for line in f:
            if line.find('|') > 0:
                ingredient_name = line[0:line.find('|') - 1]
                ingredient_quantity = line[line.find('|') + 2:line.rfind('|') - 1]
                if line[len(line) - 1] == chr(10):
                    measure = line[line.rfind('|') + 2:len(line) - 1]
                else:
                    measure = line[line.rfind('|') + 2:len(line)]
                second_glossary = {'ingredient_name': ingredient_name, 'ingredient_quantity': ingredient_quantity,
                                   'measure': measure}
                empty_list.append(second_glossary)
                glossary[name] = empty_list
                # ингридиент
            elif line[0].isdigit():
                empty_list = []
                # print('количество ингридиентов')
                # количество ингридиентов
            elif line == chr(10):
                empty_list = []
                # print('пустая строка')
                # пустая строка
            else:
                name = line[0:len(line) - 1]
                empty_list = []
    # pretty(glossary)
    return glossary

def get_shop_list_by_dishes(dishes, person_count):
    glossary = get_cook_book()
    ingredients = {}
    ready = {}
    for cook in dishes:
        if cook in glossary.keys():
            for ingredient in glossary.get(cook):
                if ingredient.get('ingredient_name') in ingredients.keys():
                    ready = ingredients[ingredient.get('ingredient_name')]
                    ready['measure'] = ingredient.get('measure')
                    count = person_count * int(ingredient.get('ingredient_quantity'))
                    ready['quantity'] += count
                else:
                    ready['measure'] = ingredient.get('measure')
                    ready['quantity'] = int(ingredient.get('ingredient_quantity')) * person_count
                ingredients[ingredient.get('ingredient_name')] = ready.copy()
    return ingredients

pprint(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 10))
