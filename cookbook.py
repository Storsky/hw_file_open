from pprint import pprint

def make_cookbook(file_recipes):
    
    with open(file_recipes, 'rt', encoding='utf8') as f:
        cookbook = dict()
        for line in f:
            mealname = line.strip()
            counter = int(f.readline())
            item_list = []
            for item in range(counter):
                name, quantity, measure = f.readline().split('|')
                item_list.append(
                    {'Наименование': name, 'Количество': quantity, 'един. изм.': measure.strip('\n')}
                )
            cookbook[mealname] = item_list
            f.readline()
    return cookbook


def get_shoplist_by_dishes(dishes, guests):
    shop_list = {}
    cookbook = make_cookbook('recipes.txt')
    for dish in dishes:
        for ing in cookbook[dish]:
            key = ing['Наименование']
            measure = ing['един. изм.']
            quan = int(ing['Количество'])*int(guests)
            if key not in shop_list:
                shop_list[key] = {'measure': measure, 'quantity': quan}        
            else:
                shop_list[key]['quantity'] += quan
    return shop_list



pprint(get_shoplist_by_dishes(['Омлет', 'Фахитос'],3))
