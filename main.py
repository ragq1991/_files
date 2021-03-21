def pretty(d, indent=0):
    for key, value in d.items():
        print('\t' * indent + str(key))
        for item in value:
            print('\t', item)

def get_cook_book():
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
                # print('наименование блюда')
                # наименование блюда
        pretty(glossary)

get_cook_book()