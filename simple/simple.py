import random

def simple_list():
    lista_de_diccionarios = []
    try:
        for i in range(1, 11):
            diccionario = {
                "id": i,
                "age": random.randint(1, 100) 
            }
            lista_de_diccionarios.append(diccionario)
        return lista_de_diccionarios
    except (OSError, IOError) as e:
        print(f"Error: {e}")
        exit(1)

def sort_list(dicts):
    sorted_list = sorted(dicts, key=lambda x: x["age"])
    return sorted_list
