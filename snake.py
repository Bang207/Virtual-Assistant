import pygame
from time import sleep
from random import randint


pygame.init()

screen = pygame.display.set_mode((601, 621))
pygame.display.set_caption("Snake")
running = True
clock = pygame.time.Clock()

GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

snakes = [[10, 10], [11, 10]]
direction = "right"
scores = [0]
score = 0

big_apple = [randint(0, 18), randint(0, 18)]
apple = [-100, -100]

bigapple_eaten = False

font = pygame.font.SysFont('sans', 20)

pausing = False

while running:
	clock.tick(60)
	screen.fill(BLACK)
	tail_x = snakes[0][0]
	tail_y = snakes[0][1]
	for i in range(21):
		pygame.draw.line(screen, WHITE, (0, 30 * i + 20), (600, 30 * i + 20))
		pygame.draw.line(screen, WHITE, (30 * i, 20), (30 * i, 600 + 20))

	for snake in snakes:
		pygame.draw.rect(screen, GREEN, (snake[0] * 30, snake[1] * 30 + 20, 30, 30))

	if snakes[-1][0] == apple[0] and snakes[-1][1] == apple[1]:
		bigapple_eaten = False
		snakes.insert(0, [tail_x, tail_y])
		score += 1
		if score % 6 == 0:
			big_apple = [randint(0, 18), randint(0, 18)]
			apple = [-100, -100]
		else:
			apple = [randint(0, 19), randint(0, 19)]
			big_apple = [-100, -100]
		for snake in snakes:
			for big_apples in (big_apple, [big_apple[0] + 1, big_apple[1]], [big_apple[0] + 1, big_apple[1] + 1],
			                   [big_apple[0], big_apple[1] + 1]):
				if snake == big_apples:
					big_apple = [randint(0, 18), randint(0, 18)]

			if snake == apple:
				apple = [randint(0, 19), randint(0, 19)]

	for big_apples in (big_apple, [big_apple[0] + 1, big_apple[1]], [big_apple[0] + 1, big_apple[1] + 1],
	                   [big_apple[0], big_apple[1] + 1]):
		if snakes[-1][0] == big_apples[0] and snakes[-1][1] == big_apples[1] and bigapple_eaten is False:
			snakes.insert(0, [tail_x, tail_y])
			score += 2
			bigapple_eaten = True
			apple = [randint(0, 19), randint(0, 19)]

	if score % 6 == 0:
		pygame.draw.rect(screen, RED, (big_apple[0] * 30, big_apple[1] * 30 + 20, 60, 60))
	else:
		pygame.draw.rect(screen, RED, (apple[0] * 30, apple[1] * 30 + 20, 30, 30))

	if direction == "right" and pausing is False:
		snakes.append([snakes[-1][0] + 1, snakes[-1][1]])
		snakes.pop(0)
	if direction == "left" and pausing is False:
		snakes.append([snakes[-1][0] - 1, snakes[-1][1]])
		snakes.pop(0)
	if direction == "up" and pausing is False:
		snakes.append([snakes[-1][0], snakes[-1][1] - 1])
		snakes.pop(0)
	if direction == "down" and pausing is False:
		snakes.append([snakes[-1][0], snakes[-1][1] + 1])
		snakes.pop(0)
	sleep(0.1)

	if snakes[-1][0] < 0 and direction == "left":
		snakes.append([19, snakes[-1][1]])
		snakes.pop(0)
	if snakes[-1][0] > 19 and direction == "right":
		snakes.append([0, snakes[-1][1]])
		snakes.pop(0)
	if snakes[-1][1] < 0 and direction == "up":
		snakes.append([snakes[-1][0], 19])
		snakes.pop(0)
	if snakes[-1][1] > 19 and direction == "down":
		snakes.append([snakes[-1][0], 0])
		snakes.pop(0)

	for i in range(len(snakes) - 1):
		if snakes[-1] == snakes[i]:
			if not pausing:
				scores.append(score)
				pausing = True
				with open("snake.txt", "a"):
					pass
				with open("snake.txt", "r") as file:
					lines = file.readlines()
					for line in lines:
						if line[-1] == "\n":
							line = line[:-1]
						scores.append(int(line))
			text1 = font.render("GAME OVER, score = " + str(score), True, WHITE)
			text2 = font.render("Press SPACE to continue", True, WHITE)
			text3 = font.render("Highest score: " + str(max(scores)), True, WHITE)
			screen.blit(text1, (250, 300))
			screen.blit(text2, (250, 330))
			screen.blit(text3, (250, 270))

	pygame.draw.rect(screen, BLACK, (0, 0, 601, 20))
	score_txt = font.render("Score: " + str(score), True, WHITE)
	screen.blit(score_txt, (0, 0))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			with open("snake.txt", "a") as file:
				file.write(str(max(scores)) + "\n")

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP and direction != "down":
				direction = "up"
			if event.key == pygame.K_DOWN and direction != "up":
				direction = "down"
			if event.key == pygame.K_LEFT and direction != "right":
				direction = "left"
			if event.key == pygame.K_RIGHT and direction != "left":
				direction = "right"

			if event.key == pygame.K_SPACE and pausing is True:
				snakes = [[10, 10], [11, 10]]
				big_apple = [randint(0, 18), randint(0, 18)]
				apple = [-100, -100]
				direction = "right"
				score = 0
				pausing = False
				bigapple_eaten = False

	pygame.display.flip()
pygame.quit()


