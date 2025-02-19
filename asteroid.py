from circleshape import *
from constants import *


class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)

	def draw(self, surface):
		sradius = int(self.radius)  # Radius as an integer
		sposition = (int(self.position.x), int(self.position.y))  # (x, y) tuple
		pygame.draw.circle(surface, (255, 255, 255), sposition, sradius, width=2)

	def update(self, dt):
		if not hasattr(self, 'velocity'):
			self.velocity = pygame.Vector2(0, 0)  # Default velocity
		self.position += (self.velocity * dt)
