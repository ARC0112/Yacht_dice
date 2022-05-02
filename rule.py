#prototype of Yacht_dice

import random
import pygame
import Yacht_dice

dice = []
dice_count = []

#주사위를 굴리는 함수
def roll():
    for i in range(5):
        dice.append(random.randint(1, 6))

#주사위에 나온 숫자들 각각의 개수를 측정
#dice 리스트의 원소는 5개인데 dice_list 리스트의 원소는 6개 이므로 반복분으로 5개 + 코드 한줄로 만들었습니다.(더 나은 방법이 있으면 수정 부탁드려요!)
def count():
    for i in range(1, 6):
        dice_count.append(dice.count(i))
    dice_count.append(dice.count(6))

#aces, deudces, threes, fours, fives, sixes 점수 계산
def calculate():
    aces = dice_count[0]
    deuces = dice_count[1] * 2
    threes = dice_count[2] * 3
    fours = dice_count[3] * 4
    fives = dice_count[4] * 5
    sixes = dice_count[5] * 6
    print("Aces:", aces)
    print("Deuces:", deuces)
    print("Threes:", threes)
    print("Fours:", fours)
    print("Fives:", fives)
    print("Sixes:", sixes)

#4 of kind는 같은 눈이 4개일때 5개의 눈의 숫자를 모두 더하므로 그냥 4개가 같으면 4 of a kind라고 판단
def four_of_a_kind():
    for i in range(6):
        if dice_count[i] == 4:
            print("4 of a kind!:", sum(dice))

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
        print("Full House!:", sum(dice))

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
        print("small_straighat: 15")


#먼저 서로 다른 숫자 5개가 나왔는지 확인 -> 이때 1 or 6이 0일경우 Large Straight는 성립하지 않으므로 이를 조건으로 판단
def large_straight():
    count = 0
    for i in range(6):
        if dice_count[i] == 1:
            count += 1
    if count == 5:
        if dice_count[0] == 0:
            print("Large Straight: 30")
        elif dice_count[5] == 0:
            print("Large Straight: 30")


#나온 주사위의 눈이 모두 같을 때 50점
def yahtzee():
    for i in range(6):
        if dice_count[i] == 5:
            print("Yahtzee: 50")

