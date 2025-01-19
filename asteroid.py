import pygame
from pygame.surface import Surface
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float):
        super().__init__(x, y, radius)

    def draw(self, screen: Surface):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt: float):
        self.position += self.velocity * dt
