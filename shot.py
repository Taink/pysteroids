from circleshape import CircleShape
from pygame.surface import Surface
from constants import SHOT_RADIUS
import pygame

class Shot(CircleShape):
    def __init__(self, x: float, y: float):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen: Surface):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt: float):
        self.position += self.velocity * dt
