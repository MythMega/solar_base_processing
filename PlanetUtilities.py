from Planet import *
from math import *
from processing import * 

def faireRotation(planeteMere, planete_fille, distance, vitesse, timepassed):
    planete_fille._pos_x = planeteMere.getPosX() + cos(timepassed*vitesse)*distance
    planete_fille._pos_y = planeteMere.getPosY() + sin(timepassed*vitesse)*distance
    
def faireRotationAutourSoleil(planete_fille, distance, vitesse, timepassed):
    planete_fille._pos_x = cos(timepassed*vitesse)*distance
    planete_fille._pos_y = sin(timepassed*vitesse)*distance

    
def dessinerPlanet(planet):
    strokeWeight(planet._size)
    stroke(planet._red,planet._green,planet._blue)
    point(planet._pos_x,planet._pos_y)
