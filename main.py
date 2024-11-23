import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidField import AsteroidField
from shot import Shot


def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	Asteroid.containers = (updatable, drawable, asteroids)
	AsteroidField.containers = (updatable)
	Shot.containers = (updatable, drawable, shots)

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	asteroid_field = AsteroidField()

	dt = 0

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		for thing in updatable:
			thing.update(dt)
		
		for asteroid in asteroids:
			if asteroid.collision(player):
				print("Game over!")
				exit()
			for shot in shots:
				if asteroid.collision(shot):
					shot.kill()
					asteroid.split()

		screen.fill("black")
		
		for object in drawable:
			object.draw(screen)
		
		pygame.display.flip()

		dt = clock.tick(60) / 1000
	

if __name__ == "__main__":
	main()
