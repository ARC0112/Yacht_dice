#prototype of Yacht_dice

import random
import pygame

#색깔 세팅
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)


dice = [0, 0, 0, 0, 0]
dice_count = [0, 0, 0, 0, 0, 0]
dice_keep_list = [0, 0, 0, 0, 0]


#주사위를 굴리는 함수
def roll():
    for i in range(5):
        dice[i]=random.randint(1, 6)

#주사위에 나온 숫자들 각각의 개수를 측정


def count():
    for i in range(0, 6):
        dice_count[i] = dice.count(i + 1)


#aces, deuces, threes, fours, fives, sixes 점수 계산
#함수 자체를 쓰지는 않지만 계산 방식 정리해두려고 놔뒀습니다.
def calculate():
    aces = dice_count[0]
    deuces = dice_count[1] * 2
    threes = dice_count[2] * 3
    fours = dice_count[3] * 4
    fives = dice_count[4] * 5
    sixes = dice_count[5] * 6


#4 of kind는 같은 눈이 4개 이상일때 5개의 눈의 숫자를 모두 더하므로 그냥 4개가 같으면 4 of a kind라고 판단
def four_of_a_kind():
    for i in range(6):
        if dice_count[i] >= 4:
            return sum(dice)

    return 0

#if문으로 굴린 주사위에서 같은 눈이 각각 3개, 2개 있는지 검사하고 count 변수를 +1 모두 검사한 후에 count 변수의 값이 2면 Full House 판단
def full_house():
    count_3 = 0
    count_2 = 0
    for i in range(6):
        if dice_count[i] == 3:
            count_3 += 1
        elif dice_count[i] == 2:
            count_2 += 1
    if count_3 == 1 and count_2 == 1:
        return sum(dice)

    return 0

#1~4까지의 숫자가 dice 리스트안에 들어있으면 count 증가 -> count == 4이면 small_striaght의 조건 완성: 1234 / (1, 2, 3, 4, 4의 경우도 커버 가능)
#밑에 if문을 통해 2345, 3456의 경우를 커버(elif를 쓰면 위의 조건부터 체크, 그렇기 때문에 각각 if문을 써 각자 조건을 체크)
#간단히 생각하면 잘못된 경우가 없을 것 같기는한데 혹시 잘못 작동하는 경우가 있으면 수정해야함!(찾으면 말해주세요)
def small_straight():
    count1 = 0
    count2 = 0
    count3 = 0
    for i in range(1, 5):
        if i in dice:
            count1 += 1
        if i + 1 in dice:
            count2 += 1
        if i + 2 in dice:
            count3 += 1
    if count1 == 4 or count2 == 4 or count3 == 4:
        return 15

    return 0


#먼저 서로 다른 숫자 5개가 나왔는지 확인 -> 이때 1 or 6이 0일경우 Large Straight는 성립하지 않으므로 이를 조건으로 판단
def large_straight():
    count = 0
    for i in range(6):
        if dice_count[i] == 1:
            count += 1
    if count == 5:
        if dice_count[0] == 0:
            return 30
        elif dice_count[5] == 0:
            return 30

    return 0

#나온 주사위의 눈이 모두 같을 때 50점
def yacht():
    for i in range(6):
        if dice_count[i] == 5:
            return 50

    return 0

def keep_button(display):
    pygame.draw.rect(display, black, [750, 500, 150, 50], 1)
    font = pygame.font.SysFont(None, 30)
    text = font.render('ReRoll', True, black)
    display.blit(text, (790, 515))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if (pos[0] >= 750 and  pos[0] <= 900) and (pos[1] >= 500 and pos[1] <= 550):
                for i in range(5):
                    if(dice_keep_list[i]==1):
                        dice_count[dice[i]-1]-=1
                        dice[i]=random.randrange(1,7)
                        dice_keep_list[i]=0
                        dice_count[dice[i]-1]+=1
                        print(dice)
                        print(dice_count)

            elif(pos[0] >= 550 and  pos[0] <= 646) and (pos[1] >= 350 and pos[1] <= 446):
                if(dice_keep_list[0]==0):
                    dice_keep_list[0]=1
                else:
                   dice_keep_list[0]=0
            elif(pos[0] >= 650 and  pos[0] <= 746) and (pos[1] >= 350 and pos[1] <= 446):
                if(dice_keep_list[1]==0):
                    dice_keep_list[1]=1
                else:
                   dice_keep_list[1]=0
            elif(pos[0] >= 750 and  pos[0] <= 846) and (pos[1] >= 350 and pos[1] <= 446):
                if(dice_keep_list[2]==0):
                    dice_keep_list[2]=1
                else:
                   dice_keep_list[2]=0
            elif(pos[0] >= 850 and  pos[0] <= 946) and (pos[1] >= 350 and pos[1] <= 446):
                if(dice_keep_list[3]==0):
                    dice_keep_list[3]=1
                else:
                   dice_keep_list[3]=0
            elif(pos[0] >= 950 and  pos[0] <= 1046) and (pos[1] >= 350 and pos[1] <= 446):
                if(dice_keep_list[4]==0):
                    dice_keep_list[4]=1
                else:
                   dice_keep_list[4]=0
            else:
                print("FAIL")
                return



#점수판
def score_board(display):
    #기본틀 그리기
    pygame.draw.rect(display, black, [50, 5, 400, 780], 1)
    
    # 유저 칸 그리기
    pygame.draw.line(display, black, [228, 30], [428, 30], 3)
    pygame.draw.line(display, black, [428, 30], [428, 130], 3)
    pygame.draw.line(display, black, [228, 30], [228, 130], 3)
    pygame.draw.line(display, black, [328, 30], [328, 130], 3)

    #위 점수판 그리기
    pygame.draw.rect(display, black, [70, 130, 360, 305], 3)
    pygame.draw.line(display, black, [70, 170], [429, 170], 3)
    pygame.draw.line(display, black, [70, 210], [429, 210], 3)
    pygame.draw.line(display, black, [70, 250], [429, 250], 3)
    pygame.draw.line(display, black, [70, 290], [429, 290], 3)
    pygame.draw.line(display, black, [70, 330], [429, 330], 3)
    pygame.draw.line(display, black, [70, 370], [429, 370], 3)
    pygame.draw.line(display, black, [70, 397], [429, 397], 3)
    pygame.draw.line(display, black, [328, 130], [328, 431], 3)
    pygame.draw.line(display, black, [228, 130], [228, 431], 3)
    font = pygame.font.SysFont(None, 25)
    subTotal = font.render("Subtotal", True, black)
    display.blit(subTotal, (80, 378))

    font = pygame.font.SysFont(None, 30)
    bonus = font.render("35 Bonus", True, black)
    display.blit(bonus, (93, 405))

    font = pygame.font.SysFont(None, 35)
    plus = font.render("+", True, black)
    display.blit(plus, (80, 400))

    #CHOICE 칸 만들기
    pygame.draw.rect(display, black, [70, 457, 360, 40], 3)
    pygame.draw.line(display, black, [328, 457], [328, 496], 3)
    pygame.draw.line(display, black, [228, 457], [228, 496], 3)
    pygame.draw.line(display, black, [223, 457], [223, 496], 3)


    #아래 점수판 그리기
    pygame.draw.rect(display, black, [70, 501, 360, 205], 3)
    pygame.draw.line(display, black, [70, 541], [429, 541], 3)
    pygame.draw.line(display, black, [70, 581], [429, 581], 3)
    pygame.draw.line(display, black, [70, 621], [429, 621], 3)
    pygame.draw.line(display, black, [70, 661], [429, 661], 3)
    pygame.draw.line(display, black, [70, 661], [429, 661], 3)
    pygame.draw.line(display, black, [328, 501], [328, 705], 3)
    pygame.draw.line(display, black, [228, 501], [228, 705], 3)
    pygame.draw.line(display, black, [223, 501], [223, 705], 3)


    #TOTAL칸 그리기
    pygame.draw.rect(display, black, [70, 710, 360, 70], 3)
    pygame.draw.line(display, black, [328, 710], [328, 779], 3)
    pygame.draw.line(display, black, [228, 710], [228, 779], 3)
    font = pygame.font.SysFont(None, 30)
    total = font.render("Total", True, black)
    display.blit(total, (82, 735))


    #규칙 그리기
    aces = font.render('Aces', True, black)
    deuces = font.render('Deuces', True, black)
    threes = font.render('Threes', True, black)
    fours = font.render('Fours', True, black)
    fives = font.render('Fives', True, black)
    sixes = font.render('Sixes', True, black)

    display.blit(aces, (112, 143))
    display.blit(deuces, (112, 183))
    display.blit(threes, (112, 223))
    display.blit(fours, (112, 263))
    display.blit(fives, (112, 303))
    display.blit(sixes, (112, 343))

    choice = font.render('Choice', True, black)
    fok = font.render('4 of a Kind', True, black)
    fh = font.render('Full House', True, black)
    s_straight = font.render('S. straight', True, black)
    l_straight = font.render('L. Straight', True, black)
    yacht = font.render('Yacht', True, black)

    display.blit(choice, (112, 470))
    display.blit(fok, (116, 514))
    display.blit(fh, (112, 554))
    display.blit(s_straight, (112, 594))
    display.blit(l_straight, (112, 634))
    display.blit(yacht, (112, 674))


def score_load(display):
    #폰트 설정
    font = pygame.font.SysFont(None, 30)

    #나중에 지울 임시 코드(그냥 리스트에 해당하는 숫자띄우려고 하는 것  +USER1 띄우기)
    font2 = pygame.font.SysFont(None, 100)
    num = font2.render(str(dice), True, black)
    display.blit(num, (605, 250))

    name = font.render('USER1', True, black)
    display.blit(name, (245, 75))

    name = font.render('USER2', True, black)
    display.blit(name, (345, 75))

    #어떤 텍스르를 넣을지 설정
    #Aces, Dueces와 같은 기본 규칙을 반복문으로 표시
    for i in range(6):
        text1 = font.render(str(dice_count[i] * (i + 1)), True, black)
        if dice_count[i] * (i + 1) < 10:
            display.blit(text1, (270, 143 + 40 * i))
        else:
            display.blit(text1, (265, 143 + 40 * i))

    #두자리 수를 같은 위치에 띄우면 균형이 안맞는 것 같아서 if문 써서 살짝 조정
    #Choice나 s_straight와 같은 규칙에 의한 점수를 반복문으로 표시

    s_score = [sum(dice), four_of_a_kind(), full_house(), small_straight(), large_straight(), yacht()]
    j = 0

    for i in s_score:
        text2 = font.render(str(i), True, black)
        if i < 10:
            display.blit(text2, (270, 470 + 40 * j))
        else:
            display.blit(text2, (265, 470 + 40 * j))
        j += 1




