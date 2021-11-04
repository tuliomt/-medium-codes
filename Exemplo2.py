items = [25,54,34,67,75,21,77,31]

def rehash(oldhash, table_size):
    return (oldhash+1) % table_size

def lp_hash(item_list, table_size):
    
    lp_hash_table = dict([(i,None) for i,x in enumerate(range(table_size))])

    for item in item_list:
        i = item % table_size
        print("%s hash == %s \n" %(item, i))
        if lp_hash_table[i] == None:
            lp_hash_table[i] = item
        elif lp_hash_table[i] != None:
            print("Colisão, tentativa de sondagem linear \n")
            next_slot = rehash(i, table_size)
            print("Definindo o próximo slot para %s \n" % next_slot)
            while lp_hash_table[next_slot] != None:
                next_slot = rehash(next_slot, len(lp_hash_table.keys()))
                print("O próximo slot não estava vazio, tentando o próximo slot %s \n" % next_slot)
            if lp_hash_table[next_slot] == None:
                lp_hash_table[next_slot] = item
    return lp_hash_table

print(lp_hash(items, 11))
