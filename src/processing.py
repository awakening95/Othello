"""
Author : SeongBin Hong
Special thanks to SeongBin!
"""
import numpy as np


def get_reversed_position(board, color, x, y):
    reversed_position_list = []

    for i, j in ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)):  # 모든 방향으로 탐색
        copy_x = x
        copy_y = y
        candidate_list = []
        available_position = False

        while True:
            copy_x += i  # direction 방향으로 이동
            copy_y += j
            if not ((0 <= copy_x <= 7) and (0 <= copy_y <= 7)):  # 맵 바운더리 체크
                break
            now_position_color = board[copy_x][copy_y]  # 해당 위치에 있는 돌을 가져옴
            if now_position_color == 0:  # 공백이면 반환 x
                break
            if now_position_color == color:  # 내 돌 색깔이면 리스트 리턴
                if available_position:  # 뒤집을 돌 있냐
                    reversed_position_list += candidate_list  # 리스트 추가
                break
            candidate_list.append((copy_x, copy_y))  # 상대 돌 색깔이면 리스트에 삽입
            available_position = True

    return reversed_position_list  # 뒤집을 수 있는 돌 모두 리턴


def get_available_position(board, color):
    available_position_list = []

    for x, y in zip(*np.where(board == 0)):
        for i, j in ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)):  # 모든 방향으로 탐색
            copy_x = x
            copy_y = y
            available_position = False

            while True:
                copy_x += i  # direction 방향으로 이동
                copy_y += j
                if not ((0 <= copy_x <= 7) and (0 <= copy_y <= 7)):  # 맵 바운더리 체크
                    available_position = False
                    break
                now_position_color = board[copy_x][copy_y]  # 해당 위치에 있는 돌을 가져옴
                if now_position_color == 0:  # 공백이면 반환 x
                    available_position = False
                    break
                if now_position_color == color:  # 내 돌 색깔이면 리스트 리턴
                    break
                available_position = True  # 상대 돌 색깔이면 리스트에 삽입

            if available_position:  # 뒤집을 돌 있냐
                available_position_list.append([int(x), int(y)])  # 좌표 기입
                break

    return available_position_list  # 착수 가능한 좌표 리스트 반환
