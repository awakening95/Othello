from src.processing import *
from copy import *
import sys

reward_board = [[120, -20, 20, 5, 5, 20, -20, 120],
                [-20, -40, -5, -5, -5, -5, -40, -20],
                [20, -5, 15, 3, 3, 15, -5, 20],
                [5, -5, 3, 3, 3, 3, -5, 5],
                [5, -5, 3, 3, 3, 3, -5, 5],
                [20, -5, 15, 3, 3, 15, -5, 20],
                [-20, -40, -5, -5, -5, -5, -40, -20],
                [120, -20, 20, 5, 5, 20, -20, 120]]

# sys.stdout = open('output.txt', 'w')

"""
reward_board = [[100, -25, 10, 5, 5, 10, -25, -100],
                [-25, -25, 2, 2, 2, 2, -25, -25],
                [10, 2, 5, 1, 1, 5, 2, 10],
                [5, 2, 1, 2, 2, 1, 2, 5],
                [5, 2, 1, 2, 2, 1, 2, 5],
                [10, 2, 5, 1, 1, 5, 2, 10],
                [-25, -25, 2, 2, 2, 2, -25, -25],
                [100, -25, 10, 5, 5, 10, -25, 100]]
"""

reward_board = np.array(reward_board)


# minimax를 이용해 나에게 최적화된 경로를 구한다.
# minimax(board, 3, alpha, beta, True, my_stone_color, 0)
def minimax(board, depth, alpha, beta, my_turn, my_stone_color, opponent_stone_color, sum_my_reward):
    if depth == 0:
        return sum_my_reward, None

    deep_copy_board = deepcopy(board)

    if my_turn is True:
        available_position = getAvailablePosition(deep_copy_board, my_stone_color)
        # print("my_turn_available_position_position:", available_position)
    else:
        available_position = getAvailablePosition(deep_copy_board, opponent_stone_color)
        # print("opponent_turn_available_position_position:", available_position)

    if not available_position:  # 어떤 플레이어가 돌을 둘 수가 없으면 PASS, 다른 플레이어 차례
        # print("PASS")
        if my_turn is True:
            my_turn = False
            available_position = getAvailablePosition(deep_copy_board, opponent_stone_color)  # 다른 플레이어가 돌을 둘 수 있는 곳
            if not available_position:  # 둘다 PASS면
                # print("ALL PASS", sum_my_reward)
                return sum_my_reward, None  # 내가 결과적으로 얻을 수 있는 돌 반환
        else:
            my_turn = True
            available_position = getAvailablePosition(deep_copy_board, my_stone_color)
            if not available_position:
                # print("ALL PASS", sum_my_reward)
                return sum_my_reward, None

    if my_turn:
        max_val = -4096  # 내가 얻을 수 있는 최적의 돌의 갯수
        max_point = [None, None]
        for x, y in available_position:
            changed_points = getReversedPosition(deep_copy_board, my_stone_color, x, y)
            for i, j in changed_points:
                deep_copy_board[i][j] = my_stone_color
            deep_copy_board[x][y] = my_stone_color

            # print("my_turn_pick: ", "depth:", depth, "sum_my_stone:", sum_my_reward, "point:", [x, y])
            val, point = minimax(deep_copy_board, depth - 1, alpha, beta, False, my_stone_color, opponent_stone_color,
                                 sum_my_reward + reward_board[x][y])
            deep_copy_board = deepcopy(board)

            if max_val < val:
                max_val = val
                max_point = [x, y]

            alpha = max(alpha, val)
            if beta <= alpha:
                break

        # print("result => depth:", depth, "max_val:", max_val, "max_point:", max_point)
        return max_val, max_point

    else:
        min_val = 4096
        min_point = [None, None]
        for x, y in available_position:
            changed_points = getReversedPosition(deep_copy_board, opponent_stone_color, x, y)
            for i, j in changed_points:
                deep_copy_board[i][j] = opponent_stone_color
            deep_copy_board[x][y] = opponent_stone_color

            # print("opponent_turn__pick:", "depth:", depth, "sum_my_stone:", sum_my_reward, "point:", [x, y])
            val, point = minimax(deep_copy_board, depth - 1, alpha, beta, True, my_stone_color, opponent_stone_color,
                                 sum_my_reward - reward_board[x][y])

            deep_copy_board = deepcopy(board)

            if min_val > val:
                min_val = val
                min_point = [x, y]

            beta = min(beta, val)
            if beta <= alpha:
                break

        # print("result => depth:", depth, "min_val:", min_val, "min_point:", min_point)
        return min_val, min_point


# 수가 얼마 안남았을 때 mlnimax를 이용해 내가 최적의 돌의 갯수를 얻기 위해 놓아야할 위치를 얻는다.
def get_max_my_stone(board, depth, alpha, beta, my_turn, my_stone_color, opponent_stone_color, sum_my_stone):
    if depth == 0:
        return sum_my_stone, None

    deep_copy_board = deepcopy(board)

    if my_turn is True:
        available_position = getAvailablePosition(deep_copy_board, my_stone_color)
        # print("my_turn_available_position_position:", available_position)
    else:
        available_position = getAvailablePosition(deep_copy_board, opponent_stone_color)
        # print("opponent_turn_available_position_position:", available_position)

    if not available_position:  # 어떤 플레이어가 돌을 둘 수가 없으면 PASS, 다른 플레이어 차례
        # print("PASS")
        if my_turn is True:
            my_turn = False
            available_position = getAvailablePosition(deep_copy_board, opponent_stone_color)  # 다른 플레이어가 돌을 둘 수 있는 곳
            if not available_position:  # 둘다 PASS면
                # print("ALL PASS", sum_my_stone)
                return sum_my_stone, None  # 내가 결과적으로 얻을 수 있는 돌 반환
        else:
            my_turn = True
            available_position = getAvailablePosition(deep_copy_board, my_stone_color)
            if not available_position:
                # print("ALL PASS", sum_my_stone)
                return sum_my_stone, None

    if my_turn:
        max_val = -4096  # 내가 얻을 수 있는 최적의 돌의 갯수
        max_point = [None, None]
        for x, y in available_position:
            changed_points = getReversedPosition(deep_copy_board, my_stone_color, x, y)
            for i, j in changed_points:
                deep_copy_board[i][j] = my_stone_color
            deep_copy_board[x][y] = my_stone_color

            sum_my_stone = len(np.where(deep_copy_board == my_stone_color)[0])
            # print("my_turn_pick: ", "depth:", depth, "sum_my_stone:", sum_my_stone, "point:", [x, y])
            val, point = get_max_my_stone(deep_copy_board, depth - 1, alpha, beta, False, my_stone_color, opponent_stone_color, sum_my_stone)
            deep_copy_board = deepcopy(board)

            if max_val < val:
                max_val = val
                max_point = [x, y]

            alpha = max(alpha, val)
            if beta <= alpha:
                break

        # print("result => depth:", depth, "max_val:", max_val, "max_point:", max_point)
        return max_val, max_point

    else:
        min_val = 4096
        min_point = [None, None]
        for x, y in available_position:
            changed_points = getReversedPosition(deep_copy_board, opponent_stone_color, x, y)
            for i, j in changed_points:
                deep_copy_board[i][j] = opponent_stone_color
            deep_copy_board[x][y] = opponent_stone_color

            sum_my_stone = len(np.where(deep_copy_board == my_stone_color)[0])
            # print("opponent_turn__pick:", "depth:", depth, "sum_my_stone:", sum_my_stone, "point:", [x, y])
            val, point = get_max_my_stone(deep_copy_board, depth - 1, alpha, beta, True, my_stone_color, opponent_stone_color, sum_my_stone)
            deep_copy_board = deepcopy(board)

            if min_val > val:
                min_val = val
                min_point = [x, y]

            beta = min(beta, val)
            if beta <= alpha:
                break

        # print("result => depth:", depth, "min_val:", min_val, "min_point:", min_point)
        return min_val, min_point
