def mat_mult_vec(mat, vec):
    # Multiplicación de una matriz por un vector
    result = [sum(mat[i][j] * vec[j] for j in range(len(vec))) for i in range(len(mat))]
    return result

def VertexShader(vertex, **kwargs):
    modelMatrix = kwargs["modelMatrix"]
    viewMatrix = kwargs["viewMatrix"]
    projectionMatrix = kwargs["projectionMatrix"]
    viewportMatrix = kwargs["viewportMatrix"]

    vt = [vertex[0], vertex[1], vertex[2], 1]  # Convertir el vértice en un tamaño de 4

    # Multiplicación de matrices
    vt = mat_mult_vec(viewportMatrix, 
                      mat_mult_vec(projectionMatrix, 
                                   mat_mult_vec(viewMatrix, 
                                                mat_mult_vec(modelMatrix, vt))))

    # Normalizar el vector resultante
    vt = [vt[0] / vt[3], vt[1] / vt[3], vt[2] / vt[3], 1]
    
    return vt

# Ejemplo de uso
from MathLib import TranslationMatrix, ScaleMatrix, RotationMatrix

modelMatrix = ScaleMatrix(1, 2, 3)
viewMatrix = RotationMatrix(30, 45, 60)
projectionMatrix = TranslationMatrix(1, 2, 3)
viewportMatrix = ScaleMatrix(2, 2, 2)

vertex = [1, 1, 1]

result = VertexShader(vertex, modelMatrix=modelMatrix, viewMatrix=viewMatrix, projectionMatrix=projectionMatrix, viewportMatrix=viewportMatrix)
print(result)
