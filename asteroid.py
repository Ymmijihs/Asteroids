from circleshape import *
from constants import *
import random

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

	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		angle = random.uniform(20, 50)
		new_radius = self.radius - ASTEROID_MIN_RADIUS
		vectorA = self.velocity.rotate(angle) * 1.2
		vectorB = self.velocity.rotate(angle * -1) * 1.2
		asteroidA = Asteroid(self.position.x, self.position.y, new_radius)
		asteroidA.velocity = vectorA
		asteroidB = Asteroid(self.position.x, self.position.y, new_radius)
		asteroidB.velocity = vectorB
		asteroids.add(asteroidA)
		asteroids.add(asteroidB)
