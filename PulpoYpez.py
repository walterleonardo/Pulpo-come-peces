import random, pygame, sys
from pygame.locals import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

class Bloque(pygame.sprite.Sprite):
	"""
	Esta clase representa la pelota        
	Deriva de la clase "Sprite" en Pygame
	"""
	def __init__(self, nombre_de_archivo):
		# Llamada al constructor de la clase padre (Sprite)
		super().__init__() 
		# Crea una imagen del bloque y la rellena con un color.
		# También podría tratarse de una imagen guardada en disco.
		self.image = pygame.image.load(nombre_de_archivo).convert_alpha()
		#Hacemos que el fondo sea transparente. Ajusta a BLANCO si tu
		# imagen de fondo es blanca.
		#self.image.set_colorkey(WHITE)
		# Extraemos el objeto rectángulo que posee las dimensiones de la imagen.
		# DEfiniendo los valores para rect.x y rect.y, actualizamos la posición de este
		# objeto
		self.rect = self.image.get_rect()

def main():
	pygame.init()
	pygame.display.set_caption("Título del juego")
	#personaje = pygame.image.load('pulpo.png')
	personaje_x = 65
	personaje_y = 65
	reloj = pygame.time.Clock()
	puntuacion = 0
	ancho_pantalla = 480
	alto_pantalla = 360
	pantalla = pygame.display.set_mode((ancho_pantalla,alto_pantalla))
	fondo = pygame.image.load('fondo.jpg')

	# create a font object. 
	# 1st parameter is the font file 
	# which is present in pygame. 
	# 2nd parameter is size of the font 
	font = pygame.font.Font('freesansbold.ttf', 22) 
	  
	# create a text suface object, 
	# on which text is drawn on it. 
	text = font.render('Contador:', True, GREEN, BLACK) 
	count = font.render('0', True, RED, BLACK) 
	  
	# create a rectangular object for the 
	# text surface object 
	textRect = text.get_rect()  
	  
	# set the center of the rectangular object. 
	textRect.center = (300, 10) 


	# Esta es una lista de todos los 'sprites.' Cada bloque en el programa es
	# añadido a esta lista. La lista es gestionada por la clase llamada 'Group.'
	listade_bloques = pygame.sprite.Group()
	 
	# Esta es una lista de cada sprite, así como de todos los bloques, incluído el del protagonista.
	listade_todoslos_sprites = pygame.sprite.Group()
	 
	for i in range(10):
		# ESto representa un bloque
		bloque = Bloque("pez.png")
	 
		# Definimos una ubicación aleatoria para el bloque
		bloque.rect.x = random.randrange(ancho_pantalla)
		bloque.rect.y = random.randrange(alto_pantalla)
		 
		# Añadimos el bloque a la lista de objetos
		listade_bloques.add(bloque)
		listade_todoslos_sprites.add(bloque)
		 
	# Creamos un bloque protagonista con una imagen de disco
	protagonista = Bloque("pulpo.png")
	listade_todoslos_sprites.add(protagonista)
	 
	# Iteramos hasta que el usuario hace click sobre el botón de salida.
	hecho = False
	 
	# Lo usamos para gestionar cuán rápido de refresca la pantalla.
	reloj = pygame.time.Clock()	


	while True:
		pantalla.fill(WHITE)
		pantalla.blit(fondo, (0, 0))
		pantalla.blit(text, textRect)
		pantalla.blit(count, (350,0))
		pos = pygame.mouse.get_pos()
		personaje_x = pos[0]
		personaje_y = pos[1]
		if (personaje_x > 480-65):
			personaje_x = 480-65
			
		if (personaje_y > 360-65):
			personaje_y = 360-65

		#pantalla.blit(personaje, (personaje_x, personaje_y))
		
							
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				if event.key == K_LEFT and personaje_x > 0:
					personaje_x -= 10 
				if event.key == K_RIGHT and personaje_x < 480-65:
					personaje_x += 10
				if event.key == K_UP and personaje_y > 0:
					personaje_y -= 10
				if event.key == K_DOWN and personaje_y < 360-65:
					personaje_y += 10

			if event.type == QUIT:
				pygame.quit()
				sys.exit(0)
		
		protagonista.rect.x = personaje_x
		protagonista.rect.y = personaje_y
		
		# Observamos si el bloque protagonista ha colisionado contra algo.
		listade_impactos_bloque = pygame.sprite.spritecollide(protagonista, listade_bloques, True)  
		 
		# Comprobamos la lista de colisiones.
		for bloque in listade_impactos_bloque:
			puntuacion += 1
			print(puntuacion)
			count = font.render(str(puntuacion), True, GREEN, BLUE) 

			 
		# Dibujamos todos los sprites
		listade_todoslos_sprites.draw(pantalla)
			
		#pygame.display.update()
		# Limitamos a 60 fps
		reloj.tick(60)
		# Avanzamos y actualizamos la pantalla con todo lo que hayamos dibujado.
		pygame.display.flip()



if __name__ == '__main__':
	main()