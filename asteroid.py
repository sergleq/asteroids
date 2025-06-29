import pygame
import random
from circleshape import CircleShape 
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)    
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()  # Удаляем текущий астероид

        if self.radius <= ASTEROID_MIN_RADIUS:
            return  # Маленький астероид — больше не делим

        # Вычисляем параметры новых астероидов
        random_angle = random.uniform(20, 50)
        velocity1 = self.velocity.rotate(random_angle) * 1.2
        velocity2 = self.velocity.rotate(-random_angle) * 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Создаём два новых меньших астероида в том же месте
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = velocity1

        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a2.velocity = velocity2
