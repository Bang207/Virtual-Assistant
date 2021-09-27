import pygame
from random import randint

pygame.init()


class Tube:

    def __init__(self, x, h):
        self.x = x
        self.height = h
        self.passed = False
        self.rect = None
        self.invrect = None

    def draw(self):
        tubeimage = pygame.image.load("pipe-green.png")

        tube_image = pygame.transform.scale(tubeimage, (TUBE_WIDTH, self.height))
        tube_image = pygame.transform.flip(tube_image, False, True)

        invtube_image = pygame.transform.scale(tubeimage, (TUBE_WIDTH, 600 - (self.height + TUBE_DISTANCE)))
        tubes[i].rect = screen.blit(tube_image, (self.x, 0))
        tubes[i].invrect = screen.blit(invtube_image, (self.x, self.height + TUBE_DISTANCE))


def line_count(fil):
    line_c = 0
    for line in fil:
        if line != "":
            line_c += 1
    return line_c


screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Flappy Bird")
running = True

backgroundd_image = pygame.image.load("background-day.png")
backgroundd_image = pygame.transform.scale(backgroundd_image, (400, 600))
backgroundn_image = pygame.image.load("background-night.png")
backgroundn_image = pygame.transform.scale(backgroundn_image, (400, 600))
bird_image = pygame.image.load("yellowbird.png")
base_image = pygame.image.load("base.png")
base_image = pygame.transform.scale(base_image, (400, 50))

GREEN = (0, 200, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

clock = pygame.time.Clock()

TUBE_WIDTH = 50
TUBE_VELOCITY = 3
TUBES_DISTANCE = 200
TUBE_DISTANCE = 200

tube1 = Tube(600, randint(0, 7) * 50)
tube2 = Tube(800, randint(0, 7) * 50)
tube3 = Tube(1000, randint(0, 7) * 50)
tubes = [tube1, tube2, tube3]

BIRD_X = 50
bird_y = 200
bird_drop_velocity = 0
GRAVITY = 0.5

score = 0
scores = [0]
font = pygame.font.SysFont('sans', 20)

playing = True
touch = True

day_and_night_barrier = 5

while running:
    clock.tick(60)
    screen.fill(GREEN)

    if score // day_and_night_barrier % 2 == 0:
        screen.blit(backgroundd_image, (0, 0))
    else:
        screen.blit(backgroundn_image, (0, 0))

    for i in range(len(tubes)):
        tubes[i].draw()
        tubes[i].x -= TUBE_VELOCITY

    if tubes[-3].x + TUBE_WIDTH < 0:
        height = randint(0, 7)
        tube = Tube(tubes[-1].x + TUBES_DISTANCE, height * 50)
        tubes.append(tube)

    sand = screen.blit(base_image, (0, 550))
    bird_rect = screen.blit(bird_image, (BIRD_X, bird_y))
    bird_y = int(bird_y + bird_drop_velocity)
    bird_drop_velocity += GRAVITY

    if tubes[-3].x + TUBE_WIDTH < BIRD_X and not tubes[-3].passed:
        score += 1
        tubes[-3].passed = True

    score_txt = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_txt, (5, 5))

    for tube in [tubes[-3].rect, tubes[-3].invrect, sand]:
        if bird_rect.colliderect(tube):
            TUBE_VELOCITY = 0
            bird_drop_velocity = 0
            if playing:
                scores.append(score)
                playing = False
            with open("flappybird.txt", "a") as f:
                pass
            with open("flappybird.txt", "r") as file:
                linecount = line_count(file)
                file.seek(0)
                for i in range(linecount):
                    a = file.readline()
                    scores.append(int(a))

            text1 = font.render("GAME OVER, score = " + str(score), True, BLACK)
            text2 = font.render("Press SPACE to continue", True, BLACK)
            text3 = font.render("Highest score: " + str(max(scores)), True, BLACK)
            screen.blit(text1, (150, 300))
            screen.blit(text2, (150, 330))
            screen.blit(text3, (150, 270))
    if bird_y < 0 and touch:
        bird_drop_velocity = 0
        touch = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            with open("flappybird.txt", "a") as file:
                file.write(str(max(scores)) + "\n")

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not playing:
                    TUBE_VELOCITY = 3
                    tube1 = Tube(600, randint(0, 7) * 50)
                    tube2 = Tube(800, randint(0, 7) * 50)
                    tube3 = Tube(1000, randint(0, 7) * 50)
                    tubes = [tube1, tube2, tube3]
                    scores.append(score)
                    score = 0
                    bird_y = 200
                    playing = True
                bird_drop_velocity = -10
                touch = True
                if bird_y == 0:
                    bird_drop_velocity = 0
    pygame.display.flip()

pygame.quit()
