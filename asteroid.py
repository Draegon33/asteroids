from circleshape import *
import random
from constants import ASTEROID_MIN_RADIUS

class Asteroid (CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)

  def draw(self, screen):
    pygame.draw.circle(screen, "white", self.position, self.radius, 2)

  def update(self, dt):
    self.position += self.velocity * dt

  def split(self):
    random_angle = random.uniform(20, 50)

    if self.radius >= ASTEROID_MIN_RADIUS * 2:
      one_asteroid = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
      one_asteroid.velocity = self.velocity * 1.2
      one_asteroid.velocity = self.velocity.rotate(random_angle)
      
      two_asteroid = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
      two_asteroid.velocity = self.velocity * 1.2
      two_asteroid.velocity = self.velocity.rotate(-random_angle)
      

    self.kill()