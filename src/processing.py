"""
Author : SeongBin Hong
Special thanks to SeongBin!
"""
import numpy as np
from protocol_enum import *


def chkArrow(map, color, x, y, direction):  # x,y 좌표로부터 direction방향까지 뒤집힐 수 있는 돌을 반환하는 함수
    result = []
    while True:
        x += direction[0]  # direction 방향으로 이동
        y += direction[1]
        if not ((0 <= x <= 7) and (0 <= y <= 7)):  # 맵 바운더리 체크
            break
        nowPositionColor = map[x][y]  # 해당 위치에 있는 돌을 가져옴
        if nowPositionColor == 0:  # 공백이면 반환 x
            break
        if nowPositionColor == color:  # 내 돌 색깔이면 리스트 리턴
            return result
        result.append((x, y))  # 상대 돌 색깔이면 리스트에 삽입
    return []


def getReversedPosition(map, color, x, y):
    direction = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]  # 8개의 방향
    result = []
    for dir in direction:  # 모든 방향으로 탐색
        tmpList = chkArrow(map, color, x, y, dir)  # 해당 방향에 뒤집을 돌 리스트
        if tmpList:  # 뒤집을 돌 있냐?
            result += tmpList  # 리스트 추가
    return result  # 뒤집을 수 있는 돌 모두 리턴


def getAvailablePosition(board, color):
    result = []
    for i, j in zip(*np.where(board == 0)):
        if getReversedPosition(board, color, i, j):  # 해당 좌표가 비어있고, 해당 방향에서 뒤집을 수 있는 돌 리스트가 비어있지 않으면
            result.append((int(i),int(j)))  # 좌표 기입
    return result  # 착수 가능한 좌표 리스트 반환
