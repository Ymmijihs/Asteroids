import pygame
from constants import *
from player import *
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
	pygame.init()
	clock =	pygame.time.Clock()
	dt = 0
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
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
		
if __name__ == "__main__":
    main()

