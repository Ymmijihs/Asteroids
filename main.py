import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
	pygame.init()
	clock =	pygame.time.Clock()
	dt = 0
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable,)
	Shot.containers = (shots, updatable, drawable)
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	asteroid_field = AsteroidField()
	while True:
		for event in pygame.event.get():
    			if event.type == pygame.QUIT:
        			return
		screen.fill((0,0,0))
		for dthing in drawable:
			dthing.draw(screen)
		updatable.update(dt)
		pygame.display.flip()
		delta = clock.tick(60)
		dt = delta / 1000
		for a in asteroids:
			if a.collision(player):
				print("Game over!")
				sys.exit()
		for a in asteroids:
			for s in shots:
				if a.collision(s):
					a.split()
					s.kill()


if __name__ == "__main__":
    main()

