def pretty(d):
    print('cook_book = {')
    for key, value in d.items():
        print("'", str(key), "': [", sep = '')
        for item in value:
            print('\t', item)
        print('\t', '],')
    print('}')

def get_cook_book():
    glossary = {}
    with open('text.txt', 'r', encoding="utf-8") as f:
        glossary = {}
        for line in f:
            if line.find('|') > 0:
                ingredient_name = line[0:line.find('|') - 1]
                ingredient_quantity = line[line.find('|') + 2:line.rfind('|') - 1]
                if line[len(line)-1] == chr(10):
                    measure = line[line.rfind('|') + 2:len(line)-1]
                else:
                    measure = line[line.rfind('|') + 2:len(line)]
                second_glossary = {}
                second_glossary['ingredient_name'] = ingredient_name
                second_glossary['ingredient_quantity'] = ingredient_quantity
                second_glossary['measure'] = measure
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
                name = line[0:len(line)-1]
                empty_list = []
    pretty(glossary)
    return glossary

def get_shop_list_by_dishes(dishes, person_count):
    glossary = get_cook_book()
    ingredients = {}
    ready = {}
    for cook in dishes:
        if cook in glossary.keys():
            for ingredient in glossary.get(cook):
                if ingredient.get('ingredient_name') in ingredients.keys():
                    count_1 = ingredient.get('ingredient_quantity')
                    vremennii = ingredients.get(ingredient.get('ingredient_name'))
                    count_2 = vremennii.get('quantity')
                    total_count = ingredients.get(ingredient.get('quantity')) + glossary.get(cook.get('ingredient_quantity'))
            ingredients = glossary.get(cook)



get_shop_list_by_dishes(['Фахитос', 'Запеченный картофель'], 0)