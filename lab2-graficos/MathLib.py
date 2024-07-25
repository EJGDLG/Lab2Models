from math import pi, sin, cos

def TranslationMatrix(x, y, z):
    return [[1, 0, 0, x],
            [0, 1, 0, y],
            [0, 0, 1, z],
            [0, 0, 0, 1]]

def ScaleMatrix(x, y, z):
    return [[x, 0, 0, 0],
            [0, y, 0, 0],
            [0, 0, z, 0],
            [0, 0, 0, 1]]

def matrix_multiply(A, B):
    result = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
    
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

def RotationMatrix(pitch, yaw, roll):
    # Convertir primero en radianes
    pitch *= pi / 180
    yaw *= pi / 180
    roll *= pi / 180
    
    # Crear la Matriz de rotación para cada eje
    pitchMat = [[1, 0, 0, 0],
                [0, cos(pitch), -sin(pitch), 0],
                [0, sin(pitch), cos(pitch), 0],
                [0, 0, 0, 1]]
    
    yawMat = [[cos(yaw), 0, sin(yaw), 0],
              [0, 1, 0, 0],
              [-sin(yaw), 0, cos(yaw), 0],
              [0, 0, 0, 1]]
    
    rollMat = [[cos(roll), -sin(roll), 0, 0],
               [sin(roll), cos(roll), 0, 0],
               [0, 0, 1, 0],
               [0, 0, 0, 1]]
    
    return matrix_multiply(matrix_multiply(pitchMat, yawMat), rollMat)

# Ejemplo de uso
trans_matrix = TranslationMatrix(1, 2, 3)
scale_matrix = ScaleMatrix(2, 2, 2)
rot_matrix = RotationMatrix(45, 45, 45)

