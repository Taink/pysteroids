import pygame
from pygame.surface import Surface
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float):
        super().__init__(x, y, radius)

    def draw(self, screen: Surface):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt: float):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS: # small asteroids
            return
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        split_angle = random.uniform(20, 50)
        new_asteroid_1.velocity = self.velocity.rotate(split_angle) * 1.2
        new_asteroid_2.velocity = self.velocity.rotate(-split_angle)
