import pygame
from net import Network
print(Network)
pygame.init()

width = 500
height = 500

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

clientNumber = 0

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.vel = 3

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.vel
        if keys[pygame.K_RIGHT]:
            self.x += self.vel
        if keys[pygame.K_UP]:
            self.y -= self.vel
        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.update()
        
    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)



def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

def read_pos(s):
    s = s.split(",")
    return int(s[0]), int(s[1])

def redraw(win, player, player2):
    win.fill((255, 255, 255))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()

def main():

    clock = pygame.time.Clock()
    run = True
    n = Network()
    startpos = read_pos(n.get_pos())
    print(startpos)
    p = Player(startpos[0], startpos[1], 100, 100, (0, 255, 0))
    p2 = Player(0, 0, 100, 100, (255, 0, 0))

    while run:
        clock.tick(60)
        p2pos = read_pos(n.send(make_pos((p.x, p.y))))
        print(p2pos)
        p2.x = p2pos[0]
        p2.y = p2pos[1]
        p2.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        p.move()
        redraw(win, p, p2)

main()