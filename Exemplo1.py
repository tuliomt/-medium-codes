items = [25,54,34,67,75,21,77,31]

def hash(item_list, table_size):
    hash_table = dict([(i,None) for i,x in enumerate(range(table_size))])
    for item in item_list:
        i = item % table_size
        print("O hash para %s é %s" % (item, i))
        hash_table[i] = item
    
    return hash_table

hash_table = hash(items, 11)

print(hash_table)

