#Anderson Allaica - 7071

padre = [["Javier","Jhon"], ["Jhon","Andres"], ["Jhon","Sebastian"]]

es_padre = input("Ingrese el nombre del padre para conocer a sus hijos: ")

for i in range(len(padre)):
    if (padre[i][0] == es_padre):
        for j in range(len(padre[i])):
            if (padre[i][j] != es_padre):
                print(padre[i][j])