def uniqueValues(list1):
    unique_values = set()
    for sublista in list1:
        unique_values.update(sublista)
        print(unique_values)
    return list(unique_values)

def sublist():
    
    num_sublistas = int(input("Ingrese la cantidad de sublistas que desea crear: "))
    list1 = []
    for i in range(num_sublistas):
        sublista = []
        print(f"Ingrese los números para la sublista {i + 1} (ingrese -1 para terminar):")
        while True:
            num = int(input())
            if num == -1:
                break
            sublista.append(num)
        list1.append(sublista)
    unique_values = uniqueValues(list1)
    print("Valores únicos presentes en todas las sublistas:", unique_values)

sublist()