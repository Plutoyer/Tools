import os
import sys
import random
import pygame


'''定义必要的常量'''
BGMPATH = 'music/bgm.mp3'
IMAGEDIR = 'pictures'
SUPPORTEXTS = ['jpg', 'png', 'bmp']
SCREENSIZE = (800, 600)
WHITE = (255, 255, 255, 27)
GRAY = (192, 192, 192)


'''随机读取一张图片'''
def readImageRandomly():
	filenames = os.listdir(IMAGEDIR)
	filenames = [f for f in filenames if f.split('.')[-1] in SUPPORTEXTS]
	imgpath = os.path.join(IMAGEDIR, random.choice(filenames))
	return pygame.transform.scale(pygame.image.load(imgpath), SCREENSIZE)


'''主程序'''
def main():
	pygame.init()
	pygame.mixer.init()
	pygame.mixer.music.load(BGMPATH)
	pygame.mixer.music.play(-1, 0.0)
	pygame.mouse.set_cursor(*pygame.cursors.diamond)
	screen = pygame.display.set_mode(SCREENSIZE)
	pygame.display.set_caption('刮刮乐')
	surface = pygame.Surface(SCREENSIZE).convert_alpha()
	surface.fill(GRAY)
	image_used = readImageRandomly()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit(-1)
		mouse_event_flags = pygame.mouse.get_pressed()
		if mouse_event_flags[0]:
			pygame.draw.circle(surface, WHITE, pygame.mouse.get_pos(), 40)
		elif mouse_event_flags[-1]:
			surface.fill(GRAY)
			image_used = readImageRandomly()
		screen.blit(image_used, (0, 0))
		screen.blit(surface, (0, 0))
		pygame.display.update()


'''run'''
if __name__ == '__main__':
	main()
