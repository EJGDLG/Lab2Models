import struct

def char(c):
    return struct.pack("=c", c.encode("ascii"))

def word(w):
    return struct.pack("=h", w)

def dword(d):
    return struct.pack("=l", d)



class Renderer(object):
    def __init__(self, screen):
        
        self.screen = screen
        _, _,self.width, self.height = screen.get_rect()
        
        self.glColor(1, 1, 1)
        self.glClearColor(0, 0, 0)
        self.glclear()
        
        self.vertexShader = None
        
        self.models = []
        
    def glColor(self, r, g, b):
        r = min(1, max(0, r))
        g = min(1, max(0, g))
        b = min(1, max(0, b))
        
        self.currColor = [r, g, b]
    
    def glClearColor(self, r, g, b):
        r = min(1, max(0, r))
        g = min(1, max(0, g))
        b = min(1, max(0, b))
        
        self.clearColor = [r, g, b]
        
    def glClear(self):
        color = [int(i * 255) for i in self.clearColor]
        self.screen.fill(color)
        
        self.frameBuffer = [[self.clearColor for y in range(self.height)]
                            for x in range(self.width)]
        
    def glPoint(self, x, y, color = None):
        # Pygame empieza a renderizar desde la esquina superior izquierda
        if (0 <= x < self.width) and (0 <= y < self.height):
            # Pygame recibe los colores en un rango de 0 a 255
            color = [int(i * 255) for i in (color or self.currColor)]
            self.screen.set_at((x, self.height - 1 - y), color)
            
            self.fremaBuffer[x][y] = color
            
    def glLine(self, v0, v1, color = None):
        
        x0 = int(v0[0])
        x1 = int(v1[0])
        y0 = int(v0[0])
        y1 = int(v1[0])
        
        if x0 == x1 and y0 == y1:
            self.glPoint(x0,y0)
            return
        dy = abs(y1 - y0)
        dx = abs(x1 - x0)
        
        steep = dy > dx
        
        if steep:
            x0, y0 = y0, x0
            x1, y1 = y1, x1
            
        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0
            
        dy = abs(y1 - y0)
        dx = abs(x1 - x0)
        
        offset = 0
        limit = 0.75
        m = dy / dx
        y = y0
        
        for x in range(x0, x1 + 1):
            if steep:
                self.glPoint(y, x, color or self.currColor)
            else:
                self.glPoint(x, y, color or self.currColor)
                
            offset += m
            
            if offset >= limit:
                if y0 < y1:
                    y += 1
                else:
                    y -= 1
                    
    def glGenerateFrameBuffer(self , filename):
        
        with open(filename, "wb") as file:
            file.write(char("B"))
            file.write(char("M"))
            file.write(dword(14 + 40 + (self.width * self.height * 3)))
            file.write(dword(0))
            file.write(dword(14 + 40))
            
            file.write(dword(40))
            file.write(dword(self.width))
            file.write(dword(self.height))
            file.write(dword(1))
            file.write(dword(24))
            file.write(dword(0))
            file.write(dword(self.width * self.height * 3))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))
            
            
            for y in range(self.height):
                for x in range(self.width):
                    color = self.frameBuffer[x][y]
                    color = bytes([color[2],color[1],color[0]])
                    
                    file.write(color)
                    
    def glRender(self):
        
        for model in self.models:
            mMat= model.GetModelMatrix()
            
            for face in model.faces:
                vertCount = len(face)
                v0 = model.vertices[face[0][0] - 1]
                v1 = model.vertices[face[1][0] - 1]
                v2 = model.vertices[face[2][0] - 1]
                if vertCount == 4:
                    v3 = model.vertices[face[3][0] - 1]
                
                if self.vertexShader:
                    v0 = self.vertice(v0, modelMatrix = mMat )
                    v1 = self.vertice(v1, modelMatrix = mMat )
                    v2 = self.vertice(v2, modelMatrix = mMat )
                    if vertCount ==4:
                        v3 = self.vertice(v3, modelMatrix = mMat )
                    
                #self.glPoint(int(v0[0]), int(v0[1]))
                #self.glPoint(int(v1[0]), int(v1[1]))
                #self.glPoint(int(v2[0]), int(v2[1]))
                #if vertCount == 4:
                   # self.glPoint(int(v3[0]), int(v3[1]))
                
            self.glLine((v0[1],v0[1]),(v1[0],v1[1]))
            
