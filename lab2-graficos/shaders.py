def vertexShader(vertex, **kwargs):
    #se lleva a cabo para cada vertice
    
    modelMatrix = kwargs["modelMatrix"]
    
    vt = [vetex[0],
          vertex[1],
          vettex[2],
          1]
    vt = modelMatrix @ vt
    
    vt = vt.tolist()[0]
    
    vt = [vt [0] / vt[3],
          vt [1] / vt[3],
          vt [2] / vt[3]]
    
    return vt