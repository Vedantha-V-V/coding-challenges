import pygame
from circleshape import CircleShape
from shot import Shot
from constants import SPACESHIP_RADIUS,SPACESHIP_TURN_SPEED,SPACESHIP_SPEED,SPACESHIP_SHOOT_SPEED,SPACESHIP_SHOOT_COOLDOWN_SECONDS

class Spaceship(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,SPACESHIP_RADIUS)
        self.rotation = 0
        self.cooldown = 0
        self.flag = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        # print([a,b,c])
        return [a, b, c]
    
    def rotate(self,dt):
        self.rotation += (SPACESHIP_TURN_SPEED*dt)

    def update(self, dt):
        self.cooldown -= dt
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_RIGHT]:
            self.rotate(-dt)
        elif keys[pygame.K_d] or keys[pygame.K_LEFT]:
            self.rotate(dt)
        elif keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(dt)
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(-dt)
        elif keys[pygame.K_SPACE]:
            if self.flag == 0:
                self.shoot()
                self.flag +=1
            elif self.flag == 5:
                self.flag = 0
            else:
                self.flag += 1
    
    def move(self,dt):
        vector = pygame.Vector2(0, 1)
        direction = vector.rotate(self.rotation)
        spaceship_vector = direction*SPACESHIP_SPEED*dt
        self.position += spaceship_vector

    def draw(self,screen):
        pygame.draw.polygon(screen,"white",self.triangle())

    def shoot(self):
        if self.cooldown > 0:
            return
        shot = Shot(self.position.x,self.position.y)
        shot.velocity = pygame.math.Vector2(0,1)
        shot.velocity = pygame.math.Vector2.rotate(shot.velocity, self.rotation)
        shot.velocity = shot.velocity*SPACESHIP_SHOOT_SPEED
        cooldown = SPACESHIP_SHOOT_COOLDOWN_SECONDS