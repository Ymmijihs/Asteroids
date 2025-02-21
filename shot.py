from circleshape import *
from constants import *

class Shot(CircleShape):
	def __init__(self, x, y):
		super().__init__(x, y, SHOT_RADIUS)

	def draw(self, surface):
		sradius = int(self.radius)
		sposition = (int(self.position.x), int(self.position.y))
		pygame.draw.circle(surface, white, sposition, sradius, width=2)

	def update(self, dt):
		if not hasattr(self, 'velocity'):
			self.velocity = pygame.Vector2(0, 0)
		self.position += (self.velocity * dt)
