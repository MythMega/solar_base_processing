from Planet import *
from PlanetUtilities import *

def setup():
  size(1870,1030) #size de l'écran
  background(0) #background noir
  stroke(255,255,255) #point blanc par défaut
  strokeWeight(10) #taille du point par défaut
  smooth()
  frameRate(240) 
  global time_passed,INDICE_DE_VITESSE,listpositionsLuneX,listpositionsLuneY,listpositionsDeimosX,listpositionsDeimosY, planetTerre, planetMars,satteliteLune,satteliteDeimos,planetMercure,planetVenus, planetJupiter, planetSaturn, planetUranus, planetNeptune
  time_passed = 55
  INDICE_DE_VITESSE = 0.001 #float, indice de vitesse global, doit être inférieur à 1
  listpositionsLuneX = [] #initialisation d'un tableau, pour sauvegarder les postions de cet astre (X de la lune)
  listpositionsLuneY = [] #initialisation d'un tableau, pour sauvegarder les postions de cet astre (Y de la lune)
  listpositionsDeimosX = [] #initialisation d'un tableau, pour sauvegarder les postions de cet astre (X de Deimos)
  listpositionsDeimosY = [] #initialisation d'un tableau, pour sauvegarder les postions de cet astre (Y de Deimos)
  
  #déclaration des planetes
  planetMercure = Planet(20, 255, 127, 0, "Venus", 200, 1.7)
  planetVenus = Planet(25, 240, 50, 30, "Mercure", 280,1.8)
  planetTerre = Planet(40, 0, 40, 255, "Terre", 325,0.8)
  planetMars = Planet(35, 240, 50, 30, "Mars", 380,1.4)
  planetJupiter = Planet(100, 200, 200, 127, "Jupiter", 450, 0.4)
  planetSaturn = Planet(80, 200, 200, 127, "Saturn", 500,0.9)
  planetUranus = Planet(50, 0, 150, 255, "Uranus", 530,1.2)
  planetNeptune = Planet(50, 240, 50, 255, "Neptune", 560,1.5)
  
  #declaratiosn des sattelites
  satteliteLune = Planet(8, 240, 255, 255, "Lune", 48,11.8)
  satteliteDeimos = Planet(25, 240, 255, 255, "Deimos", 80,8)
  
#fonction qui s'execute a chaque frame  
def draw():
    global time_passed,INDICE_DE_VITESSE,planetTerre, planetMars,satteliteLune,satteliteDeimos,planetMercure,planetVenus, planetJupiter, planetSaturn, planetUranus, planetNeptune
    checkKeyPressed() #permet de controler la vitesse en fonction de la touche du clavier appuyée
    background(0)
    translate(width/2, height/2) #on deplace le repere de la moitié de la hauteur et de la moitiée de la largeur, histoire d'avoir un repere en 0;0, au centre au lieu de l'avoir en haut a gauche de la fenetre
    
    strokeWeight(150)
    stroke(255,255,200)
    point(0,0)
    
    #execute les calculs des nouvelles coordonnées de chaque planète, et les enregistre en tant qu'attribut
    faireRotationAutourSoleil(planetTerre, planetTerre._distance, planetTerre._vitesse, time_passed)
    faireRotationAutourSoleil(planetMars, planetMars._distance, planetMars._vitesse, time_passed)
    faireRotationAutourSoleil(planetMercure, planetMercure._distance, planetMercure._vitesse, time_passed)
    faireRotationAutourSoleil(planetVenus, planetVenus._distance, planetVenus._vitesse, time_passed)
    faireRotationAutourSoleil(planetJupiter, planetJupiter._distance, planetJupiter._vitesse, time_passed)
    faireRotationAutourSoleil(planetSaturn, planetSaturn._distance, planetSaturn._vitesse, time_passed)
    faireRotationAutourSoleil(planetUranus, planetUranus._distance, planetUranus._vitesse, time_passed)
    faireRotationAutourSoleil(planetNeptune, planetNeptune._distance, planetNeptune._vitesse, time_passed)
    
    faireRotation(planetTerre, satteliteLune, satteliteLune._distance, satteliteLune._vitesse, time_passed)
    # faireRotation(planetMars, satteliteDeimos, satteliteDeimos._distance, satteliteDeimos._vitesse, time_passed)
    
    listePlanete = [planetTerre, planetMars,planetMercure,planetVenus, planetJupiter, planetSaturn, planetUranus, planetNeptune]
    listeSatellite = [satteliteLune]
    listeAstres = listePlanete + listeSatellite
    
    listpositionsLuneX.append(satteliteLune.getPosX())
    listpositionsLuneY.append(satteliteLune.getPosY())
    for i in range(len(listpositionsLuneX)):
        strokeWeight(2)
        stroke(255)
        point(listpositionsLuneX[i], listpositionsLuneY[i]) 
    
    # listpositionsDeimosX.append(satteliteDeimos.getPosX())
    # listpositionsDeimosY.append(satteliteDeimos.getPosY())
    # for i in range(len(listpositionsDeimosX)):
    #     strokeWeight(2)
    #     stroke(255,127,0)
    #     point(listpositionsDeimosX[i], listpositionsDeimosY[i]) 
    
    #dessine chaque astres à ses nouvelles coordonées
    for i in range(len(listeAstres)):
        dessinerPlanet(listeAstres[i])
        name = listeAstres[i]._name
        text(listeAstres[i]._name, listeAstres[i]._pos_x + listeAstres[i]._size/2 +5 , listeAstres[i]._pos_y )
    

    
    
    print(time_passed)
    
    
def mouseClicked():
    pass
    
def checkKeyPressed():
    global INDICE_DE_VITESSE, time_passed
    if mousePressed:
        uptime = 0
    else:
        uptime = INDICE_DE_VITESSE
    if keyPressed:
        if key == 'v' or key == 'V':
            uptime = INDICE_DE_VITESSE * 10
        if key == 's' or key == 'S':
            uptime = INDICE_DE_VITESSE//10
    time_passed += uptime
    
    
def drawSun():
    strokeWeight(100)
    stroke(127,127,0)
    point(0,0)
    strokeWeight(10)
    stroke(255,255,255)
