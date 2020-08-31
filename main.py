
import pygame, sys, random
pygame.init()
pygame.display.init()

size = 600,600
white = 255,255,255
black = 0,0,0
red = 255,0,0
surface = pygame.display.set_mode(size)


def collide(P, B):
    if P.x-20 < B.x < P.x+20:
        if B.y > P.y+65 or B.y < P.y-65:
            return True
    return False



class BIRD():
    def __init__(self):
        self.x = 100
        self.y = 200
        self.v = 0
        self.g = 1

    def update(self):
        if self.y < 580:
            self.y += self.v
            self.v += 1
            #print(self.y, self.v)

    def up(self):
        self.v -= 5
        self.v = min(self.v,10)


class PIPE():
    def __init__(self, x):
        self.x = x
        self.y = random.randint(100,500)
        self.v = 5

    def update(self):
        self.x -= self.v

    def draw(self):
        pygame.draw.rect(surface, white, (self.x, 0, 20, self.y-75))
        pygame.draw.rect(surface, white, (self.x, self.y+75, 20, 600-self.y))



bird = BIRD()
pipes = [PIPE(600), PIPE(900)]

while True:

    bird.update()
    pipes[0].update()
    pipes[1].update()
    if pipes[0].x < -20:
        pipes.pop(0)
        pipes.append(PIPE(600))
        #print(pipes)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        bird.up()
        #print('space')

    surface.fill(black)
    pygame.draw.circle(surface, white, (bird.x, bird.y), 10)
    pipes[1].draw()

    if collide(pipes[0], bird):
        pygame.draw.rect(surface, red, (pipes[0].x, 0, 20, pipes[0].y - 75))
        pygame.draw.rect(surface, red, (pipes[0].x, pipes[0].y + 75, 20, 600 - pipes[0].y))
    else:
        pipes[0].draw()


    pygame.display.flip()
    pygame.time.delay(50)


