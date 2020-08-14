
def read_input(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        return [line.split() for line in lines]   

def find_count_items(transactions):
    count_items = {}
    for basket in transactions:
        for i in basket:
            if i in count_items.keys():
                count_items[i] += 1
            else:
                count_items[i] = 1
    return count_items
    
def find_frequent_items(count_items, s):
    #frequent_items = dict([(k, v) for k, v in count_items.values() if v >= s])  ko chay duoc
    frequent_items = {}
    for i in count_items.keys():
        if count_items[i] >= s:
            frequent_items[i] = count_items[i]   
    return frequent_items
   
def find_baskets_frequent_item_appear(frequent_items, baskets):
    
    baskets_frequent_item_appear = {}
    numb_basket = 0
    for basket in baskets:
        numb_basket += 1
        for i in basket:
            if i in frequent_items.keys():
                if i not in baskets_frequent_item_appear:
                    baskets_frequent_item_appear[i] = []
                    baskets_frequent_item_appear[i].append(numb_basket)
                else:
                    baskets_frequent_item_appear[i].append(numb_basket)
                    
    return baskets_frequent_item_appear

def find_association_rules(baskets_frequent_items_appear, s):
    same_basket = []
    for i in baskets_frequent_items_appear.keys():
        for j in baskets_frequent_items_appear.keys():
            if i < j:
                d = [item for item in baskets_frequent_items_appear[i] if item in baskets_frequent_items_appear[j]]
                if len(d) >= s :
                    same_x_y = [i,j,len(d)]
                    same_basket.append(same_x_y)
    return same_basket
    
if __name__ == '__main__':
    inputss = [['a','b'],['a','c','d'], ['a','b']]
    s = 100
    
    inputs = read_input('browsing.txt')
    count_items = find_count_items(inputs)
    frequent_items = find_frequent_items(count_items, s)
    baskets_frequent_items_appear = find_baskets_frequent_item_appear(frequent_items, inputs)
    same_basket = find_association_rules(baskets_frequent_items_appear, s)
    print(same_basket.pop())
    