# Quá trình phát triển hay sáng tạo một trò chơi sẽ xuất phát từ
# ý tưởng có thể phải đập đi xây lại rất nhiều lần để hình thành
# được kết quả cuối cùng
import pygame
from random import randint
import os
import string
cwd=os.getcwd()
cwd=cwd.replace(string.punctuation[-9],r"\\")
pygame.init()
# screen initialize
screen=pygame.display.set_mode((400,600))
pygame.display.set_caption("Flappy Bird")
clock=pygame.time.Clock()
WHITE=(255,255,255)
RED=(255,0,0)
YELLOW=(255,255,0)
BLUE=(0,0,255)
x_bird=50
y_bird=350
tube1_x=400
tube2_x=600
tube3_x=800
tube_width = 50
tube1_height=randint(100,400)
tube2_height=randint(100,400)
tube3_height=randint(100,400)
space_2tube=150
bird_drop_velocity=0
gravity=0.5
tube_velocity=2

score=0
font=pygame.font.SysFont("san",20)
font1=pygame.font.SysFont("san",40)
font2=pygame.font.SysFont("san",30)
background_img=pygame.image.load(cwd+r"\\flappy bird\\images\\background.png")
background_img=pygame.transform.scale(background_img,(400,600))
# import flappy bird
bird_img=pygame.image.load(cwd+r"\\flappy bird\\images\\bird.png")
bird_img=pygame.transform.scale(bird_img,(30,30))
# import tube
tube_img=pygame.image.load(cwd+r"\\flappy bird\\images\\tube.png")
# import tube1_op, tube2_op, tube3_op
tube_op_img=pygame.image.load(cwd+r"\\flappy bird\\images\\tube_op.png")
sound=pygame.mixer.Sound(cwd+r"\\flappy bird\\no6.wav")
sand_img=pygame.image.load(cwd+r"\\flappy bird\\images\\sand.png")
sand_img=pygame.transform.scale(sand_img,(400,40))
tube1_pass=False
tube2_pass=False
tube3_pass=False
pausing=False
running=True
while running:
	pygame.mixer.Sound.play(sound)
	clock.tick(60)
	screen.fill(WHITE)
	screen.blit(background_img,(0,0))
	tube1_img=pygame.transform.scale(tube_img,(tube_width,tube1_height))
	tube1=screen.blit(tube1_img,(tube1_x,0))
	tube2_img=pygame.transform.scale(tube_img,(tube_width,tube2_height))
	tube2=screen.blit(tube2_img,(tube2_x,0))
	tube3_img=pygame.transform.scale(tube_img,(tube_width,tube3_height))
	tube3=screen.blit(tube3_img,(tube3_x,0))
	# add oposite tube
	tube1_op_img=pygame.transform.scale(tube_op_img,(tube_width,600-(tube1_height+space_2tube)))
	tube1_op=screen.blit(tube1_op_img,(tube1_x,tube1_height+space_2tube))
	tube2_op_img=pygame.transform.scale(tube_op_img,(tube_width,600-(tube2_height+space_2tube)))
	tube2_op=screen.blit(tube2_op_img,(tube2_x,tube2_height+space_2tube))
	tube3_op_img=pygame.transform.scale(tube_op_img,(tube_width,600-(tube3_height+space_2tube)))
	tube3_op=screen.blit(tube3_op_img,(tube3_x,tube3_height+space_2tube))
	# Left move of out tube
	if tube1_x<-tube_width:
		tube1_x=550
		tube1_height=randint(100,400)
		tube1_pass=False
		# tube1_img=pygame.transform.scale(tube_img,(tube_width,tube1_height))
		# tube1=screen.blit(tube1_img,(tube1_x,0))
		# tube1_op_img=pygame.transform.scale(tube_op_img,(tube_width,600-(tube1_height+space_2tube)))
		# tube1_op=screen.blit(tube1_op_img,(tube1_x,tube1_height+space_2tube))
	if tube2_x<-tube_width:
		tube2_x=550
		tube2_height=randint(100,400)
		tube2_pass=False
		# tube2_img=pygame.transform.scale(tube_img,(tube_width,tube2_height))
		# tube2=screen.blit(tube1_img,(tube2_x,0))
		# tube2_op_img=pygame.transform.scale(tube_op_img,(tube_width,600-(tube2_height+space_2tube)))
		# tube2_op=screen.blit(tube2_op_img,(tube2_x,tube2_height+space_2tube))
	if tube3_x<-tube_width:
		tube3_x=550
		tube3_height=randint(100,400)
		tube3_pass=False
		# tube3_img=pygame.transform.scale(tube_img,(tube_width,tube3_height))
		# tube3=screen.blit(tube3_img,(tube3_x,0))
		# tube3_op_img=pygame.transform.scale(tube_op_img,(tube_width,600-(tube3_height+space_2tube)))
		# tube3_op=screen.blit(tube3_op_img,(tube3_x,tube3_height+space_2tube))
		
	tube1_x-=tube_velocity
	tube2_x-=tube_velocity
	tube3_x-=tube_velocity
	# Draw sand
	sand=screen.blit(sand_img,(0,560))
	# Draw bird
	bird=screen.blit(bird_img,(x_bird,y_bird))
	# Draw bird fall 
	y_bird+=bird_drop_velocity
	bird_drop_velocity+=gravity
	# Score
	score_txt=font.render("Score: "+str(score),True,YELLOW)
	screen.blit(score_txt,(5,5))
	# Increase Score
	if tube1_x+tube_width<=x_bird and tube1_pass==False:
		score+=1
		tube1_pass=True
	if tube2_x+tube_width<=x_bird and tube2_pass==False:
		score+=1
		tube2_pass=True
	if tube3_x+tube_width<=x_bird and tube3_pass==False:
		score+=1
		tube3_pass=True
	# Test pass to sand or tube
	tubes=[tube1,tube2,tube3,tube1_op,tube2_op,tube3_op,sand]
	for tube in tubes:
		if bird.colliderect(tube):
			pygame.mixer.pause()
			tube_velocity=0
			bird_drop_velocity=0
			game_over_txt=font1.render("Game over, Score: "+str(score),True,RED)
			screen.blit(game_over_txt,(75,250))
			space_txt=font2.render("Press space to continue!",True,BLUE)
			screen.blit(space_txt,(85,290))
			pausing=True
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			running=False
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_SPACE:
				bird_drop_velocity=0 
				bird_drop_velocity=bird_drop_velocity-7
				if pausing:
					pygame.mixer.unpause()
					x_bird=50
					y_bird=350
					tube1_x=400
					tube2_x=600
					tube3_x=800
					tube_width=50
					tube_velocity=2
					score=0
					pausing=False
	pygame.display.flip()
pygame.quit()