import rule
import pygame

#색깔 세팅
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)

di = ["dice1.png", "dice2.png", "dice3.png", "dice4.png", "dice5.png", "dice6.png"]

#주사위 굴리기(랜덤 지정)
rule.roll()
#화면에 나온 이미지와 주사위 눈이 같은지 출력해서 확인
print(rule.dice)

#pygame문법
while True:
    pygame.init()

    display = pygame.display.set_mode((1200, 800))
    display.fill(white)
    #화면에 랜덤으로 뽑은 주사위 출력
    for i in range(5):
        for j in range(1, 7):
            if rule.dice[i] == j:
                image = pygame.image.load(di[j - 1])
                display.blit(image, [240 + 150 * i, 400])

    pygame.display.flip()




