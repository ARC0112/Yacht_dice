import pygame
import rule

#색깔 세팅
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)

#이미지를 리스트로 정리
di = ["dice1.png", "dice2.png", "dice3.png", "dice4.png", "dice5.png", "dice6.png"]

#주사위 굴리기(랜덤 지정)
rule.roll()
rule.count()
#화면에 나온 이미지와 주사위 눈이 같은지 출력해서 확인

#pygame문법
while True:
    pygame.init()
    event = pygame.event.poll()

    #화면 설정
    display = pygame.display.set_mode((1200, 800))
    display.fill(white)

    #화면 이름 설정
    pygame.display.set_caption("Yacht")

    #rule에서 작성한 점수판 함수 실행
    rule.score_board(display)
    rule.score_load(display)


    #화면에 랜덤으로 뽑은 주사위 출력
    #리스트내 주사위의 값이 1~6중 어느 것인지 인식 -> 그에 해당하는 이미지 출력
    for i in range(5):
        for j in range(1, 7):
            if rule.dice[i] == j:
                image = pygame.image.load(di[j - 1])
                display.blit(image, [550 + 100 * i, 350])

    pygame.display.flip()

    #화면 종료 인식 + 인식 시 종료
    if event.type == pygame.QUIT:
        pygame.quit()
        break

