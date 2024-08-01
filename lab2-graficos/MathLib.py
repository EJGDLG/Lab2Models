def mat_mult(A, B):
    # Multiplicación de matrices 4x4
    return [[sum(a * b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]

def invert_matrix(matrix):
    # Calcula la inversa de una matriz 4x4
    # Aquí deberías implementar la lógica para calcular la inversa de una matriz 4x4
    # Una implementación común es usando el método de la matriz adjunta y determinante
    pass  # Reemplaza esto con tu implementación real

def TranslationMatrix(x, y, z):
    return [
        [1, 0, 0, x],
        [0, 1, 0, y],
        [0, 0, 1, z],
        [0, 0, 0, 1]
    ]

def ScaleMatrix(x, y, z):
    return [
        [x, 0, 0, 0],
        [0, y, 0, 0],
        [0, 0, z, 0],
        [0, 0, 0, 1]
    ]

def RotationMatrix(pitch, yaw, roll):
    from math import pi, sin, cos
    # Convertir grados a radianes
    pitch *= pi / 180
    yaw *= pi / 180
    roll *= pi / 180


    # Matrices de rotación para cada eje
    pitchMat = [
        [1, 0, 0, 0],
        [0, cos(pitch), -sin(pitch), 0],
        [0, sin(pitch), cos(pitch), 0],
        [0, 0, 0, 1]
    ]

    yawMat = [
        [cos(yaw), 0, sin(yaw), 0],
        [0, 1, 0, 0],
        [-sin(yaw), 0, cos(yaw), 0],
        [0, 0, 0, 1]
    ]

    rollMat = [
        [cos(roll), -sin(roll), 0, 0],
        [sin(roll), cos(roll), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ]

    return mat_mult(mat_mult(pitchMat, yawMat), rollMat)
