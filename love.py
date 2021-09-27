import webbrowser

import pygame

pygame.init()
# global mouse
# # noinspection PyRedeclaration
# mouse = pygame.mouse.get_pos()
# noinspection PyRedeclaration


class Video:
	def __init__(self, title, link):
		self.title = title
		self.link = link
		self.seen = False

	def open(self):
		webbrowser.open(self.link)
		self.seen = True


class TextButton:
	def __init__(self, text, position, color):
		self.text = text
		self.position = position
		self.color = color
		self.font = pygame.font.SysFont('sans', 30)
		self.text_render = self.font.render(self.text, True, self.color)
		self.text_box = self.text_render.get_rect()
		self.small_font = pygame.font.SysFont('sans', 15)
		self.small_text_render = self.small_font.render(self.text, True, self.color)
		self.small_text_box = self.small_text_render.get_rect()
		self.click = False
		btn_list.append(self)

	def is_mouse_on_text(self):
		# noinspection PyGlobalUndefined
		global mouse
		mouse = pygame.mouse.get_pos()
		if (self.position[0] >= mouse[0] or mouse[0] >= self.position[0] + self.text_box[2]) or (
				self.position[1] >= mouse[1] or mouse[1] >= self.position[1] + self.text_box[3]):
			return False
		return True

	def draw(self):
		if self.is_mouse_on_text():
			self.text_render = self.font.render(self.text, True, (0, 0, 255))
			pygame.draw.line(screen, (0, 0, 255), (self.position[0], self.position[1] + self.text_box[3]),
							[self.position[0] + self.text_box[2], self.position[1] + self.text_box[3]])
		else:
			self.text_render = self.font.render(self.text, True, self.color)
		screen.blit(self.text_render, self.position)

	def draw_rect(self):
		pygame.draw.rect(screen, (0, 0, 0), (self.position[0], self.position[1], self.text_box[2], self.text_box[3]))

	def small_draw(self):
		screen.blit(self.small_text_render, self.position)

	def small_draw_rect(self):
		pygame.draw.rect(screen, (0, 0, 0),
						 (self.position[0], self.position[1], self.small_text_box[2], self.small_text_box[3]))

	def center(self):
		self.position = (WIDTH / 2 - self.text_box.width / 2, self.position[1])


btn_list = []
WIDTH = 465
HEIGHT = 618
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Love")
running = True

WHITE = (255, 255, 255)
clock = pygame.time.Clock()

background_image = pygame.image.load("background.JPG")
background_image = pygame.transform.scale(background_image, (474, 618))
love_image = pygame.image.load("mylove.JPG")
love_image = pygame.transform.scale(love_image, (WIDTH, HEIGHT))
# main page
back_btn = TextButton("Back", (0, 0), WHITE)
happy_anni_btn = TextButton("Happy early anniiiiiii", (0, 50), WHITE)
about_her_btn = TextButton("About Her", (0, 100), WHITE)
music_btn = TextButton("Play her's favorite songs", (0, 150), WHITE)

# happy anni
love_btn = TextButton("Anh iu emmmmmm", (0, 0), WHITE)

# about her
birthday_btn = TextButton("Birthday", (0, 50), WHITE)
hobby_btn = TextButton("Hobbies", (0, 100), WHITE)
dreams_btn = TextButton("Dreams", (0, 150), WHITE)

list_about_her_btn = [birthday_btn, hobby_btn, dreams_btn]

# her favorite songs
to_the_moon_btn = TextButton("To The Moon", (0, 50), WHITE)
song1 = Video("To The Moon", "https://www.youtube.com/watch?v=nmKTlmByng0&ab_channel=hooligan.official")
s3107_btn = TextButton("3107", (0, 100), WHITE)
song2 = Video("3107", "https://www.youtube.com/watch?v=AUz0JNWLt30&ab_channel=DuonggOfficial")
I_love_you_3000_btn = TextButton("I Love You 3000", (0, 150), WHITE)
song3 = Video("I Love You 3000", "https://www.youtube.com/watch?v=a0qC7lG3Vfc&ab_channel=Myynhh")

list_her_favorite_song = [to_the_moon_btn, s3107_btn, I_love_you_3000_btn]
songs = [song1, song2, song3]

back_btn.click = True

while running:
	clock.tick(60)
	screen.fill((0, 200, 0))
	screen.blit(background_image, (0, 0))

	if btn_list[0].click:
		for i in range(len(btn_list)):
			if i == 0:
				continue
			btn_list[i].position = (-1000, btn_list[i].position[1])

		happy_anni_btn.center()
		happy_anni_btn.draw_rect()
		happy_anni_btn.draw()

		about_her_btn.center()
		about_her_btn.draw_rect()
		about_her_btn.draw()

		music_btn.center()
		music_btn.draw_rect()
		music_btn.draw()

	if btn_list[1].click:
		for i in range(len(btn_list)):
			if i == 0:
				continue
			btn_list[i].position = (-1000, btn_list[i].position[1])
		screen.blit(love_image, (0, 0))
		back_btn.draw_rect()
		back_btn.draw()
		love_btn.center()
		love_btn.draw_rect()
		love_btn.draw()

	if btn_list[2].click:
		for i in range(len(btn_list)):
			if i == 0:
				continue
			btn_list[i].position = (-1000, btn_list[i].position[1])

		for btn in list_about_her_btn:
			btn.center()
			btn.draw_rect()
			btn.draw()

		if birthday_btn.is_mouse_on_text():
			# noinspection PyUnboundLocalVariable
			date_btn = TextButton("20/05/2003", (mouse[0] + 10, mouse[1]), WHITE)
			date_btn.small_draw_rect()
			date_btn.small_draw()

		if hobby_btn.is_mouse_on_text():
			hobby1 = TextButton("1.chuch chichhhhhhhh, dui ga rannnnnnn", (mouse[0] + 10, mouse[1]), WHITE)
			hobby2 = TextButton("2.hong tra machiatto tran chau tranggggg", (mouse[0] + 10, mouse[1] + 20), WHITE)
			hobby3 = TextButton("3.xem phimmmmmmm, nguuuuuuuuuuu", (mouse[0] + 10, mouse[1] + 40), WHITE)
			hobby_list = [hobby1, hobby2, hobby3]
			for i in range(len(hobby_list)):
				hobby_list[i].small_draw_rect()
				hobby_list[i].small_draw()

		if dreams_btn.is_mouse_on_text():
			dream1 = TextButton("1.di du nich chau auuuu", (mouse[0] + 10, mouse[1]), WHITE)
			dream2 = TextButton("2.o zoi nhau mai maiiiiii", (mouse[0] + 10, mouse[1] + 20), WHITE)
			dream_list = [dream1, dream2]
			for i in range(len(dream_list)):
				dream_list[i].small_draw_rect()
				dream_list[i].small_draw()

		back_btn.draw_rect()
		back_btn.draw()

	if btn_list[3].click:
		for i in range(len(btn_list)):
			if i == 0:
				continue
			btn_list[i].position = (-1000, btn_list[i].position[1])

		for i in range(len(list_her_favorite_song)):
			list_her_favorite_song[i].center()
			list_her_favorite_song[i].draw_rect()
			list_her_favorite_song[i].draw()
			if songs[i].seen:
				list_her_favorite_song[i].color = (0, 0, 255)

		back_btn.draw_rect()
		back_btn.draw()

	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				for i in range(len(songs)):
					if list_her_favorite_song[i].is_mouse_on_text():
						songs[i].open()
				for i in range(len(btn_list)):
					if i > 3:
						pass
					elif btn_list[i].is_mouse_on_text():
						btn_list[i].click = True
						for t in range(len(btn_list)):
							if t == i:
								continue
							btn_list[t].click = False

		if event.type == pygame.QUIT:
			running = False

	pygame.display.flip()

pygame.quit()
