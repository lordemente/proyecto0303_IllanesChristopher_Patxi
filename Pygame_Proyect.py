import pygame as py             #Importamos pygame y lo definimos como py
import random                   #Importación de la biblioteca random


class Background_and_Music(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = py.image.load("MagicBackground.png")                       #Cargando una imagen a nuestro código
        self.rect = self.image.get_rect()                                       #Convertirlo en un rectangulo (Eje X, Eje Y, (Ancho,Alto))
        self.fondo = py.mixer.music.load("Gorillaz _ On Melancholy Hill.mp3")  #Sube un sonido al código. Sonido Principal               
        self.impact = py.mixer.Sound("blip.mp3")     #Sondio Secundario, blip/borbuja
        self.gameover = py.mixer.Sound("sadness.mp3")      #Sonido secundario, Game Over Scene
 
    
    def Play_Musica(self):
        py.mixer.music.play(-1)         #(-1) Repetición en BUCLE
        # py.mixer.music.set_volume() #Juego con %, pero en este caso no es necesario ya que es el sonido  principal
        
    def Pause_music(self):
        py.mixer.music.pause()          #Detiene el sonido 
    
    def Unpause_Music(self):
        py.mixer.music.unpause()        #Reanuda el sonido
        

    def Play_Impact(self):       
        self.impact.play()              #Reproduce el sonido
        self.impact.set_volume(0.5)     #Juego con %, Mientas más bajo - sonido , SONIDO MAXIMO = 1 = 100%
        

    def Play_GameOver(self):       
        self.gameover.play()                #Reproduce un sondio
        # self.gameover.set_volume(1)       #Controla el sonido del timbre del audio
        

    def Stop_GameOver(self):
        self.gameover.stop()                #Detiene completamente el sonido
        
            
class Esfera_and_GameOver(py.sprite.Sprite):                            #Creación
    def __init__(self):
        super().__init__()
        self.image = py.image.load("Borbuja.png")                   #Cargando una imagen a nuestro código
        self.image = py.transform.scale(self.image, (30,30))        #Cambiando su tamaño original a una escala que se adapte a nuestro juego
        self.rect = self.image.get_rect()      
        self.rect.center = ((VENTANAX //2, VENTANAY *0.3))          #Cambiando su punto de referencia al centro del cuadrado
        self.movimiento = [5,5]                                     #Variable para que nos ayude a mover la imagen más adelante

        
        self.win = py.image.load("purpura.jpg")                         
        self.win = py.transform.scale(self.win, (VENTANAX,VENTANAY)) 
        self.rectan = self.win.get_rect()
        
        
        self.Pantalla1 = py.font.Font(None, 100)                         #Subir funtes de texto a nuestro código, si ponemos None, utilizamos la fuente de pygame
        self.Pantalla2 = py.font.Font(None, 50)                         # (tipo de letra, tamaño)
        self.Pantalla3 = py.font.Font(None, 50)
        self.Pantallawinner = py.font.Font(None, 150)
        

    def update(self):
        self.rect = self.rect.move(self.movimiento)                 #Cambiará de posición depende a su vectores X,Y
        if self.rect.left < 0 or self.rect.right > VENTANAX:        #Sí la esfuera llega <0 o >tamaño de la venta
            self.movimiento[0] = -self.movimiento[0]                #Desplazamineto invertido en su Eje X
            
        if self.rect.top <0:                                        #Si llega a la parte superior de la ventana
            self.movimiento[1] = - self.movimiento[1]              #Desplazamineto invertido en su Eje Y
        

    def GameOver(self):        
        
        self.text1 = self.Pantalla1.render(" Game over ",True,(255,255,255))                            #Creaciónnes de un texto("Texto",True/False,(R,G,B))                          
        self.text2 = self.Pantalla2.render("Press 'SPACE' to continue", True, (255,255,255))
        self.text3 = self.Pantalla2.render("Press 'X' to exit", True, (255,255,255))
        self.texto4 = self.Pantallawinner.render("YOU WIN !0_0!", True, (255,255,255))
        
        if self.rect.bottom > VENTANAY:                                                  #si la bola llega a la parte inferior
            
            textorect = self.text1.get_rect()                                            #Conviertiento la imagen,bola, a un rectangulo
            textorect.center = ((VENTANAX * 0.5, VENTANAY * 0.5))                        #Posición exacta dondé aparece nuestra imagen Y a su vez cambiando punto de referencia   
            ventana.blit(self.text1,textorect)                                           #De está manera se puede plasmar nuestro texto anteriormente creado
             
            textorect = self.text2.get_rect()
            textorect.centerx = VENTANAX //2
            textorect.centery = VENTANAY *0.6 
            ventana.blit(self.text2,textorect)
 

            textorect = self.text3.get_rect()
            textorect.center = ((VENTANAX//2, VENTANAY*0.7))     
            ventana.blit(self.text3,textorect)
            
            background.Pause_music()                                                     #Se pausea el sonido
            background.Play_GameOver()                                                   #Comienza a reproducir el sondio de GAMEOVER
            
            keys = py.key.get_pressed()                                                    #Bolean para detectar si una tecla está siendo o no presionada
            if keys[py.K_SPACE]:                                                           #Condicional, letra SPACE, si se cumple está condición
                self.rect.centerx = VENTANAX //2                                           #la imagen aparecerá en un punto especifico de la ventana
                self.rect.centery = VENTANAY *0.3                                          #Tanto en el Eje X y el Eje X

                background.Stop_GameOver()                             #Detiene el sonido secuendario
                background.Unpause_Music()                             #Reanuda el sondio principal depués de apretar la tecla SPACE


    def Winner(self):                                                  #Cuando no hayan más ladrillos cambia de imagen y
        ventana.blit(self.win, self.rectan)
        winnerect = self.texto4.get_rect()
        winnerect.center = ((VENTANAX//2, VENTANAY//2))
        ventana.blit(self.texto4,winnerect)                             #Texto de YOU WIN 0_0 sobre la pantalla
        

class BAR(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = py.image.load("BARRR.png")                             #Subimos una imagen
        self.image = py.transform.scale(self.image, (100,50))               #Cambio de ESCALA de la imagen original
        self.rect = self.image.get_rect()    
        self.rect.center = ((VENTANAX//2, VENTANAY*0.97))
        self.movimiento = [4,4]
        self.timeL = None
        self.timeR = None
              

    def update(self):
        x = random.randint(5, 8)                             #Número aleatorio (desde, hasta)
        TIEMPO_BARRA = 0.5      

        keys = py.key.get_pressed()                          #Bool   True, si se presiona alguna tecla
        if keys[py.K_LEFT]:                                  #Especificación de la tecla pulsada, en este caso K_LEFT
            tiempoL = py.time.get_ticks()/1000               #se consigue el tiempo en milisengundos 
            
            if self.timeL == 0:                         
                self.timeL = py.time.get_ticks()/1000          #Otra variable para conseguir los milisegundos 
            
            if (tiempoL - self.timeL) > TIEMPO_BARRA:            #Si se cumple está condición la barra se movera mucho más rápido
                self.rect = self.rect.move(-15, 0)              #en su EJE -X= -15

            else:
                self.rect = self.rect.move(-x, 0)               #Y si no, solo se movera el número elegido por x = random.randint(5,8)
        else:
            self.timeL = 0                                      #

        if keys[py.K_RIGHT]:                                    #Lo mismo pero ahora con la telca K_RIGHT
            tiempoR = py.time.get_ticks()/1000
                     
            if self.timeR == 0:
                self.timeR = py.time.get_ticks()/1000
         
            if (tiempoR - self.timeR) > TIEMPO_BARRA:   
                self.rect = self.rect.move(15,0)         
            else:
                self.rect = self.rect.move(x,0)

        else:
            self.timeR = 0            

        if self.rect.colliderect(esfera.rect):                        #Si barra colisiona con la bola o esfera
            esfera.movimiento[1] = -esfera.movimiento[1]                #Se movera en el sentido contrario de su eje Y
           
                              
class Ladrillo(py.sprite.Sprite):
    def __init__(self,x, y):
        super().__init__()
        self.image = py.image.load("brick.png")                  #Tamaño original de la foto 64,32
        # self.image = py.transform.scale(self.image, (70,32)) 
        self.rect = self.image.get_rect(topleft = (x,y))
    

class Ladrillo_Irrompible(Ladrillo):
    def __init__(self,x,y,irrompibleX,irrompibleY):
        super().__init__(x,y)
        self.x = x
        self.y = y
        self.imagen = py.image.load("brick.png")
        self.image.fill((150,0,150,200), special_flags=py.BLEND_RGBA_MAX)       
        self.rect = self.image.get_rect()

        self.picture = py.image.load("brick.png")  
        self.picture.fill((150,0,150,200), special_flags=py.BLEND_RGBA_MAX)                
        self.rectangulo1 = self.picture.get_rect()

        self.irrompibleX = irrompibleX
        self.irrompibleY = irrompibleY


    def COLISIÓN(self):      
        self.rect.center = (self.x,self.y)  
        ventana.blit(self.image,self.rect)

        self.rectangulo1.center = ((self.irrompibleX, self.irrompibleY))   
        ventana.blit(self.picture,self.rectangulo1)
        
        if self.rect.colliderect(esfera.rect):
            self.rect.midbottom = ((self.x,self.y))
            esfera.movimiento[1] = - esfera.movimiento[1]
           
            if self.rect.colliderect(esfera.rect):
                self.rect.midtop = ((self.x,self.y))
                esfera.movimiento[1] = - esfera.movimiento[1]
               
                       
        if self.rectangulo1.colliderect(esfera.rect):
            self.rectangulo1.midbottom = ((self.irrompibleX, self.irrompibleY))
            esfera.movimiento[1] *= - 1
          

            if self.rectangulo1.colliderect(esfera.rect):
                self.rectangulo1.midtop = ((self.irrompibleX, self.irrompibleY))
                esfera.movimiento[1] *= - 1


                        
py.init()
VENTANAX, VENTANAY = 800,800
ventana = py.display.set_mode((VENTANAX,VENTANAY))
encabezado = py.display.set_caption("Snowball")
tiempo = py.time.Clock()

all_Sprites_Group = py.sprite.Group()                         #Mi Grupo principal de Sprites

background = Background_and_Music()                           #Guardando las Clases dentro del juego para usarlos tanto
esfera = Esfera_and_GameOver()                                #dentro y fuera del juego
bar = BAR()

all_Sprites_Group.add(background)                              #Agregando las CLASES al GRUPO PRINCIPAL
all_Sprites_Group.add(esfera)
all_Sprites_Group.add(bar)


ladrillo_irrompible1 = Ladrillo_Irrompible(200,300, 600,300)    #Creando los ladrillos irrompibles
ladrillo_irrompible2 = Ladrillo_Irrompible(300,400, 500,400)


background.Play_Musica()

'''Lista para guardar números aleatorios para generar el Efecto Nieve'''
lista_nieve = []                                        #Lista vacia para guardar coordenadas aleatorias
for snow in range(60):
    x = random.randint(0, VENTANAX)                         
    y = random.randint(0, VENTANAY)
    lista_nieve.append([x,y])                           #Lista con corrdenadas aleatorias


'''Creación de los ladrillos mediante 2 bucles For.'''
Ladrillos_Group = py.sprite.Group()                                #Sub Grupo Creado u otro grupo
FILAS = 5
COLUMNAS = 11
ANCHO_ladrillo = 64                                                #Tamaño del ladrillo 64,32
ALTO_ladrillo = 32
ESPACIO_entre_ladrillos = 10                                        #Falso Espacio
for fila in range(FILAS):                                               #Repite 5 veces
    for columna in range(COLUMNAS):                                     #Repite 11 veces
        x = columna * (ANCHO_ladrillo + ESPACIO_entre_ladrillos )
        y = fila * (ALTO_ladrillo + ESPACIO_entre_ladrillos )

        ladrillo = Ladrillo(x, y)                                   #Clase
        Ladrillos_Group.add(ladrillo)                               #Agregando al SUBGRUPO
        all_Sprites_Group.add(ladrillo)                             #Agregando al Grupo PRINCIPAL ""



SCORE = 0
'''Bucle del juego'''
jugando = True
while jugando:
    for event in py.event.get():
        if event.type == py.QUIT:
            jugando = False

    all_Sprites_Group.draw(ventana)
    
    '''Eliminación de los ladrillos al rebote'''  
    colisiones = py.sprite.spritecollide(esfera, Ladrillos_Group, True)         #True para eliminar el ladrio en el grupo que se encuentra, False --> lo atraviesa  
    if colisiones:
        esfera.movimiento[1] = -esfera.movimiento[1]
        background.Play_Impact()
        for i in colisiones:
            SCORE += 1
            print(f"ladrillos rotos: {SCORE}        Grupos Eliminados: {Ladrillos_Group}")
            if SCORE == 20:
                print("Aceleración aumentada a 7,7")
                esfera.movimiento = [7,7]
                esfera.rect.move(esfera.movimiento)
                if SCORE == 40:
                    print("Aceleración aumentada a 8,8")
                    esfera.movimiento = [8,8]
                    esfera.rect.move(esfera.movimiento)


    ''' Efecto Nieve '''
    for j in lista_nieve:
        py.draw.circle(ventana,(255,255,255), (j[0],j[1]),4)
        j[1] += 1
        if j[1] > VENTANAY:
            j[1] = 0
    
      
    ladrillo_irrompible1.COLISIÓN()             #Llamando al metodo dentro de la clase Ladrillo_Irrompible
    ladrillo_irrompible2.COLISIÓN()
    
    all_Sprites_Group.update()                  #Actualizando todos los metodos guardados dentro del Grupo princial
  
    
    esfera.GameOver()                           #LLmando al metodo Game Over
    if SCORE == FILAS* COLUMNAS:                #Si desapareces todos los ladrillos
        esfera.Winner()                                        
        if esfera.rect.bottom >VENTANAY *0.9:                                        
             esfera.movimiento[1] = - esfera.movimiento[1]
        for j in lista_nieve:
            py.draw.circle(ventana,(255,255,255), (j[0],j[1]),4)
            j[1] += 1
            if j[1] > VENTANAY:
                j[1] = 0

    py.display.flip()
    tiempo.tick(60)



