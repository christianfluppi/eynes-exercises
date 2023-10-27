def transpose(matrix):
    #Obtengo el numero de filas y columnas de la matriz
    filas = len(matrix)
    columnas = len(matrix[0])

    #Inicializo la transpuesta con todos los valores en 0 (cero)
    transpuesta = [[0 for _ in range(filas)] for _ in range(columnas)]
