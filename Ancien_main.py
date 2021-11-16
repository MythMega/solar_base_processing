from Planet import *
from PlanetUtilities import *

def setup():
  size(1000,1000)
  background(0)
  stroke(255,255,255)
  strokeWeight(10)
  smooth()
  global time_passed,INDICE_DE_VITESSE
  time_passed = 55
  INDICE_DE_VITESSE = 0.01 #float
def draw():
    global time_passed,INDICE_DE_VITESSE
    if mousePressed:
        uptime = 0
    else:
        uptime = INDICE_DE_VITESSE
    if keyPressed:
        if key == 'v' or key == 'V':
            uptime = INDICE_DE_VITESSE * 10
        if key == 's' or key == 'S':
            uptime = 0


    time_passed += uptime
    background(0)
    translate(width/2, height/2)
    
    strokeWeight(150)
    stroke(255,255,200)
    point(0,0)
    
    position_Terre_x =(cos(time_passed)*200)
    position_Terre_y = (sin(time_passed)*200)
    position_Lune_x = position_Terre_x + (cos(time_passed*10)*40)
    position_Lune_y = position_Terre_y + (sin(time_passed*10)*40)
    #print("Tx = " + str(position_Terre_x) + " Ty = " + str(position_Terre_y) + "Lx = " + str(position_Lune_x) + " Ly = " + str(position_Lune_y))
    print(time_passed)
    
    strokeWeight(35)
    stroke(0,127,255)
    point(position_Terre_x,position_Terre_y)
        
    strokeWeight(20)
    stroke(200,200,200)
    point(position_Lune_x,position_Lune_y)


def mouseClicked():
    pass
    
    
def drawSun(coordX,CoordY):
    strokeWeight(100)
    stroke(255,255,0)
    point(coordX,CoordY)
    strokeWeight(10)
    stroke(255,255,255)
    
def drawEarth(coordX,CoordY):
    strokeWeight(40)
    stroke(0,70,255)
    point(coordX,CoordY)
    strokeWeight(10)
    stroke(255,255,255)
    
def drawMoon(coordX,CoordY):
    strokeWeight(12)
    stroke(200,200,200)
    point(coordX,CoordY)
    strokeWeight(10)
    stroke(255,255,255)
