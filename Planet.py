class Planet:
    def __init__(self, planetSize, color_r, color_g, color_b, name, distance, vitesse=1, astre="sun", position_x = 0, position_y = 0):
        self._astre = astre
        self._red = color_r
        self._green = color_g
        self._blue = color_b
        self._name = name
        self._distance = distance
        self._vitesse = vitesse
        self._size = planetSize
        self._pos_x = position_x
        self._pos_y = position_y
        
        
    def getAstre(self):
        return self._astre

    def getRed(self):
        return self._red

    def getGreen(self):
        return self._green

    def getBlue(self):
        return self._blue

    def getName(self):
        return self._name

    def getDistance(self):
        return self._astre

    def getVitesse(self):
        return self._color

    def getSize(self):
        return self._size

    def getPosX(self):
        return self._pos_x

    def getPosY(self):
        return self._pos_y

    def changeColor(self, r,g,b):
        self._red = r
        self._green = g
        self._blue = b

    def changePosition(self, posX, posY):
        self._pos_x = posX
        self._pos_y = posY
